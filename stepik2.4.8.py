from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

LINK='http://suninjuly.github.io/explicit_wait2.html'

def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    book_button = browser.find_element_by_css_selector('#book')
    book_button.click()
    locator_for_number = browser.find_element_by_css_selector('#input_value')
    number_from_locator = locator_for_number.text
    number_for_text_field = calc(number_from_locator)
    text_field = browser.find_element_by_css_selector('#answer')
    text_field.send_keys(number_for_text_field)
    submit_button = browser.find_element_by_css_selector('[type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
