import os
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Choose the database and collection
db = client['ClosetCoach']
collection = db['MyntraProductPageUrls']

# Find all documents in the collection
cursor = collection.find()

bash_script = 'cd ./myntra_spider/myntra_spider\n'
# Iterate through the documents
for document in cursor:
    for url in document['urls']:
        bash_script += f"scrapy crawl product_details_scraper -a start_urls={url}\n"

# save bash script to file
with open('run_product_details_scraper_spider.sh', 'w') as f:
    f.write(bash_script)