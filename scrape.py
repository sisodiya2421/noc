import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import logging


class Scrapper():
    def __init__(self):
        self.img_urls = []
        self.driver = webdriver.Firefox()

    def scrape(self, url):
        # Establish chrome driver and go to report site URL
        self.driver.get(url)

        # Scrolling down to the end of the page to load all images of the page
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

        try:
            actual_imgs = self.driver.find_elements(
                By.CSS_SELECTOR, 'img.img-responsive')
            for actual_img in actual_imgs:
                if actual_img.get_attribute('src') and 'https' in actual_img.get_attribute('src'):
                    self.img_urls.append(actual_img.get_attribute('src'))
        except ElementNotInteractableException as err:
            logging.exception(f"Error occured while extraction : {err}")
        try:
            next_page = self.driver.find_element(
                By.CSS_SELECTOR, 'li.pagination-next > a').get_attribute('href')
        except NoSuchElementException:
            logging.info("Last Page Reached")
            next_page = None

        scrapped_data = {
            'img_url': self.img_urls,
        }
        # return next page url and extracted data from Myntra
        data = {
            'next_page': next_page,
            'scrapped_data': scrapped_data
        }
        return data
