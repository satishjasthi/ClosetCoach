BOT_NAME = "myntra_spider"

SPIDER_MODULES = ["myntra_spider.spiders"]
NEWSPIDER_MODULE = "myntra_spider.spiders"

DOWNLOAD_DELAY = 5

MYNTRA_PRODUCT_CATEGORY_URLS = [
    "https://www.myntra.com/men-tshirts",
    "https://www.myntra.com/men-casual-shirts",
    "https://www.myntra.com/men-formal-shirts",
    "https://www.myntra.com/men-sweatshirts",
    "https://www.myntra.com/men-sweaters",
    "https://www.myntra.com/men-jackets",
    "https://www.myntra.com/men-blazers",
    "https://www.myntra.com/men-suits",
    "https://www.myntra.com/rain-jacket",
    "https://www.myntra.com/men-jeans",
    "https://www.myntra.com/men-casual-trousers",
    "https://www.myntra.com/men-formal-trousers",
    "https://www.myntra.com/mens-shorts",
    "https://www.myntra.com/men-trackpants",
    "https://www.myntra.com/men-casual-shoes",
    "https://www.myntra.com/men-sports-shoes",
    "https://www.myntra.com/men-formal-shoes",
    "https://www.myntra.com/men-sneakers",
    "https://www.myntra.com/men-sandals",
    "https://www.myntra.com/men-flip-flops",
    "https://www.myntra.com/men-socks",
    "https://www.myntra.com/men-sports-shoes",
    "https://www.myntra.com/men-sports-sandals",
    "https://www.myntra.com/men-sports-wear-tshirts",
    "https://www.myntra.com/men-trackpants-shorts",
    "https://www.myntra.com/men-tracksuits",
    "https://www.myntra.com/men-sports-jackets",
    "https://www.myntra.com/men-sports-accessories",
    "https://www.myntra.com/men-swimwear",
    "https://www.myntra.com/men-kurtas",
    "https://www.myntra.com/sherwani",
    "https://www.myntra.com/nehru-jackets",
    "https://www.myntra.com/dhoti",
    "https://www.myntra.com/men-sunglasses",
    "https://www.myntra.com/women-kurtas-kurtis-suits",
    "https://www.myntra.com/ethnic-tops",
    "https://www.myntra.com/saree",
    "https://www.myntra.com/women-ethnic-wear",
    "https://www.myntra.com/women-ethnic-bottomwear?f=categories%3AChuridar%2CLeggings%2CSalwar",
    "https://www.myntra.com/skirts-palazzos",
    "https://www.myntra.com/dress-material",
    "https://www.myntra.com/lehenga-choli",
    "https://www.myntra.com/dupatta-shawl",
    "https://www.myntra.com/women-jackets",
    "https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen",
    "https://www.myntra.com/tops",
    "https://www.myntra.com/myntra-fashion-store?f=Categories%3ATshirts%3A%3AGender%3Amen%20women%2Cwomen",
    "https://www.myntra.com/women-jeans",
    "https://www.myntra.com/women-trousers",
    "https://www.myntra.com/women-shorts-skirts",
    "https://www.myntra.com/myntra-fashion-store?f=Categories%3AClothing%20Set%2CCo-Ords%3A%3AGender%3Amen%20women%2Cwomen",
    "https://www.myntra.com/playsuit?f=Gender%3Amen%20women%2Cwomen",
    "https://www.myntra.com/jumpsuits?f=Gender%3Amen%20women%2Cwomen",
    "https://www.myntra.com/women-shrugs",
    "https://www.myntra.com/women-sweaters-sweatshirts",
    "https://www.myntra.com/women-jackets-coats",
    "https://www.myntra.com/women-blazers-waistcoats",
    "https://www.myntra.com/flats",
    "https://www.myntra.com/women-casual-shoes",
    "https://www.myntra.com/women-heels",
    "https://www.myntra.com/women-boots-menu?f=Type_article_attr%3Aflat%20boots%2Cheeled%20boots",
    "https://www.myntra.com/women-sports-shoes",
    "https://www.myntra.com/women-sportswear-clothing",
    "https://www.myntra.com/women-sports-shoes",
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Configure item pipelines
ITEM_PIPELINES = {"myntra_spider.pipelines.MongoDBPipeline": 300}

MONGO_URI = "mongodb://localhost:27017"
MONGO_DATABASE = "ClosetCoach"
MYNTRA_PRODUCT_PAGE_URLS_COLLECTION = "MyntraProductPageUrls"
MYNTRA_PRODUCT_PAGE_INFO_COLLECTION = "MyntraProductData"
MYNTRA_PRODUCT_PAGE_URLS_FAILED_REQUESTS_COLLECTION = (
    "MyntraProductPageUrlsFailedRequests"
)
MYNTRA_PRODUCT_PAGE_INFO_FAILED_REQUESTS_COLLECTION = (
    "MyntraProductPageInfoFailedRequests"
)


# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# handle failed urls
DOWNLOADER_MIDDLEWARES = {
    "myntra_spider.middlewares.FailedURLMiddleware": 543,
}
