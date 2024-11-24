import pytest
from selenium import webdriver

driver = None
@pytest.fixture()
def setup():
    print("Start the browser")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()
    print("Close the browser")


def test_1(setup):
    driver.get("http://www.google.co.in/")
    print("Test 1 executed")


def test_2(setup):
    driver.get("https://www.facebook.com/")
    print("Test 2 executed")


def test_3(setup):
    driver.get("https://www.gmail.com")
    print("Test 3 executed")
