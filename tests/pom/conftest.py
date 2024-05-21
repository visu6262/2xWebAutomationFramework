import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    vwo_url = os.getenv("vwo_url")
    username = os.getenv("user_name")
    password = os.getenv("pass_word")

    request.cls.driver=driver
    request.cls.vwo_url=vwo_url
    request.cls.username=username
    request.cls.password=password


    yield driver
    driver.quit()

