from selenium import webdriver
import time 
import os

LINK = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    first_name_locator = browser.find_element_by_css_selector('[placeholder$="first name"]')
    first_name_locator.send_keys('First')
    last_name_locator = browser.find_element_by_css_selector('[placeholder$="last name"]')
    last_name_locator.send_keys('Last')
    email_locator = browser.find_element_by_css_selector('[placeholder$="email"]')
    email_locator.send_keys('email@email.com')
    upload_button_locator = browser.find_element_by_css_selector('#file')
    directory_filepath = os.path.abspath(os.path.dirname(__file__))
    txt_filepath = os.path.join(directory_filepath, 'empty_file.txt')
    upload_button_locator.send_keys(txt_filepath)
    submit_button_selector = browser.find_element_by_css_selector('[type="submit"]')
    submit_button_selector.click()

finally:
    time.sleep(10)
    browser.quit()
