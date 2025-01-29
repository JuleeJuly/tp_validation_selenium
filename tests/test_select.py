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

@scenario('features/widget.feature', "Selecting options")
def test_select():
    pass

@given('I am on the select page')
def open_select_page(browser):
    browser.get('https://demoqa.com/select-menu')
    browser.fullscreen_window()
    time.sleep(1)

@when('I select options from the different dropdowns')
def select_options(browser):
    #Cliquer sur le selecteur
    browser.find_element(By.ID, 'withOptGroup').click()
    #Localiser l'élément et scroller jusqu'à lui
    element = browser.find_element(By.ID, "react-select-2-option-3")
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    element.click()
    browser.execute_script("window.scrollBy(0, 300);")
    time.sleep(1)
    #Cliquer sur le selecteur
    browser.find_element(By.ID, 'selectOne').click()
    #Localiser l'élément et scroller jusqu'à lui
    element = browser.find_element(By.ID, "react-select-3-option-0-5")
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    element.click()
    time.sleep(1)
    #Chosir une option dans le selecteur
    select_aqua = Select(browser.find_element(By.ID, 'oldSelectMenu'))
    select_aqua.select_by_visible_text('Aqua')
    #Cliquer sur le selecteur
    browser.find_element(By.XPATH, "//div[7]//div[@class=' css-1hwfws3']").click()
    time.sleep(1)
    browser.find_element(By.ID, "react-select-4-option-0").click()
    browser.find_element(By.ID, "react-select-4-option-1").click()
    browser.find_element(By.ID, "react-select-4-option-2").click()
    browser.find_element(By.ID, "react-select-4-option-3").click()
    time.sleep(1)
    browser.find_element(By.XPATH,"//option[.='Audi']").click()
    #Chosir une option dans le selecteur
    time.sleep(1)

@then('the options should be selected')
def verify_select_options(browser):
    # Vérifier que les options sont bien sélectionnée
    assert browser.find_element(By.ID, 'withOptGroup').text == "Another root option"
    assert browser.find_element(By.ID, 'selectOne').text == "Other"
    select_aqua = Select(browser.find_element(By.ID, 'oldSelectMenu'))
    selected_option = select_aqua.first_selected_option
    assert selected_option.get_attribute("value") == "10", "L'option sélectionnée est incorrecte"
    select_cars = Select(browser.find_element(By.ID, 'cars'))
    assert select_cars.first_selected_option.text == "Audi", "L'option sélectionnée est incorrecte"