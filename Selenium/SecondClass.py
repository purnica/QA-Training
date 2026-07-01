# Locators Practice

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(2)

driver.maximize_window()
time.sleep(2)

url = "https://sheguidesme.com/"

driver.get(url)

name = driver.find_element(By.NAME,"full_name")
name.send_keys("")


# purnika@yopmail.com

time.sleep(3)
driver.quit()
