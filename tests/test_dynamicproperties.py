import pytest
import pytest_bdd
import time

from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, when, then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('features/element.feature', "Testing dynamic properties")
def test_dynamic():
    pass

@given('I am on the dynamic properties page')
def open_dynamic_page(browser):
    browser.get('https://demoqa.com/dynamic-properties')
    browser.fullscreen_window()
    time.sleep(1)

@when('the 5-second timer expires')
def timer(browser):
    time.sleep(1)
    button_disabled = browser.find_element(By.ID, "enableAfter")
    assert not button_disabled.is_enabled()
    button_color = browser.find_element(By.ID, "colorChange")
    color = button_color.value_of_css_property("color")
    assert color == "rgba(255, 255, 255, 1)"
    time.sleep(5)

@then('the button s color changes')
def button_color(browser):
    button_disabled = browser.find_element(By.ID, "enableAfter")
    assert button_disabled.is_enabled()
    button_color = browser.find_element(By.ID, "colorChange")
    new_color = button_color.value_of_css_property("background-color")
    assert new_color == "rgba(0, 123, 255, 1)"