import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()  # Use appropriate driver here, like Firefox(), Edge(), etc.

# Example: Open a webpage
driver.get("https://www.classyclix.com/")

userName = "Ajay"
password = "Ajayjha@123"
# Example: Find an element and interact with it
driver.find_element(By.LINK_TEXT,"Sign In").click()
driver.find_element(By.XPATH,"//*[@id='customer_login']/div[1]/form[2]/button[2]").click()
driver.find_element(By.ID,"username").send_keys(userName)
driver.find_element(By.ID,'password').send_keys(password)
driver.find_element(By.NAME,'login').click()






driver.quit()