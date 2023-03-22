import scrapy
from scrapy.utils.project import get_project_settings
from itemloaders.processors import MapCompose

SETTINGS = get_project_settings()


def add_prefix_to_url(url):
    return "https://www.myntra.com" + "/" + url


def fetch_category(url):
    return url.split("/")[-1].split("?")[0]


class ProductPageUrl(scrapy.Item):
    urls = scrapy.Field(input_processor=MapCompose(str.strip, add_prefix_to_url))
    category = scrapy.Field(
        serializer=str,
        input_processor=MapCompose(fetch_category),
        output_processor=lambda x: x[0],
    )
