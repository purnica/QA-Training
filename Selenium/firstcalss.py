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

# using locator ID
# uname = driver.find_element(By.ID,"user-name")

# using locatorrelative path
uname = driver.find_element(By.XPATH,"//*[@id='user-name']")
uname.send_keys("standard_user")

# password = driver.find_element(By.ID,"password")

password = driver.find_element(By.XPATH,"//*[@id='password']")
password.send_keys("secret_sauce")

# loginbtn = driver.find_element(By.ID,"login-button")

loginbtn = driver.find_element(By.XPATH,"//*[@id='login-button']")

loginbtn.click()

# execute delay
time.sleep(3)

# assert "inventory" in driver.current_url, "Login Unsuccessful"

if "inventory" in driver.current_url:
    print ("Login successful")

else:
    print ("Login Unsuccessful")

# driver close
driver.quit()