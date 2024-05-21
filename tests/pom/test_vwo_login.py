import time

import allure
import pytest
from selenium import webdriver
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import DashBoardPage


class TestVwoLogin:

    @allure.title("vwo_log_in_negative")
    @allure.description("this is for Vwo login nagative test case with is display if any one enter wrong uid or pwd")
    @pytest.mark.usefixtures("setup")
    def test_vwo_log_in_negative(self, setup):
        driver = setup
        driver.get(self.vwo_url)
        loginpage = LoginPage(driver)
        loginpage.login_to_vwo(uid="python@one.com", pwd="123")
        time.sleep(5)
        error_message = loginpage.error_msg_login()
        assert error_message == "Your email, password, IP address or location did not match"


    @allure.title("vwo_log_in_positive")
    @allure.description("this for Vwo login positive test case")
    @pytest.mark.usefixtures("setup")
    def test_vwo_log_in_positive(self, setup):
        driver = setup
        driver.get(self.vwo_url)
        loginpage = LoginPage(driver)
        loginpage.login_to_vwo(uid=self.username, pwd=self.password)
        time.sleep(10)
        dashboardpage = DashBoardPage(driver)
        assert "Dashboard" in driver.title
        assert "python" in dashboardpage.dash_board_text()

