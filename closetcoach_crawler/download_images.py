"""
Script to download all the images from a fashion database
"""
import asyncio
from dataclasses import dataclass
from typing import List, Optional
import aiohttp
from motor.motor_asyncio import AsyncIOMotorClient


@dataclass
class ImageMetaData:
    product_id: str
    urls: List[str]

    def __eq__(self, other):
        """
        Method to compare two ImageMetaData objects
        """
        if isinstance(other, ImageMetaData):
            return (self.product_id == other.product_id 
                    and set(self.urls) == set(other.urls))
        return False

    def __hash__(self):
        """
        Method to hash ImageMetaData objects based on their product ID and URLs
        """
        return hash((self.product_id, tuple(sorted(self.urls))))


@dataclass
class ImageData:
    product_id: str
    url:str
    binary_image: Optional[bytes] = None


# create a corountine to save data to mongodb
async def save_to_mongodb(collection, image_data):
    """ 
    Save image data to MongoDB
    :param collection: collection to save image to
    :param image_data: ImageData object containing the productID and binary image data
    :return: None
    """
    # Find the document with given product ID and update it with new image data
    document = await collection.find_one_and_update(
        {"product_id": image_data.product_id},
        {"$push": {"image_data": image_data.binary_image}},
        upsert=True,
    )
    if document is None:
        # Document does not already exist, create a new one
        await collection.insert_one(
            {
                "product_id": image_data.product_id,
                "image_data": [image_data.binary_image],
            }
        )


# async function to download images
async def download_image(session, image_metadata, collection, errors):
    """
    Download image from given url in an asynchronous manner
    :param session: aiohttp session
    :param image_metadata: ImageMetaData object containing the productID and list of urls of the image to download
    :param collection: collection to save image to
    :return: None
    """
    for url in image_metadata.urls:
        image_data = ImageData(product_id=image_metadata.product_id, url=url)
        async with session.get(image_data.url) as response:
            # Check if the request was successful (status code 200)
            if response.status == 200:
                # Read the image content
                image_data.binary_image = await response.read()
                # Store the image to MongoDB instead of writing it to a file
                await save_to_mongodb(collection, image_data)
            else:
                print(
                    f"Failed to download image from url {image_data.url}\n. Status code: {response.status}"
                )
                errors.append(image_data.url)


async def batch_download_images():
    """
    Download images from a list of urls asynchronously
    :return: None
    """
    mongo_uri = "mongodb://localhost:27017/"
    errors = []
    completed_urls = set()
    client = AsyncIOMotorClient(mongo_uri)
    db = client["ClosetCoach"]
    collection = db["MyntraProductData"]

    images_metadata_list = []
    cursor = await collection.find().to_list(length=None)
    for document in cursor:
        try:
            images_metadata_list.append(
                ImageMetaData(product_id=document["product_id"], 
                          urls=document["product_image_urls"].split(', '))
            )
        except KeyError:
            print(f"🚨🚨🚨Product with ID {document['product_id']} has no image urls in database.")

    async with aiohttp.ClientSession() as session:
        while len(completed_urls) < len(images_metadata_list):
            for index, image_metadata in enumerate(images_metadata_list):
                if image_metadata not in completed_urls:
                    try:
                        await download_image(session, image_metadata, collection, errors)
                        completed_urls.add(image_metadata)
                    except:
                        print(f"Error downloading image with metadata:\n{image_metadata}")
                    if (index + 1) % 10 == 0:
                        print(
                            "Waiting for 20 seconds before making next batch of 10 more requests."
                        )
                        await asyncio.sleep(20)
            if len(errors) > 0:
                print(
                    f"{len(errors)} images failed to download. Retrying in 5 seconds."
                )
                for error in errors:
                    print(error)
                errors = []
                await asyncio.sleep(60)
    client.close()
    print("All images downloaded successfully.")


if __name__ == "__main__":
    asyncio.run(batch_download_images())
