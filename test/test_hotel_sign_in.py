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

# BEJELETKEZÉSI FOLYAMAT ELLENŐRZÉSE

login_btn = browser.find_element(By.XPATH, '//a[text()="Bejelentkezés"]')
login_btn.click()

email_field = browser.find_element(By.ID, 'email')
email_field.send_keys('hiwasi1765@wisnick.com')

password_field = browser.find_element(By.ID, 'password')
password_field.send_keys('tesztelek2021')

belepes_btn = browser.find_element(By.NAME, 'submit')
belepes_btn.click()

time.sleep(1)

# BEJELENTKEZÉS SIKERESSÉGÉNEK ELLENŐRZÉSE A KILÉPÉS GOMB MEGLÉTÉVEL

assert browser.find_element(By.ID, 'logout-link').is_displayed
