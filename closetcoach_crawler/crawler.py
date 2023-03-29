"""
This script is used to run Scrapy spiders for scraping data from Myntra. It currently supports
two spiders: 'product_page_url_scraper' and 'product_details_scraper'. The script establishes a
connection to a MongoDB instance for storing the scraped data and handles the configuration and
execution of the Scrapy spiders.
"""

import argparse
import logging
import time
from typing import Any
from scrapy import signals
from pymongo import MongoClient
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from myntra_spider.spiders.product_details_scraper import ProductDetailsScraperSpider
from myntra_spider.spiders.product_page_urls import ProductPageUrlScraper

settings = get_project_settings()


def configure_spider(spider_name: str) -> None:
    """
    Configures and starts a Scrapy spider based on the given spider_name.

    :param spider_name: The name of the spider to run.
    """
    process = CrawlerProcess(settings)

    # database connection
    MONGO_URI = settings.get("MONGO_URI")
    MONGO_DATABASE = settings.get("MONGO_DATABASE")
    MYNTRA_PRODUCT_PAGE_URL_COLLECTION = settings.get(
        "MYNTRA_PRODUCT_PAGE_URLS_COLLECTION"
    )
    logging.info(f"Connecting to database {MONGO_DATABASE} at {MONGO_URI}")
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DATABASE]

    try:
        if spider_name == "product_page_url_scraper":
            urls = settings.get("MYNTRA_PRODUCT_CATEGORY_URLS")
            process.crawl(ProductPageUrlScraper, start_urls=",".join(urls))
            process.start()
            time.sleep(5)  # Add a sleep duration between each batch

        elif spider_name == "product_details_scraper":
            logging.info(f"Using collection: {MYNTRA_PRODUCT_PAGE_URL_COLLECTION}")
            collection = db[MYNTRA_PRODUCT_PAGE_URL_COLLECTION]
            cursor = collection.find()
            urls_list = []
            for document in cursor:
                urls_list.extend(document["urls"])

            process.crawl(ProductDetailsScraperSpider, start_urls=",".join(urls_list))
            process.start()
    except KeyError:
        print(f"Spider '{spider_name}' not found. Check the name and try again.")


def run_spider(spider_name: str) -> None:
    """
    Runs the Scrapy spider with the given spider_name.

    :param spider_name: The name of the spider to run.
    """
    configure_spider(spider_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Run a Scrapy spider to scrape data from Myntra.

        Currently supports product_page_url_scraper and product_details_scraper.

        Usage: python -m closetcoach_crawler spider_name"""
    )
    parser.add_argument("spider", help="The name of the spider to run.", nargs="?")

    args = parser.parse_args()

    if args.spider is not None:
        run_spider(args.spider)
    else:
        parser.print_help()
    # run_spider("product_details_scraper")
