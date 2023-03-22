# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient


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
            collection_name=crawler.settings.get(
                "MYNTRA_PRODUCT_PAGE_URLS_COLLECTION", "scrapy_items"
            ),
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.collection_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item_dict = dict(item)
        key_to_update = item["category"]
        new_urls = item["urls"]
        existing_record = self.collection.find_one({"key": key_to_update})
        if existing_record:
            # check if the new URLs already exist in the record
            existing_urls = existing_record["urls"] if existing_record else []
            new_urls = [url for url in new_urls if url not in existing_urls]

            # update the record with the new URLs
            self.collection.update_one(
                {"key": key_to_update}, {"$push": {"urls": {"$each": new_urls}}}
            )
        else:
            # if urls does not exist then update the DB
            self.collection.insert_one({"key": key_to_update, "urls": new_urls})
        return item
