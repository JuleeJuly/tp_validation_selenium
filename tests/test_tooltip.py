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

@scenario('features/widget.feature', "Displaying a tooltip")
def test_tooltip():
    pass

@given('I am on the tooltip page')
def open_tooltip_page(browser):
    browser.get('https://demoqa.com/tool-tips')
    browser.fullscreen_window()
    time.sleep(1)

@when('I hover my mouse over an element')
def mouse_hover(browser):
    verify_tool_tip_by_id(browser,'toolTipButton','tooltip-inner')
    verify_tool_tip_by_id(browser,'toolTipTextField','tooltip-inner')
    verify_tool_tip_by_XPATH(browser,"//a[.='Contrary']",'tooltip-inner')
    verify_tool_tip_by_XPATH(browser,"//a[.='1.10.32']",'tooltip-inner')

@then('a message appears indicating that my mouse is over the element')
def verify_mouse_hover(browser):
    pass

def verify_tool_tip_by_id(browser,id_element,id_message):
    # Trouver l'élément sur lequel passer la souris
    element = browser.find_element(By.ID, id_element)
    # Créer une instance d'ActionChains
    actions = ActionChains(browser)
    # Effectuer le mouse hover
    actions.move_to_element(element).perform()
    time.sleep(2)
    # Vérifier la présence du tooltip
    tooltip = browser.find_element(By.CLASS_NAME, id_message)
    assert tooltip.is_displayed()

def verify_tool_tip_by_XPATH(browser,element,id_message):
    # Trouver l'élément sur lequel passer la souris
    element = browser.find_element(By.XPATH, element)
    # Créer une instance d'ActionChains
    actions = ActionChains(browser)
    # Effectuer le mouse hover
    actions.move_to_element(element).perform()
    time.sleep(2)
    # Vérifier la présence du tooltip
    tooltip = browser.find_element(By.CLASS_NAME, id_message)
    assert tooltip.is_displayed()