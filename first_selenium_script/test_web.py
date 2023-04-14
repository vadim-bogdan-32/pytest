from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_web():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    url = 'https://www.google.by/'
    chrome.get(url)
    search_box = chrome.find_element(By.CLASS_NAME, 'gLFyf')
    search_box.send_keys('Python 3.10')
    search_box.submit()
    time.sleep(3)
    chrome.close()
