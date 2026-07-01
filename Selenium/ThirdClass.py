# Wait / Syncronization Practice

# import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# chrome web browser
driver = webdriver.Chrome()
time.sleep(2)

# maximum size of the window
driver.maximize_window()
time.sleep(2)

# navigate to website
url = "https://www.saucedemo.com/"

driver.get(url)

# implicit wait - # driver.implicitly_wait(10)

# using locator ID
# uname = driver.find_element(By.ID,"user-name")

# using locatorrelative path
uname = driver.find_element(By.XPATH,"//*[@id='user-name']")
uname.send_keys("standard_user")

# password = driver.find_element(By.ID,"password")

password = driver.find_element(By.XPATH,"//*[@id='password']")
password.send_keys("secret_sauce")

# loginbtn = driver.find_element(By.ID,"login-button")

# loginbtn = driver.find_element(By.XPATH,"//*[@id='login-button']")
# loginbtn.click()

# explicit wait--------------------
wait = WebDriverWait(driver, 10)
login_button = wait.until(ec.element_to_be_clickable((By.ID,"login-button")))
login_button.click()
time.sleep(2)

# scroll using pixel
driver.execute_script("window.scrollBy(0,300);")
time.sleep(3)

# scroll to top
driver.execute_script("window.scrollTo(0,300);")
time.sleep(3)

# scroll to bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# assert "inventory" in driver.current_url, "Login Unsuccessful"

if "inventory" in driver.current_url:
    print ("Login successful")

else:
    print ("Login Unsuccessful")

# driver close
driver.quit()