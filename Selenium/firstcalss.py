# import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(2)

driver.maximize_window()
time.sleep(2)

# navigate to website
url = "https://www.saucedemo.com/"

driver.get(url)

uname = driver.find_element(By.ID,"user-name")
uname.send_keys("standard_user")

password = driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")

loginbtn = driver.find_element(By.ID,"login-button")
loginbtn.click()

# execute delay
time.sleep(3)

# driver close
driver.quit()