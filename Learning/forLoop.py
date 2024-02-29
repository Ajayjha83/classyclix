import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestClassyClix():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_and_navigation(self):
        self.driver.get("https://www.classyclix.com/")
        self.driver.set_window_size(1382, 744)

        # Test Login
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        self.driver.find_element(By.ID, "username").send_keys("Ajay")
        self.driver.find_element(By.ID, "password").send_keys("Ajayjha@123")
        self.driver.find_element(By.CSS_SELECTOR, ".xoo-ml-low-back").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.NAME, "login").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()

        # Test Navigation Links
        element = self.driver.find_element(By.LINK_TEXT, "Rings")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".wpb_wrapper > .vc_row .logo img").click()
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        self.driver.find_element(By.ID, "username").send_keys("Ajay")
        self.driver.find_element(By.ID, "password").send_keys("Ajayjha@123")
        self.driver.find_element(By.CSS_SELECTOR, ".xoo-ml-low-back").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.NAME, "login").click()
        self.driver.find_element(By.LINK_TEXT, "Earrings").click()
        # Add more navigation tests as needed

    def test_search_functionality(self):
        self.driver.get("https://www.classyclix.com/")
        self.driver.set_window_size(1382, 744)

        # Test Search
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("earring")
        self.driver.find_element(By.CSS_SELECTOR, ".header-search:nth-child(1) .button-search").click()
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("rings")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        # Add more search tests as needed



class TestClassyClix():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_and_navigation(self):
        self.driver.get("https://www.classyclix.com/")
        self.driver.set_window_size(1382, 744)

        # Test Login
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        self.driver.find_element(By.ID, "username").send_keys("Ajay")
        self.driver.find_element(By.ID, "password").send_keys("Ajayjha@123")
        self.driver.find_element(By.CSS_SELECTOR, ".xoo-ml-low-back").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.NAME, "login").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()

        # Test Navigation Links
        element = self.driver.find_element(By.LINK_TEXT, "Rings")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".wpb_wrapper > .vc_row .logo img").click()
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        self.driver.find_element(By.ID, "username").send_keys("Ajay")
        self.driver.find_element(By.ID, "password").send_keys("Ajayjha@123")
        self.driver.find_element(By.CSS_SELECTOR, ".xoo-ml-low-back").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.NAME, "login").click()
        self.driver.find_element(By.LINK_TEXT, "Earrings").click()
        # Add more navigation tests as needed

    def test_search_functionality(self):
        self.driver.get("https://www.classyclix.com/")
        self.driver.set_window_size(1382, 744)

        # Test Search
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("earring")
        self.driver.find_element(By.CSS_SELECTOR, ".header-search:nth-child(1) .button-search").click()
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("rings")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        # Add more search tests as needed

    def test_homepage_slider(self):
        self.driver.get("https://www.classyclix.com/")
        self.driver.set_window_size(1382, 744)

        # Test Homepage Slider
        for _ in range(4):
            self.driver.find_element(By.CSS_SELECTOR, ".tp-rightarrow").click()
        # Add more slider tests as needed

    def test_login_navigation_links(self):
        self.driver.get("https://www.classyclix.com/")
        self.driver.set_window_size(1382, 744)

        # Test Login Navigation Links
        # Add your test steps here

    def test_homepage(self):
        self.driver.get("https://www.classyclix.com/")
        self.driver.set_window_size(1382, 744)

        # Test Homepage
        # Add your test steps here

    def test_product_search(self):
        self.driver.get("https://www.classyclix.com/")
        self.driver.set_window_size(1382, 744)

        # Test Product Search
        # Add your test steps here



