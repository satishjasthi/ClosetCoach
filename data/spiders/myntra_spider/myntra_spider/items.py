import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
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


def convert_to_float(string_num):
    try:
        return float(string_num)
    except ValueError:
        return string_num

def remove_newline(string):
    return string.replace("\n", " ")

def remove_rupee_symbol(string):
    return string.replace("₹", "")

class ProductDetails(scrapy.Item):
    product_page_url = scrapy.Field(serializer=str, output_processor=TakeFirst())
    product_name = scrapy.Field(
        serializer=str,
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
    )
    product_description = scrapy.Field(
        serializer=str,
        input_processor=MapCompose(str.strip, remove_newline),
        output_processor=Join(" "),
    )
    product_rating = scrapy.Field(
        serializer=float,
        input_processor=MapCompose(str.strip, convert_to_float),
        output_processor=TakeFirst(),
    )
    product_num_reviews = scrapy.Field(
        serializer=str,
        input_processor=MapCompose(str.strip, convert_to_float),
        output_processor=TakeFirst(),
    )
    product_price_after_discount = scrapy.Field(
        serializer=float,
        input_processor=MapCompose(str.strip, remove_rupee_symbol, convert_to_float),
        output_processor=TakeFirst(),
    )
    product_image_urls = scrapy.Field(
        serializer=str,
        input_processor=MapCompose(str.strip),
        output_processor=Join(", "),
    )
    product_category = scrapy.Field(
        serializer=str,
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
    )
    product_id = scrapy.Field(
        serializer=str,
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
    )
    product_metadata = scrapy.Field(serializer=dict)
