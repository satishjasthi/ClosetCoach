# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient
from itemadapter import ItemAdapter


class MongoDBPipeline:
    def __init__(self, mongo_uri, mongo_db, collection_name):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE", "items"),
            collection_name={
                "product_page_urls_collection_name": crawler.settings.get(
                    "MYNTRA_PRODUCT_PAGE_URLS_COLLECTION", None
                ),
                "product_details_collection_name": crawler.settings.get(
                    "MYNTRA_PRODUCT_PAGE_INFO_COLLECTION", None
                ),
            },
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.product_page_urls_collection = self.db[
            self.collection_name["product_page_urls_collection_name"]
        ]
        self.product_details_collection = self.db[
            self.collection_name["product_details_collection_name"]
        ]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if spider.name == "product_page_url_scraper":
            key_to_update = item["category"]
            new_urls = item["urls"]
            existing_record = self.product_page_urls_collection.find_one(
                {"key": key_to_update}
            )
            if existing_record:
                # check if the new URLs already exist in the record
                existing_urls = existing_record["urls"] if existing_record else []
                new_urls = [url for url in new_urls if url not in existing_urls]

                # update the record with the new URLs
                self.product_page_urls_collection.update_one(
                    {"key": key_to_update}, {"$push": {"urls": {"$each": new_urls}}}
                )
            else:
                # if urls does not exist then update the DB
                self.product_page_urls_collection.insert_one(
                    {"key": key_to_update, "urls": new_urls}
                )
            return item
        elif spider.name == "product_details_scraper":
            key_to_update = item["product_id"]
            # get the existing record

            existing_record = self.product_details_collection.find_one(
                {"product_id": key_to_update}
            )
            if existing_record:
                # if product info exists just pass dont change the data
                pass
            else:
                self.product_details_collection.insert_one(ItemAdapter(item).asdict())
            return item
