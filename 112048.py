#! python3
# chap11PracProj2048.py - Plays 2048 in a simple way.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
time.sleep(5)

elem = browser.find_element_by_class_name('game-container')
over = browser.find_element_by_class_name('retry-button')

while over.is_displayed() == False:
    elem.send_keys(Keys.DOWN)
    time.sleep(1)
    elem.send_keys(Keys.LEFT)
    time.sleep(1)
    elem.send_keys(Keys.UP)
    time.sleep(1)
    elem.send_keys(Keys.RIGHT)
    time.sleep(1)

print('You had a good run.')
