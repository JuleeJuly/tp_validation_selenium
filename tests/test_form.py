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

@scenario('features/form.feature', "Entering data into the form")
def test_open():
    pass

@given('I am on the form page')
def open_browser_windows_page(browser):
    browser.get('https://demoqa.com/automation-practice-form')
    browser.fullscreen_window()
    
@when('I enter data into the required fields')
def enter_data(browser):
    #Vérification de la présence des champs du formulaire
    assert browser.find_element(By.ID, 'lastName').is_displayed()
    assert browser.find_element(By.ID, 'firstName').is_displayed()
    assert browser.find_element(By.ID, 'userEmail').is_displayed()
    assert browser.find_element(By.XPATH, '//label[text()="Female"]').is_displayed()
    assert browser.find_element(By.ID, 'userNumber').is_displayed()
    assert browser.find_element(By.ID, 'dateOfBirthInput').is_displayed()
    #actions
    browser.find_element(By.ID, 'lastName').send_keys('Mason')
    browser.find_element(By.ID, 'firstName').send_keys('Jason')
    browser.find_element(By.ID, 'userEmail').send_keys('jason.mason@jm.fr')
    browser.find_element(By.XPATH, '//label[text()="Male"]').click()
    browser.find_element(By.ID, 'userNumber').send_keys('0102030102')
    time.sleep(3)
    #input_element = browser.find_element(By.ID, 'dateOfBirthInput')
    elementDate = browser.find_element(By.ID, "subjectsContainer")
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", elementDate)
    time.sleep(2)
    browser.find_element(By.ID, 'dateOfBirthInput').click()
    select_month = Select(browser.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select'))
    select_month.select_by_visible_text('June')
    select_year = Select(browser.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select'))
    select_year.select_by_visible_text('1999')
    browser.find_element(By.XPATH, '//div[text()="3"]').click()
    time.sleep(3)
    #Localiser l'élément et scroller jusqu'à lui
    element = browser.find_element(By.ID, "submit")
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(1)
    browser.find_element(By.ID, 'subjectsInput').send_keys('Maths')
    browser.find_element(By.ID, 'subjectsInput').send_keys('\uE007')
    time.sleep(1)
    browser.find_element(By.XPATH, '//label[text()="Sports"]').click()
    browser.find_element(By.ID, 'currentAddress').send_keys('1 rue de la paix')
    check_form(browser)

@then('I should be able to submit the form')
def submit_form(browser):
    time.sleep(1)
    browser.find_element(By.ID, 'submit').click()
    time.sleep(1)
    text = browser.find_element(By.ID, 'example-modal-sizes-title-lg').text
    phrase = "Thanks for submitting the form"
    # Verify the number of occurrences of the word
    word_count = text.count(phrase)
    assert word_count == 1
    print('Test Ok')

def check_form(browser):
    assert browser.find_element(By.ID, 'lastName').get_attribute('value') == 'Mason'
    assert browser.find_element(By.ID, 'firstName').get_attribute('value') == 'Jason'
    assert browser.find_element(By.ID, 'userEmail').get_attribute('value') == 'jason.mason@jm.fr'
    assert browser.find_element(By.ID, 'userNumber').get_attribute('value') == '0102030102'
    assert browser.find_element(By.ID, 'currentAddress').get_attribute('value') == '1 rue de la paix'