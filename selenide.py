from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

driver: WebDriver = ...
timeout = 4

def wait():
    return WebDriverWait(driver, timeout=timeout, ignored_exceptions=(WebDriverException,))


class element_value_is_empty(object):
    def __init__(self, selector):
        self.selector = selector

    def __call__(self, driver):
        return (driver.find_element(By.CSS_SELECTOR, self.selector)
                .get_attribute('value') == '')

    def __str__(self):
        return f'Value of element {self.selector} is empty'


class Element:
    def __init__(self, selector):
        self.selector = selector

    def should_be_blank(self):
        wait().until(element_value_is_empty(self.selector))


def open_page(url):
    driver.get(url)











