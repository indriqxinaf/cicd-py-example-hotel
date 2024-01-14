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

# HOTELEK LISTÁJÁNAK LEKÉRÉSE

hotelek_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
hotelek_btn.click()
time.sleep(1)

# MINDEN CHECKBOX BEJELÖLÉSE

checkboxes = browser.find_elements(By.XPATH, '//input[@type="checkbox"]')

for checkbox in checkboxes:
    checkbox.click()

assert checkbox.is_selected() in range(len(checkboxes))

# 'Szoba szolgáltatás szűrések törlése' GOMB MŰKÖDÉSÉNEK ELLENŐRZÉSE

deselect_btn = browser.find_element(By.ID, 'redstar')
deselect_btn.click()

assert not checkbox.is_selected()
