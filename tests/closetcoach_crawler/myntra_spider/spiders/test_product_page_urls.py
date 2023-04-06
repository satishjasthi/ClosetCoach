"""
This script is used to test the ProductPageUrlScraper spider from the myntra_spider
project. It tests the start_requests and parse methods of the spider.
"""

import unittest
from unittest.mock import MagicMock
from scrapy.utils.project import get_project_settings
from scrapy.utils.test import get_crawler
from scrapy.utils import reactor
from twisted.internet import asyncioreactor


from closetcoach_crawler.myntra_spider.spiders.product_page_urls import (
    ProductPageUrlScraper,
)
from tests.test_data.constants import TEST_PRODUCT_URLS


class TestProductPageUrlScraper(unittest.TestCase):
    """
    This class contains methods to test the ProductPageUrlScraper spider.
    """

    def setUp(self):
        """
        This method is used to set up the test by initializing the crawler and the spider.
        """
        self.crawler = get_crawler(
            ProductPageUrlScraper, settings_dict=get_project_settings()
        )
        self.spider = self.crawler.spidercls()

    def test_parse(self):
        """
        This method tests the parse method of the spider.
        """
        # Open the first test data file and read its contents into a variable
        for category in TEST_PRODUCT_URLS.keys():
            with open(TEST_PRODUCT_URLS[category]["html_file_path"]) as f:
                body = f.read()
            # Mock a response object and set its url and meta attributes
            response = MagicMock()
            response.url = TEST_PRODUCT_URLS[category]["page_url"]
            response.meta = {"html": body, "test": True}
            # Call the parse method and check the scraped_data
            scraped_data = list(self.spider.parse(response))[0]
            self.assertEqual(
                len(scraped_data["urls"]),
                len(TEST_PRODUCT_URLS[category]["urls"]),
            )
            self.assertEqual(scraped_data["category"], category)
            self.assertTrue(scraped_data["urls"], TEST_PRODUCT_URLS[category]["urls"])

    # Clean up the test by stopping the crawler
    def tearDown(self):
        """
        This method is used to clean up the test by stopping the crawler.
        """
        self.crawler.stop()
        del self.spider
        del self.crawler
