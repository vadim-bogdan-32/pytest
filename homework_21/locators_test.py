from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_form_1(browser):
    chrome = browser
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    chrome.get('https://thedemosite.co.uk/savedata.php')
    username_box = chrome.find_element(By.NAME, 'username')
    username_box.send_keys('Vadim')
    time.sleep(2)
    password_box = chrome.find_element(By.NAME, 'password')
    password_box.send_keys('111222333')
    time.sleep(2)
    save_button = chrome.find_element(By.NAME, 'FormsButton2')
    save_button.click()
    time.sleep(2)


def test_form_2(browser):
    chrome = browser
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    chrome.get('https://demoqa.com/text-box')
    username_box = chrome.find_element(By.ID, 'userName')
    username_box.send_keys('Bogdan Vadim Andreevich')
    time.sleep(2)
    email_box = chrome.find_element(By.ID, 'userEmail')
    email_box.send_keys('bogdanvadim@gmail.com')
    time.sleep(2)
    address_box = chrome.find_element(By.ID, 'currentAddress')
    address_box.send_keys('Pushkina street, h. 32')
    time.sleep(2)
    permanent_address_box = chrome.find_element(By.ID, 'permanentAddress')
    permanent_address_box.send_keys('Kolotushkina street, h. 55')
    time.sleep(2)
    submit_button = chrome.find_element(By.ID, 'submit')
    submit_button.click()
    time.sleep(2)

