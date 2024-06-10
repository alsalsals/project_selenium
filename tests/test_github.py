from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

import selenide as browser


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.open_page('https://github.com/alsalsals/project_selene')
browser.Element('[itemprop="name"]').should_be_blank()



