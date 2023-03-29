# import scrapy
# import logging
# from scrapy.http import HtmlResponse
# from scrapy.loader import ItemLoader
# from myntra_spider.items import ProductPageUrl
# from myntra_spider.utils import get_page_source

# logging.getLogger("selenium").setLevel(logging.CRITICAL)
# logging.getLogger("urllib3").setLevel(logging.CRITICAL)

# MAX_PAGE_NUM = 10
# PAGE_NUMS = {}


# class ProductPageUrlScraper(scrapy.Spider):
#     name = "product_page_url_scraper"
#     allowed_domains = ['myntra.com']

#     def start_requests(self):
#         urls = getattr(self, "start_urls", []).split(",")
#         if isinstance(urls, str):
#             urls = [urls]
#         for url in urls:
#             # send scrapy request with selenium's resopnse as meta info
#             PAGE_NUMS[url.split("/")[-1]] = 0
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         # get selenium's response
#         html = get_page_source(response.url)
#         # convert selenium's resonse as scrapy based html response
#         html_response = HtmlResponse(
#             url=response.url, body=html, encoding="utf-8"
#         )
#         loader = ItemLoader(item=ProductPageUrl(), response=html_response)
#         loader.add_xpath(
#             "urls",
#             "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]/section/ul/li/a/@href",
#         )
#         loader.add_value("category", html_response.url)
#         yield loader.load_item()
#         # check if next page exists
#         PAGE_NUMS[response.url.split("/")[-1].split("?")[0]] += 1
#         next_page = html_response.xpath(
#             '//*[@id="desktopSearchResults"]/div[2]/section/div[2]/ul/li[12]/a/@href'
#         ).extract_first()
#         if next_page is not None:
#             if PAGE_NUMS[response.url.split("/")[-1].split("?")[0]] < MAX_PAGE_NUM:
#                 html = get_page_source(next_page)
#                 yield scrapy.Request(
#                     url=next_page, callback=self.parse, meta={"html": html}
#                 )

import scrapy
import logging
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from myntra_spider.items import ProductPageUrl
from myntra_spider.utils import get_page_source

# Set logging levels for external libraries
logging.getLogger("selenium").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

MAX_PAGE_NUM = 10
PAGE_NUMS = {}


class ProductPageUrlScraper(scrapy.Spider):
    name = "product_page_url_scraper"
    allowed_domains = ["myntra.com"]

    def start_requests(self) -> scrapy.Request:
        """
        Initiates requests to the URLs provided as start_urls.

        :return: A generator of scrapy.Request instances.
        """
        # Get the URLs and initiate requests
        urls = getattr(self, "start_urls", []).split(",")
        if isinstance(urls, str):
            urls = [urls]
        for url in urls:
            # Initialize the page number for each URL
            PAGE_NUMS[url.split("/")[-1]] = 0
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: scrapy.http.Response) -> scrapy.Item:
        """
        Parses the response obtained from start_requests.

        :param response: The scrapy.http.Response object.
        :return: A generator of scrapy.Item instances.
        """
        # Get the page source using Selenium
        html = get_page_source(response.url)

        # Convert Selenium response to Scrapy response
        html_response = HtmlResponse(url=response.url, body=html, encoding="utf-8")

        # Load and process the item
        loader = ItemLoader(item=ProductPageUrl(), response=html_response)
        loader.add_xpath(
            "urls",
            "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]/section/ul/li/a/@href",
        )
        loader.add_value("category", html_response.url)
        yield loader.load_item()

        # Update the page number
        PAGE_NUMS[response.url.split("/")[-1].split("?")[0]] += 1

        # Check if there is a next page
        next_page = html_response.xpath(
            '//*[@id="desktopSearchResults"]/div[2]/section/div[2]/ul/li[12]/a/@href'
        ).extract_first()

        # If next page exists and the maximum page number is not reached, initiate a request for the next page
        if next_page is not None:
            if PAGE_NUMS[response.url.split("/")[-1].split("?")[0]] < MAX_PAGE_NUM:
                html = get_page_source(next_page)
                yield scrapy.Request(
                    url=next_page, callback=self.parse, meta={"html": html}
                )
