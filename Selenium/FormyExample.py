# import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# chrome web browser
driver = webdriver.Chrome()
time.sleep(2)

# maximum size of the window
driver.maximize_window()
time.sleep(2)

# navigate to website
url = "https://formy-project.herokuapp.com/switch-window"
driver.get(url)

alertbtn = driver.find_element(By.ID,"alert-button")
alertbtn.click()
time.sleep(3)

alert = driver.switch_to.alert
alert.accept()
# alert.dismiss()
# alert.send_keys("sdgvjdv") --> for input alert box
time.sleep(3)

driver.quit()