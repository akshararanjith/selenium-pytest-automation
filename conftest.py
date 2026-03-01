import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver= webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
    