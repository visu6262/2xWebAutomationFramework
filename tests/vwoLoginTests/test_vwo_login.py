import time

import allure
import pytest
from selenium import webdriver
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import DashBoardPage


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    return driver


@allure.title("vwo_log_in_negative")
@allure.description("this is for Vwo login nagative test case with is display if any one enter wrong uid or pwd")
def test_vwo_log_in_negative(setup):
    driver = setup
    loginpage = LoginPage(driver)
    loginpage.login_to_vwo(uid="python@one.com", pwd="123")
    time.sleep(5)
    error_message = loginpage.error_msg_login()
    assert error_message == "Your email, password, IP address or location did not match"
    # driver.close()


@allure.title("vwo_log_in_positive")
@allure.description("this for Vwo login positive test case")
def test_vwo_log_in_positive(setup):
    driver = setup
    loginpage = LoginPage(driver)
    loginpage.login_to_vwo(uid="python@one.com", pwd="Admin@123")
    time.sleep(10)
    dashboardpage = DashBoardPage(driver)
    assert "Dashboard" in driver.title
    assert "python" in dashboardpage.dash_board_text()
    # driver.close()
