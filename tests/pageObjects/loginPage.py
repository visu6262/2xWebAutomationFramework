# Login Page Class

# Respon ->
# get username and send keys - email
# # get password and send keys - email
# # click the submit button and navigate to dashboard Page
# Invalid -> error message
# Forgot password


# Page Class

# Page Locators
# Page Actions
# Page Action - Main Action
# WebDriver Init
# Custom Functions
# No assertions(in Page Object Class)


# driver= webdriver.Chrome()
# email_address = driver.find_element(By.ID,"login-username") # element"Loctors"
# email_address.send_keys("abc@add.com") # element"Action"

from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    email_address = (By.ID, "login-username")
    pass_word = (By.NAME, "password")
    sign_in = (By.ID, "js-login-btn")
    error_msg = (By.XPATH, "//div[@id='js-notification-box-msg']")

    # Page Actions
    def get_email_addres(self):  # sendkeys
        return self.driver.find_element(*LoginPage.email_address)

    def get_password(self):  # sendkeys
        return self.driver.find_element(*LoginPage.pass_word)

    def get_sign_in(self):  # click
        return self.driver.find_element(*LoginPage.sign_in)

    def get_error_msg(self):  # text
        return self.driver.find_element(*LoginPage.error_msg)

    # Page Action - Main Action

    def login_to_vwo(self, uid, pwd):
        self.get_email_addres().send_keys(uid)
        self.get_password().send_keys(pwd)
        self.get_sign_in().click()

    def error_msg_login(self):
        return self.get_error_msg().text
