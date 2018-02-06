from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

dest = sys.argv[1]
message = sys.argv[2]
USERNAME = '{USERNAME_HERE'
PASSWORD = '{PASSWORD_HERE}'
SUBJECT = 'Command Line Emailer'
URL = 'https://mail.yahoo.com'

browser = webdriver.Firefox()
browser.get(URL)

try:
    username_field = browser.find_element_by_id('login-username')
    username_field.send_keys(USERNAME)
    username_field.submit()
except:
    print("Problem with username...")
time.sleep(5)
try:
    password_field = browser.find_element_by_id('login-passwd')
    password_field.send_keys(PASSWORD)
    browser.find_element_by_id('login-signin').click()
except:
    print("Problem with password...")
time.sleep(5)
try:
    browser.find_element_by_class_name('btn-compose').click()
    dest_field = browser.find_element_by_id('to-field')
    dest_field.send_keys(dest)
    subject_field = browser.find_element_by_id('subject-field')
    subject_field.send_keys(SUBJECT)
    body_field = browser.find_element_by_id('rtetext')
    body_field.send_keys(message)
    body_field.send_keys(Keys.CONTROL + Keys.ENTER)
except:
    print("Problem sending email...") 
    time.sleep(5)   
browser.quit()
