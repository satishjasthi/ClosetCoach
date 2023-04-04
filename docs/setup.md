# Welcome to ClosetCoach - Project Setup Guide

Thank you for your interest in the ClosetCoach project! This guide will
walk you through setting up the project on your local machine, so you
can use it, contribute to it, or just explore the code.

## Prerequisites

Before you dive into the setup process, ensure that you have the
following software installed on your computer:

1.  Python 3.8 or later: [Download
    Python](https://www.python.org/downloads/)
2.  Git: [Download Git](https://git-scm.com/downloads)
3.  Poetry: [Install
    Poetry](https://python-poetry.org/docs/#installation)

## Step 1: Clone the Repository

Begin by cloning the repository to your local machine. Run the following
command in your terminal or command prompt:

`git clone https://github.com/satishjasthi/ClosetCoach.git`

Next, navigate to the project directory:

`cd ClosetCoach`

## Step 2: Set up a Virtual Environment

To isolate project dependencies, we recommend using a virtual
environment. Please note that whenever the term 'python' is used in this
guide, it refers to your locally installed Python 3.8 or later version.
Create a virtual environment using the command below:

`python -m venv venv`

Activate the virtual environment:

-   For Windows:

    powershellCopy code

    `venv\Scripts\activate`

-   For macOS/Linux:

    `source venv/bin/activate`

## Step 3: Install Dependencies with Poetry

Now it's time to install the required dependencies using Poetry:

`poetry install`

## Setp 4: Setup MongoDB
Based on your OS, follow the instructions to install MongoDB [here](https://www.mongodb.com/docs/manual/installation/)

And you can download database [here](https://drive.google.com/file/d/16d4VaRvOQHbMfG39Urzp-uYgC72X63wh/view?usp=sharing)

## Step 4: Scraping Data

With the dependencies installed, you're ready to start scraping the
necessary data for the project.

There are two spiders in the `closetcoach_crawler` directory. The first
one scrapes product page URLs from various product categories, while the
second one extracts product data from the collected product page URLs on
Myntra.

To run the product page URL scraper, execute the following command:

`cd closetcoach_crawler`

`python crawl_urls.py product_page_url_scraper`

Once you have scraped the product page URLs, you can proceed to run the
product data scraper with this command:

`cd closetcoach_crawler`

`python crawl_urls.py product_details_scraper`

That's it! You've successfully set up the ClosetCoach project on your
local machine. Feel free to explore the code, or contribute to the
project. If you encounter any issues or have questions, don't hesitate
to create an issue on the GitHub repository. We appreciate your support
and are excited to have you on board!
