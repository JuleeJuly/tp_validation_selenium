import pytest
import pytest_bdd
import time

from selenium.webdriver.support.ui import Select
from pytest_bdd import parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, when, then

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('features/element.feature', "Following links sends an API call")
def test_open_link():
    pass

@given('I am on the Links Page')
def open_browser_windows_page(browser):
    browser.get('https://demoqa.com/links')
    browser.fullscreen_window()
    
@when('I try the different links')
def open_link(browser):
    time.sleep(1)
    browser.execute_script("window.scrollBy(0, 500);")
    # click on the link
    click_link(browser,'created')
    verify_link(browser,"201","Created")
    # click on the link
    click_link(browser,'no-content')
    verify_link(browser,"204","No Content")
    # click on the link
    click_link(browser,'moved')
    verify_link(browser,"301","Moved Permanently")
    # click on the link
    click_link(browser,'bad-request')
    verify_link(browser,"400","Bad Request")
    # click on the link
    click_link(browser,'unauthorized')
    verify_link(browser,"401","Unauthorized")
    # click on the link
    click_link(browser,'forbidden')
    verify_link(browser,"403","Forbidden")
    # click on the link
    click_link(browser,'invalid-url')
    verify_link(browser,"404","Not Found")

@then('the API returns the corresponding status code')
def response_api(browser):
    pass


def click_link(browser,id_link):
    # click on the link
    time.sleep(1)
    link = browser.find_element(By.ID, id_link)
    link.click()
    time.sleep(1)

def verify_link(browser,code,message):
    # Retrieve the text
    element = browser.find_element(By.ID, 'linkResponse')
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    text = element.text
    # Word to search for
    word = code
    word2 = message
    # Verify the number of occurrences of the word
    word_count = text.count(word)
    word_count2 = text.count(word2)
    assert word_count == 1
    assert word_count2 == 1