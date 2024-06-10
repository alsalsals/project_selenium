from __future__ import annotations

from typing import Callable

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

driver: WebDriver = ...
timeout = 4

def wait():
    return WebDriverWait(driver, timeout=timeout, ignored_exceptions=(WebDriverException,))


class element_value_is_empty(object):
    def __init__(self, locate: Callable[[], WebElement]):
        self.locate = locate

    def __call__(self, driver):
        return self.locate().get_attribute('value') == ''

    def __str__(self):
        return f'Value of element {self.locate} is empty'


class Element:
    def __init__(self, locate: Callable[[], WebElement]):
        self.locate = locate

    def should_be_blank(self):
        wait().until(element_value_is_empty(self.locate))
        return self

    def set_value(self, text) -> Element:
        def command(driver):
            webelement = self.locate()
            webelement.clear()
            webelement.send_keys(text)
            return True

        wait().until(command)
        return self

    def press_enter(self) -> Element:
        def command(driver):
            webelement = self.locate()
            webelement.send_keys(Keys.ENTER)
            return True

        wait().until(command)
        return self

    def click(self) -> Element:
        def command(driver):
            webelement = self.locate()
            webelement.click()
            return True

        wait().until(command)
        return self

    def element(self, selector: str) -> Element:
        return Element(lambda: self.locate().find_element(By.CSS_SELECTOR, selector))


def open_page(url):
    driver.get(url)


def element(selector: str):
    return Element(lambda: driver.find_element(By.CSS_SELECTOR, selector))
