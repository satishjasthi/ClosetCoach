from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse


class SeleniumDriver:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()

    def slowly_scroll_to_page_bottom(self):
        """
        Function to slowly scroll to the bottom of current page
        """
        scroll_pause_time = 1
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0, last_height, int(last_height / 12)):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(scroll_pause_time)
        return self.driver

    def load_page(self, url):
        self.driver.get(url)
        self.slowly_scroll_to_page_bottom()
        self.slowly_scroll_to_page_top()
        return True

    def slowly_scroll_to_page_top(self):
        """
        Function to slowly scroll to the top of current page from bottom
        """
        scroll_pause_time = 0.5
        # Get scroll height
        last_height = 0

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        return self.driver

    def close_driver(self):
        self.driver.quit()


def get_page_source(url, click_button_xpath: str = None):
    browser = SeleniumDriver()
    browser.load_page(url)
    if click_button_xpath:
        browser.driver.find_element(By.XPATH, click_button_xpath).click()
        time.sleep(3)
    html = browser.driver.page_source
    browser.close_driver()
    return html
