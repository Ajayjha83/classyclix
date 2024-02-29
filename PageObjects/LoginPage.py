class Loginpage:


    buton_signIn_linktext = "Sign In"
    button_customerLogin_xpath = "//*[@id='customer_login']/div[1]/form[2]/button[2]"
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_name = "login"

    # define constructor
    def __init__(self, driver):
        self.driver = driver

    def click_signin_button(self, signin):
        self.driver.find_element(By.LINK_TEXT, self.button_signIn_linktext).click()

    def click_customer_login_button(self):
        self.driver.find_element(By.XPATH, self.button_customerLogin_xpath).click()

    def set_username_field(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys("Ajay")

    def set_password_field(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys("Ajayjha@123")

    def click_login_button(self, login):
        self.driver.find_element(By.NAME, self.button_login_name).click()
