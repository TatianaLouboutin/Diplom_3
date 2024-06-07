import pytest
from selenium import webdriver
import settings
import allure
from pages.base_functions import BaseFunctions

@allure.step("Создание кроссбраузерного драйвера для Chrome и Firefox")
@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    driver = None
    if request.param == 'chrome':
          driver = webdriver.Chrome()
    elif request.param == 'firefox':
          driver = webdriver.Firefox()
    driver.get(settings.URL)

    yield driver
    driver.quit()


