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

@scenario('features/element.feature', "Interacting with radio buttons")
def test_radio_button():
    pass

@given('I am on the radio buttons page')
def open_radio_page(browser):
    browser.get('https://demoqa.com/radio-button')
    browser.fullscreen_window()
    time.sleep(1)

@when('I select different options')
def radio_button(browser):
    time.sleep(1)
    browser.find_element(By.XPATH, '//label[text()="Yes"]').click()
    # Trouver le bouton radio par son attribut value ou son texte
    yes_button = browser.find_element(By.XPATH, "//input[@type='radio' and @id='yesRadio']")
    time.sleep(1)
    verify_button(browser,"Yes",yes_button)
    browser.find_element(By.XPATH, '//label[text()="Impressive"]').click()
    # Trouver le bouton radio par son attribut value ou son texte
    impressive_button = browser.find_element(By.XPATH, "//input[@type='radio' and @id='impressiveRadio']")
    time.sleep(1)
    verify_button(browser,"Impressive",impressive_button)       

@then('the No radio button should be disabled')
def verify_radio_button(browser):
    radio_button = browser.find_element(By.ID, "noRadio")
    assert not radio_button.is_enabled(), "Le bouton radio ne devrait pas être activé !"

def verify_button(browser,find_word,radio_button):
    # Vérifier que le bouton est bien sélectionné
    assert radio_button.is_selected(), "Le bouton radio n'a pas été sélectionné !"
    element = browser.find_element(By.CLASS_NAME, 'text-success')
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    text = element.text
    # Word to search for
    word = find_word
    # Verify the number of occurrences of the word
    assert text.count(word) == 1