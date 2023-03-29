# Scraping Myntra Product Data Part2: Product Data and Metadata
Welcome back! In our [previous tutorial](./scraping_myntra_product_data_part1.md), we learned how to use Scrapy to collect product page URLs from Myntra. In this sequel tutorial, we will build on that knowledge and learn how to use Scrapy to scrape product data from those URLs.

By collecting product data, we can build machine learning models and provide personalized fashion recommendations to users through ClosetCoach. This will help users save time and make more informed purchasing decisions

The source code provided in the previous tutorial showed a spider called `ProductDetailsScraperSpider`. This spider extracts product data using `ItemLoader` and `XPath` selectors. The data includes the product name, description, rating, number of reviews, price after discount, category, and image URLs. Additionally, it extracts product metadata, such as specifications and other details.

This spider is crucial for the ClosetCoach project, as it enables us to collect large amounts of product data from Myntra. With this data, we can train machine learning models to recommend products that match a user's style and preferences. This will help users to save time and make more informed purchasing decisions.

Now that you understand the importance of this spider for the `ClosetCoach` project, let's take a closer look at the code. The start_requests method initiates requests to the URLs provided as start_urls. For each URL, it checks if the product page details already exist and, if not, initiates a request to scrape the data using `scrapy.Request`.

```python
def start_requests(self):
    urls = getattr(self, "start_urls", []).split(",")
    if isinstance(urls, str):
        urls = [urls]
    for url in urls:
        # check if product page details already exists
        url_exists = check_if_product_exists(url)
        if not url_exists:
            logging.info(f"Scraping product page details from {url}")
            yield scrapy.Request(url=url, callback=self.parse)
        else:
            logging.info(f"Product page details already exists for {url}")

```

The `parse` method extracts the data from the response and creates a ProductDetails object using `ItemLoader`. The `ItemLoader` object allows us to load data into ProductDetails fields using `XPath` selectors.

```python
def parse(self, response):
    # generate selenium's response
    html = get_page_source(response.url, click_button_xpath='//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[3]/div/div[4]/div[2]')
    # convert selenium's resonse as scrapy based html response
    html_response = HtmlResponse(url=response.url, body=html, encoding="utf-8")
    loader = ItemLoader(item=ProductDetails(), response=html_response)
    # add data to item using xpath selectors
    loader.add_value("product_page_url", html_response.url)
    loader.add_value("product_id", html_response.url.split("/")[-2])
    loader.add_xpath("product_name", '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[1]/text()')
    loader.add_xpath("product_description", '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[2]/text()')
    loader.add_xpath("product_rating", '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/div/div/div[1]/text()')
    loader.add_xpath("product_num_reviews", '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/div/div/div[3]/text()')
    loader.add_xpath("product_price_after_discount", '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[1]/strong/text()')
```
Next lets see the section that extracts image URLs 

```python
divs = html_response.xpath('//div[@class="image-grid-image"]')

for div in divs:
    # Extract the style attribute value
    style = div.xpath("@style").get()

    # Use a regular expression to extract the URL from the style attribute value
    url_match = re.search(r'url\(["\']?(.+?)["\']?\)', style)

    if url_match:
        url = url_match.group(1)
        loader.add_value("product_image_urls", url)
```

This code extracts the image URLs for a product from the `html_response`. It first selects all `div` elements with a class of "image-grid-image" using XPath selectors. It then loops over each `div` element and extracts the value of the `style` attribute using `xpath("@style").get()`. It then uses a regular expression to extract the URL from the `style` attribute value using `re.search`. Finally, it adds each URL to the `product_image_urls` field of the `ProductDetails` object using `loader.add_value`.

The section that extracts product metadata is shown below:

```python
product_details_div = html_response.xpath('//div[@class="pdp-productDescriptorsContainer"]')

headings = product_details_div.xpath(".//h4/text()").getall()
contents = product_details_div.xpath(".//p/text()").getall()

details_dict = {}
for i in range(len(headings)):
    try:
        details_dict[headings[i].strip()] = contents[i].strip()
    except IndexError:
        pass

spec_rows = product_details_div.xpath('.//div[contains(@class, "index-row")]')
for row in spec_rows:
    key = row.xpath('.//div[contains(@class, "index-rowKey")]/text()').get()
    value = row.xpath('.//div[contains(@class, "index-rowValue")]/text()').get()
    if key and value:
        details_dict[key.strip()] = value.strip()

loader.add_value("product_metadata", details_dict)
```

This code extracts the product metadata, such as specifications and other details, from the `html_response`. It first selects the `div` element with a class of "pdp-productDescriptorsContainer" using XPath selectors. It then selects all `h4` and `p` elements within this `div` using `.//h4/text()` and `.//p/text()` XPath selectors, respectively.

It creates an empty dictionary called `details_dict` and populates it with the product metadata by iterating over the `headings` and `contents` lists. For each iteration, it tries to add the `heading` as a key and the corresponding `content` as a value to `details_dict`.

Next, it selects all `div` elements containing "index-row" in their class using `'.//div[contains(@class, "index-row")]'` XPath selector. It then extracts the `key` and `value` of each row using `'.//div[contains(@class, "index-rowKey")]/text()'` and `'.//div[contains(@class, "index-rowValue")]/text()'` XPath selectors, respectively. Finally, it adds the `key-value` pairs to `details_dict`.

Finally, it adds the entire `details_dict` to the `product_metadata` field of the `ProductDetails` object using `loader.add_value`.
