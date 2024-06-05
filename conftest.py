import pytest
from selenium import webdriver
import settings

#@pytest.fixture(scope='function')
#def driver():
#    driver = webdriver.Firefox()
#    driver = webdriver.Chrome()
#    driver.get(settings.URL)
#    driver.maximize_window()
#    yield driver
#    driver.quit()



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
