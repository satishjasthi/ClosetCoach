import scrapy
import logging
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from myntra_spider.items import ProductPageUrl
from myntra_spider.utils import get_page_source
from scrapy.utils.project import get_project_settings

logging.getLogger("selenium").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

MAX_PAGE_NUM = 10
PAGE_NUMS = {}


class ProductPageUrlScraper(scrapy.Spider):
    name = "product_page_url_scraper"
    allowed_domains = ['myntra.com']

    def start_requests(self):
        url = getattr(self, "start_urls", [])
        html = get_page_source(url)
        # send scrapy request with selenium's resopnse as meta info
        PAGE_NUMS[url.split("/")[-1]] = 0
        yield scrapy.Request(url=url, callback=self.parse, meta={"html": html})

    def parse(self, response):
        # convert selenium's resonse as scrapy based html response
        html_response = HtmlResponse(
            url=response.url, body=response.meta["html"], encoding="utf-8"
        )
        loader = ItemLoader(item=ProductPageUrl(), response=html_response)
        loader.add_xpath(
            "urls",
            "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]/section/ul/li/a/@href",
        )
        loader.add_value("category", html_response.url)
        yield loader.load_item()
        # check if next page exists
        PAGE_NUMS[response.url.split("/")[-1].split("?")[0]] += 1
        next_page = html_response.xpath(
            '//*[@id="desktopSearchResults"]/div[2]/section/div[2]/ul/li[12]/a/@href'
        ).extract_first()
        if next_page is not None:
            if PAGE_NUMS[response.url.split("/")[-1].split("?")[0]] < MAX_PAGE_NUM:
                html = get_page_source(next_page)
                yield scrapy.Request(
                    url=next_page, callback=self.parse, meta={"html": html}
                )