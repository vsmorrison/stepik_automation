from selenium import webdriver
import time
import math

LINK = 'http://suninjuly.github.io/redirect_accept.html'

def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    submit_button_selector = browser.find_element_by_css_selector('[type="submit"]')
    submit_button_selector.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
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
