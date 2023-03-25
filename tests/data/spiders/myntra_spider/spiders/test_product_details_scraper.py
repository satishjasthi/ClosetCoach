"""
This script is used to test the ProductDetailsScraperSpider spider from the myntra_spider
project. It tests the start_requests and parse methods of the spider.
"""

import unittest
from unittest.mock import MagicMock
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
from scrapy.utils.test import get_crawler
from tests.test_data.constants import TEST_PRODUCT_DETAILS


from data.spiders.myntra_spider.myntra_spider.spiders.product_details_scraper import (
    ProductDetailsScraperSpider,
)


class TestProductDetailsScraperSpider(unittest.TestCase):
    """
    This class contains methods to test the ProductPageUrlScraper spider.
    """

    def setUp(self):
        """
        This method is used to set up the test by initializing the crawler and the spider.
        """
        self.crawler = get_crawler(
            ProductDetailsScraperSpider, settings_dict=get_project_settings()
        )
        self.spider = self.crawler.spidercls()

    def test_start_requests(self):
        """
        This method tests the start_requests method of the spider.
        """
        # Set the spider's start_urls to the first page URL in the constants file
        self.spider.start_urls = TEST_PRODUCT_DETAILS["7546900"]["product_page_url"]
        # Mock the spider's get_page_source method
        self.spider.get_page_source = MagicMock(return_value="<html></html>")
        # Call the start_requests method and check the scraped_data
        requests = list(self.spider.start_requests())
        assert len(requests) == 1
        assert isinstance(requests[0], Request)
        assert requests[0].url == TEST_PRODUCT_DETAILS["7546900"]["product_page_url"]

    def test_parse(self):
        """
        This method will tests the parse method of ProductDetailsScraperSpider spider.
        """
        for product_id in TEST_PRODUCT_DETAILS.keys():
            with open(TEST_PRODUCT_DETAILS[product_id]["html_file_path"]) as f:
                body = f.read()
            response = MagicMock()
            response.url = TEST_PRODUCT_DETAILS[product_id]["product_page_url"]
            response.meta = {"html": body}
            item = list(self.spider.parse(response))[0]
            print(item)
            assert (
                item["product_page_url"]
                == TEST_PRODUCT_DETAILS[product_id]["product_page_url"]
            )
            assert item["product_id"] == TEST_PRODUCT_DETAILS[product_id]["product_id"]
            assert (
                item["product_name"] == TEST_PRODUCT_DETAILS[product_id]["product_name"]
            )
            assert (
                item["product_description"]
                == TEST_PRODUCT_DETAILS[product_id]["product_description"]
            )
            assert (
                item["product_rating"]
                == TEST_PRODUCT_DETAILS[product_id]["product_rating"]
            )
            assert (
                item["product_num_reviews"]
                == TEST_PRODUCT_DETAILS[product_id]["product_num_reviews"]
            )
            assert (
                item["product_price_after_discount"]
                == TEST_PRODUCT_DETAILS[product_id]["product_price_after_discount"]
            )
            assert (
                item["product_category"]
                == TEST_PRODUCT_DETAILS[product_id]["product_category"]
            )
            assert (
                item["product_image_urls"]
                == TEST_PRODUCT_DETAILS[product_id]["product_image_urls"]
            )
            assert (
                item["product_metadata"]
                == TEST_PRODUCT_DETAILS[product_id]["product_metadata"]
            )

    # Clean up the test by stopping the crawler
    def tearDown(self):
        """
        This method is used to clean up the test by stopping the crawler.
        """
        self.crawler.stop()
