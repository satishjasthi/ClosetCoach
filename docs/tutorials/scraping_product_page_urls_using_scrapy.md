# Scraping Myntra Product Data Part1: Product Page URLs
In this tutorial, we'll be looking at how to scrape product page URLs from Myntra using Scrapy, which is a crucial step in building the ClosetCoach project. By collecting product information from Myntra's website, we can use it to train machine learning models and provide personalized fashion recommendations to users.

Let's take a closer look at the source code provided in the previous question. First, we define the spider's `start_requests` method to initiate requests to the URLs provided as `start_urls`. These URLs can be updated to target specific categories of products that we want to collect information on. For example, we could target men's clothing with the following code:

```python
class ProductPageUrlScraper(scrapy.Spider):     
    name = "product_page_url_scraper"     
    allowed_domains = ["myntra.com"]     
    start_urls = ["https://www.myntra.com/men-clothing"]
```

Next, we define the `parse` method, which extracts product page URLs and product categories using `ItemLoader` and XPath selectors. We then yield a `ProductPageUrl` item object, which contains the URL and category of the product:

```python
def parse(self, response: scrapy.http.Response) -> scrapy.Item:
    loader = ItemLoader(item=ProductPageUrl(), response=response)
    loader.add_xpath(
        "urls",
        "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]/section/ul/li/a/@href",
    )
    loader.add_value("category", response.url)
    yield loader.load_item()
```

Finally, we check if there's a next page using XPath, and if so, we initiate a new request for that page. We also keep track of the page number using a dictionary called `PAGE_NUMS`, which ensures that we don't scrape more pages than necessary:

```python
next_page = response.xpath(
    '//*[@id="desktopSearchResults"]/div[2]/section/div[2]/ul/li[12]/a/@href'
).extract_first()
if next_page is not None:
    if PAGE_NUMS[response.url.split("/")[-1].split("?")[0]] < MAX_PAGE_NUM:
        yield scrapy.Request(url=next_page, callback=self.parse)

```

And that's it! By running this spider, we can collect product page URLs and categories from Myntra's website, which will be used in the ClosetCoach project to provide personalized fashion recommendations to users.

I hope this tutorial has been helpful in getting started with Scrapy and web scraping. Happy coding!

## Previous Tutorial: Introduction to Scrapy
[Go to Previous Tutorial](./intro_to_scrapy.md)

## Next Tutorial: Scraping Myntra Product Data Part1: Product Data and Metadata
[Go to Next Tutorial](./scraping_myntra_product_data.md)

