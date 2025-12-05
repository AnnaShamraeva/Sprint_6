import pytest
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service

from curl import Url



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(Url.main_page)
    yield driver
    driver.quit()
