from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumDriver:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()

    def slowly_scroll_to_page_bottom(self) -> webdriver.Firefox:
        """
        Slowly scrolls to the bottom of the current page.

        :return: The updated webdriver instance with the scrolled page.
        """
        scroll_pause_time = 1
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0, last_height, int(last_height / 12)):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(scroll_pause_time)
        return self.driver

    def load_page(self, url: str) -> bool:
        """
        Loads the given URL in the webdriver and scrolls the page.

        :param url: The URL to load.
        :return: True if successful.
        """
        self.driver.get(url)
        try:
            self.scroll_to_element(
                element_xpath='//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[4]'
            )
        except:
            self.slowly_scroll_to_page_bottom()
        self.slowly_scroll_to_page_top()
        return True

    def slowly_scroll_to_page_top(self) -> webdriver.Firefox:
        """
        Slowly scrolls to the top of the current page from the bottom.

        :return: The updated webdriver instance with the scrolled page.
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

    def scroll_to_element(self, element_xpath: str) -> webdriver.Firefox:
        """
        Scrolls to the specified element on the current page.

        :param element_xpath: The XPath of the target element.
        :return: The updated webdriver instance with the scrolled page.
        """
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, element_xpath))
        )
        # Scroll to the element
        target_element = self.driver.find_element(By.XPATH, element_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", target_element)
        return self.driver

    def close_driver(self) -> None:
        """
        Closes the webdriver instance.
        """
        self.driver.quit()


def get_page_source(url: str, click_button_xpath: str = None) -> str:
    """
    Retrieves the page source of the given URL, optionally clicks a button.

    :param url: The URL to retrieve the page source from.
    :param click_button_xpath: The optional XPath of the button to click.
    :return: The HTML page source as a string.
    """
    browser = SeleniumDriver()
    browser.load_page(url)
    if click_button_xpath:
        try:
            click_button_element = browser.driver.find_element(
                By.XPATH, click_button_xpath
            )
            click_button_element.click()
        except:
            pass
        time.sleep(1)

    html = browser.driver.page_source
    browser.close_driver()
