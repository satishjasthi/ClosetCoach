# import scrapy
# from itemloaders.processors import Join, MapCompose, TakeFirst
# from scrapy.utils.project import get_project_settings
# from itemloaders.processors import MapCompose

# SETTINGS = get_project_settings()


# def add_prefix_to_url(url):
#     return "https://www.myntra.com" + "/" + url


# def fetch_category(url):
#     return url.split("/")[-1].split("?")[0]


# class ProductPageUrl(scrapy.Item):
#     urls = scrapy.Field(input_processor=MapCompose(str.strip, add_prefix_to_url))
#     category = scrapy.Field(
#         serializer=str,
#         input_processor=MapCompose(fetch_category),
#         output_processor=lambda x: x[0],
#     )


# def convert_to_float(string_num):
#     try:
#         return float(string_num)
#     except ValueError:
#         return string_num

# def remove_newline(string):
#     return string.replace("\n", " ")

# def remove_rupee_symbol(string):
#     return string.replace("₹", "")

# class ProductDetails(scrapy.Item):
#     product_page_url = scrapy.Field(serializer=str, output_processor=TakeFirst())
#     product_name = scrapy.Field(
#         serializer=str,
#         input_processor=MapCompose(str.strip),
#         output_processor=TakeFirst(),
#     )
#     product_description = scrapy.Field(
#         serializer=str,
#         input_processor=MapCompose(str.strip, remove_newline),
#         output_processor=Join(" "),
#     )
#     product_rating = scrapy.Field(
#         serializer=float,
#         input_processor=MapCompose(str.strip, convert_to_float),
#         output_processor=TakeFirst(),
#     )
#     product_num_reviews = scrapy.Field(
#         serializer=str,
#         input_processor=MapCompose(str.strip, convert_to_float),
#         output_processor=TakeFirst(),
#     )
#     product_price_after_discount = scrapy.Field(
#         serializer=float,
#         input_processor=MapCompose(str.strip, remove_rupee_symbol, convert_to_float),
#         output_processor=TakeFirst(),
#     )
#     product_image_urls = scrapy.Field(
#         serializer=str,
#         input_processor=MapCompose(str.strip),
#         output_processor=Join(", "),
#     )
#     product_category = scrapy.Field(
#         serializer=str,
#         input_processor=MapCompose(str.strip),
#         output_processor=TakeFirst(),
#     )
#     product_id = scrapy.Field(
#         serializer=str,
#         input_processor=MapCompose(str.strip),
#         output_processor=TakeFirst(),
#     )
#     product_metadata = scrapy.Field(serializer=dict)


import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from scrapy.utils.project import get_project_settings

SETTINGS = get_project_settings()


def add_prefix_to_url(url: str) -> str:
    """
    Adds the Myntra base URL as a prefix to the given relative URL.

    :param url: The relative URL to be prefixed.
    :return: The absolute URL with the base URL prefixed.
    """
    return "https://www.myntra.com" + "/" + url


def fetch_category(url: str) -> str:
    """
    Extracts the category name from a given URL.

    :param url: The URL containing the category name.
    :return: The category name extracted from the URL.
    """
    return url.split("/")[-1].split("?")[0]


class ProductPageUrl(scrapy.Item):
    """
    The item containing the product page URLs and their corresponding categories.
    """

    urls = scrapy.Field(input_processor=MapCompose(str.strip, add_prefix_to_url))
    category = scrapy.Field(
        serializer=str,
        input_processor=MapCompose(fetch_category),
        output_processor=lambda x: x[0],
    )


def convert_to_float(string_num: str) -> float:
    """
    Converts a string to a float if possible.

    :param string_num: The string representation of a number.
    :return: The float representation of the number or the original string if conversion fails.
    """
    try:
        return float(string_num)
    except ValueError:
        return string_num


def remove_newline(string: str) -> str:
    """
    Removes newline characters from the given string.

    :param string: The input string.
    :return: The string without newline characters.
    """
    return string.replace("\n", " ")


def remove_rupee_symbol(string: str) -> str:
    """
    Removes the Rupee symbol from the given string.

    :param string: The input string containing the Rupee symbol.
    :return: The string without the Rupee symbol.
    """
    return string.replace("₹", "")


class ProductDetails(scrapy.Item):
    """
    The item containing the product details.
    """

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
