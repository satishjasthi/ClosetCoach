import re
import scrapy
import logging
from scrapy.http import HtmlResponse
from data.spiders.myntra_spider.myntra_spider.items import ProductDetails
from scrapy.loader import ItemLoader
from data.spiders.myntra_spider.myntra_spider.utils import get_page_source


class ProductDetailsScraperSpider(scrapy.Spider):
    name = "product_details_scraper"
    allowed_domains = ["myntra.com"]

    def start_requests(self):
        url = getattr(self, "start_urls", [])
        html = get_page_source(
            url,
            click_button_xpath='//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[3]/div/div[4]/div[2]',
        )
        # send scrapy request with selenium's resopnse as meta info
        yield scrapy.Request(url=url, callback=self.parse, meta={"html": html})

    def parse(self, response):
        # convert selenium's resonse as scrapy based html response
        html_response = HtmlResponse(
            url=response.url, body=response.meta["html"], encoding="utf-8"
        )
        loader = ItemLoader(item=ProductDetails(), response=html_response)
        loader.add_value("product_page_url", html_response.url)
        loader.add_value("product_id", html_response.url.split("/")[-2])
        loader.add_xpath(
            "product_name",
            '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[1]/text()',
        )
        loader.add_xpath(
            "product_description",
            '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[2]/text()',
        )
        loader.add_xpath(
            "product_rating",
            '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/div/div/div[1]/text()',
        )
        loader.add_xpath(
            "product_num_reviews",
            '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/div/div/div[3]/text()',
        )
        loader.add_xpath(
            "product_price_after_discount",
            '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[1]/strong/text()',
        )
        loader.add_xpath(
            "product_category",
            '//*[@id="mountRoot"]/div/div[1]/main/div[1]/a[4]/text()',
        )

        # extract image urls
        divs = html_response.xpath('//div[@class="image-grid-image"]')

        for div in divs:
            # Extract the style attribute value
            style = div.xpath("@style").get()

            # Use a regular expression to extract the URL from the style attribute value
            url_match = re.search(r'url\(["\']?(.+?)["\']?\)', style)

            if url_match:
                url = url_match.group(1)
                loader.add_value("product_image_urls", url)

        # extract product metadata
        product_details_div = html_response.xpath(
            '//div[@class="pdp-productDescriptorsContainer"]'
        )

        headings = product_details_div.xpath(".//h4/text()").getall()
        contents = product_details_div.xpath(".//p/text()").getall()

        details_dict = {}
        for i in range(len(headings)):
            details_dict[headings[i].strip()] = contents[i].strip()

        spec_rows = product_details_div.xpath('.//div[contains(@class, "index-row")]')
        for row in spec_rows:
            key = row.xpath('.//div[contains(@class, "index-rowKey")]/text()').get()
            value = row.xpath('.//div[contains(@class, "index-rowValue")]/text()').get()
            if key and value:
                details_dict[key.strip()] = value.strip()
        loader.add_value("product_metadata", details_dict)
        yield loader.load_item()
