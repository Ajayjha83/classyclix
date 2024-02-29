import explicit
from selenium import webdriver
import pytest
from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://classyclick.com/"
    username = "Ajay"
    password = "Ajayjha@123"
    explicit_wait = 10

    def test_homePage_title(self):
        driver = webdriver.Chrome()  # Create a new WebDriver instance
        driver.get(self.baseURL)  # Navigate to the base URL
        actual_title = driver.title  # Get the title of the page
        driver.close()  # Close the browser window
        assert actual_title == "ClassyClix - Artificial Jewellery Online Shopping India"  # Check if the title matches
'''
    def test_login(self):
        driver = webdriver.Chrome()  # Create a new WebDriver instance
        driver.get(self.baseURL)  # Navigate to the base URL

        # Create an instance of the LoginPage class
        lp = LoginPage(driver)

        # Click the sign-in button
        lp.click_signin_button()

        # Click the customer login button
        lp.click_customer_login_button()

        # Set the username and password fields
        lp.set_username_field(self.username)
        lp.set_password_field(self.password)

        # Click the login button
        lp.click_login_button()

        driver.quit()  # Quit the WebDriver instance
'''