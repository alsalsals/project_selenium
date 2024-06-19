import pytest
import os


@pytest.fixture(autouse=True)
def browser_management():

    browser.config.window_width = os.getenv('window_width', '2050')
    browser.config.window_height = os.getenv('window_width', '1441')
    browser.config.timeout = float(os.getenv('timeout', '5.0'))
