from selenium.webdriver.common.by import By


class DashBoardPage:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators

    user_log_in = (By.XPATH, "//span[@data-qa='lufexuloga']")

    # Page Actions

    def get_user_log_in(self):
        return self.driver.find_element(*DashBoardPage.user_log_in)

    # Page Action - Main Action

    def dash_board_text(self):
        return self.get_user_log_in().text
