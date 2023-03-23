"""
This script is used to test the ProductPageUrlScraper spider from the myntra_spider
project. It tests the start_requests and parse methods of the spider.
"""

import unittest
from unittest.mock import MagicMock
from scrapy.utils.project import get_project_settings
from scrapy.utils.test import get_crawler
from scrapy.http import Request
from scrapy.utils import reactor
from twisted.internet import asyncioreactor

from data.spiders.myntra_spider.myntra_spider.spiders.product_page_urls import (
    ProductPageUrlScraper,
)
from tests.test_data.constants import PRODUCT_CATEGORY_DETAILS

# Install the AsyncioSelectorReactor and set it as the default reactor for Scrapy
asyncioreactor.install()
reactor.reactor = asyncioreactor.AsyncioSelectorReactor()


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

    def test_start_requests(self):
        """
        This method tests the start_requests method of the spider.
        """
        # Set the spider's start_urls to the first page URL in the constants file
        self.spider.start_urls = PRODUCT_CATEGORY_DETAILS["men-tshirts"]["page_url"]
        # Mock the spider's get_page_source method
        self.spider.get_page_source = MagicMock(return_value="<html></html>")
        # Call the start_requests method and check the scraped_data
        requests = list(self.spider.start_requests())
        assert len(requests) == 1
        assert isinstance(requests[0], Request)
        assert requests[0].url == PRODUCT_CATEGORY_DETAILS["men-tshirts"]["page_url"]

    def test_parse(self):
        """
        This method tests the parse method of the spider.
        """
        # Open the first test data file and read its contents into a variable
        for category in PRODUCT_CATEGORY_DETAILS.keys():
            with open(PRODUCT_CATEGORY_DETAILS[category]["html_file_path"]) as f:
                body = f.read()
            # Mock a response object and set its url and meta attributes
            response = MagicMock()
            response.url = PRODUCT_CATEGORY_DETAILS[category]["page_url"]
            response.meta = {"html": body}
            # Call the parse method and check the scraped_data
            scraped_data = list(self.spider.parse(response, test=True))[0]
            self.assertEqual(
                len(scraped_data["urls"]),
                len(PRODUCT_CATEGORY_DETAILS[category]["urls"]),
            )
            self.assertEqual(scraped_data["category"], category)
            self.assertTrue(
                scraped_data["urls"], PRODUCT_CATEGORY_DETAILS[category]["urls"]
            )

    # Clean up the test by stopping the crawler
    def tearDown(self):
        """
        This method is used to clean up the test by stopping the crawler.
        """
        self.crawler.stop()
