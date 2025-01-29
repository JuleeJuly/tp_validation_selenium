import pytest
import pytest_bdd
import time

from selenium.webdriver.support.ui import Select
from pytest_bdd import parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given,when,then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('features/books.feature', "Registering a new user")
def test_book():
    pass

@given('I am on the user registration page')
def open_books_page(browser):
    browser.get('https://demoqa.com/register')
    browser.fullscreen_window()

@when('I enter the required information')
def add_user(browser):
    #Vérification de la présence des champs du formulaire
    assert browser.find_element(By.ID, 'lastname').is_displayed()
    assert browser.find_element(By.ID, 'firstname').is_displayed()
    assert browser.find_element(By.ID, 'userName').is_displayed()
    assert browser.find_element(By.ID, 'password').is_displayed()
    #actions
    browser.find_element(By.ID, 'lastname').send_keys('Jean4')
    browser.find_element(By.ID, 'firstname').send_keys('Michel4')
    browser.find_element(By.ID, 'userName').send_keys('JeanMich4')
    browser.find_element(By.ID, 'password').send_keys('Test01234!')
    element = browser.find_element(By.ID, 'register')
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(2)
    #Identifier l'iframe reCAPTCHA
    try:
        iframe = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]"))
        )
        browser.switch_to.frame(iframe)
        print("Switch dans l'iframe réussi !")
        #cliquer sur la case je ne suis pas un robot
        captcha_checkbox = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
        )
        # Simuler un vrai mouvement de souris avant de cliquer
        ActionChains(browser).move_to_element(captcha_checkbox).click().perform()
        # Attendre que le CAPTCHA soit validé
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='recaptcha-checkbox-checked']"))
        )
        print("CAPTCHA validé !")
    except Exception as e:
        print(f"Erreur lors du traitement du CAPTCHA : {e}")
    finally:
        browser.switch_to.default_content()
        print("Retour à la page principale !")

@when('I submit the registration')
def valid_user(browser): 
    browser.find_element(By.ID, 'register').click()
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert.accept()

@then("I should see that the user has been successfully added")
def verify_user(browser):
    browser.find_element(By.ID, 'gotologin').click()
    browser.find_element(By.ID, 'userName').send_keys('JeanMich4')
    browser.find_element(By.ID, 'password').send_keys('Test01234!')
    element = browser.find_element(By.ID, "login")
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(1)
    browser.find_element(By.ID, 'login').click()
    time.sleep(1)
    assert browser.find_element(By.ID, 'userName-value').text == "JeanMich4"
    time.sleep(1)