from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем видимости элемента, потом его находим')
    def wait_and_find(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ждем кликабельности элемента')
    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Ждем отсутсвия элемента')
    def wait_abcent(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(locator))



    @allure.step('Открываем страницу')
    def open_page(self, url):
        self.driver.get(url)


    @allure.step('Перетаскиваем ингридиент в заказ')
    def drag_drop(self, locator1, locator2,  locator3):
        source = self.wait_and_find(locator1)
        target = self.wait_and_find(locator2)
        drag_and_drop(self.driver, source, target)
        self.wait_and_find(locator3)


    @allure.step('Возвращаем текст найденного элемента')
    def return_text_element(self, locator):
        self.wait_and_find(locator)
        text = self.driver.find_element(*locator).text
        return text



    @allure.step('Нажимаем элемент')
    def click_element(self, locator):
        element = self.wait_and_find(locator)
        self.driver.execute_script("arguments[0].click();", element)



