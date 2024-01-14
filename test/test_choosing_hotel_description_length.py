import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = 'http://hotel-v3.progmasters.hu/'
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

browser.get(URL)

hotelek_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
hotelek_btn.click()
time.sleep(1)

# HOTEL KIVÁLASZTÁSA (Rainbow Six Siege - szálloda)

rainbow = browser.find_element(By.XPATH, '//h4[text()="Rainbow Six Siege - szálloda"]')
rainbow.click()
time.sleep(1)
rainbow_loaded = browser.find_element(By.XPATH, '//h3[@class="card-title"]')
assert rainbow_loaded.text == 'Rainbow Six Siege - szálloda'

# LEÍRÁS HOSSZÁNAK ELLENŐRZÉSE

leiras = browser.find_elements(By.XPATH, '//p[@class="card-text"]')[1]

assert len(leiras.text) >= 500
