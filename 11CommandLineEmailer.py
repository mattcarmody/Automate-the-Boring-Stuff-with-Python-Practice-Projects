#! /usr/bin/python3
# chap11PracProjCommandLineEmailer.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

dest = sys.argv[1]
message = sys.argv[2]
username = 'placeholder'
jewel = 'placeholder'
subject = 'Command Line Emailer'
url = 'https://mail.yahoo.com'

browser = webdriver.Firefox()
browser.get(url)

try:
    usernameField = browser.find_element_by_id('login-username')
    usernameField.send_keys(username)
    usernameField.submit()
except:
    print("Problem with username...")
time.sleep(10)
try:
    passwordField = browser.find_element_by_id('login-passwd')
    passwordField.send_keys(jewel)
    loginBtn = browser.find_element_by_id('login-signin')
    loginBtn.click()
except:
    print("Problem with password...")
time.sleep(10)
try:
    composeBtn = browser.find_element_by_class_name('btn-compose')
    composeBtn.click()
    time.sleep(10)
    toField = browser.find_element_by_id('to-field')
    toField.send_keys(dest)
    subjectField = browser.find_element_by_id('subject-field')
    subjectField.send_keys(subject)
    bodyField = browser.find_element_by_id('rtetext')
    bodyField.send_keys(message)
    bodyField.send_keys(Keys.CONTROL + Keys.ENTER)
except:
    print("Problem sending email...")
time.sleep(5)    
browser.quit()
