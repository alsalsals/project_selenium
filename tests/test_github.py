from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

import selenide as browser


browser.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

query = browser.Element('[name=q]')

browser.open_page('https://google.com')
query.should_be_blank()
query.set_value('alsalsals').press_enter()

browser.Element('#rso .g').element('adfs').click()
