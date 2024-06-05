import settings
from locators.locators import Locators
from pages.base_functions import BaseFunctions
import allure


class OrderList(BaseFunctions):
    @allure.step('Кликаем на заказ')
    def click_order(self, driver):
        self.transit_to_order_list(driver)
        self.click_element(Locators.LIST_ORDER_FIRST_ORDER)
        self.wait_and_find(Locators.LIST_ORDER_MODAL_WINDOW_TEXT)


    @allure.step('Создание заказа')
    def creation_order(self, driver):
        self.open_page(settings.URL)
        self.go_to_acc(driver)
        self.auth(driver)
        self.open_page(settings.URL)
        self.add_ingridient(driver)
        self.click_element(Locators.BUTTON_CREATE_ORDER)
        self.click_element(Locators.INGRIDIENT_BUTTON_CLOSE)


    @allure.step('Ищем последний заказ пользователя в Истории заказов, он равен первому заказу в Ленте заказов')
    def order_from_order_history_in_orders_list(self, driver):
        self.creation_order(driver)
        self.transit_personal_area(driver)
        self.click_element(Locators.PERSONAL_AREA_ORDERS_HISTORY)
        self.wait_and_find(Locators.ORDER_HISTORY_LAST_ORDER)
        number_new_order = self.return_text_element(Locators.ORDER_HISTORY_LAST_ORDER)
        self.transit_to_order_list(driver)
        number_in_orders_list = self.return_text_element(Locators.LIST_ORDER_FIRST_ORDER_NUMBER)
        if number_new_order == number_in_orders_list:
            return True


    @allure.step('Находим номера заказов до и после заказа')
    def find_number_orders(self, driver, locator):
        self.transit_to_order_list(driver)
        self.wait_and_find(locator)
        return self.return_text_element(locator)






