import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import logging


class Scrapper():
    def __init__(self):
        self.img_urls = []
        self.names = []
        self.brands = []
        self.prices = []
        self.ratings = []
        self.driver = webdriver.Firefox()

    def scrape(self, url):
        # Establish chrome driver and go to report site URL
        self.driver.get(url)

        # Scrolling down to the end of the page to load all images of the page
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

        try:
            products = self.driver.find_elements(By.CLASS_NAME, 'product-base')
            for product in products:
                try:
                    name = product.find_element(
                        By.CSS_SELECTOR, 'h4.product-product').text
                    brand = product.find_element(
                        By.CSS_SELECTOR, 'h3.product-brand').text
                    img_url = product.find_element(
                        By.CSS_SELECTOR, 'img.img-responsive').get_attribute('src')
                    rating = product.find_element(
                        By.CSS_SELECTOR, 'div.product-ratingsContainer > span').text
                    try:
                        price = product.find_element(
                            By.CLASS_NAME, 'product-discountedPrice').text
                    except:
                        price = product.find_element(
                            By.CLASS_NAME, 'product-price').text
                except NoSuchElementException:
                    continue
                self.names.append(name)
                self.brands.append(brand)
                self.prices.append(price)
                self.img_urls.append(img_url)
                self.ratings.append(rating)
        except ElementNotInteractableException as err:
            logging.exception(f"Error occured while extraction : {err}")

        try:
            next_page = self.driver.find_element(
                By.CSS_SELECTOR, 'li.pagination-next > a').get_attribute('href')
        except NoSuchElementException:
            logging.info("Last Page Reached")
            next_page = None

        scrapped_data = {
            'product': self.names,
            'brand': self.brands,
            'price': self.prices,
            'rating': self.ratings,
            'img_url': self.img_urls,
        }
        # return next page url and extracted data from Myntra
        data = {
            'next_page': next_page,
            'scrapped_data': scrapped_data
        }
        return data
