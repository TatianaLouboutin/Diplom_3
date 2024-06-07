import settings
from locators.locators import Locators
from pages.base_page import BasePage
from pages.base_functions import BaseFunctions
from pages.personal_area import PersonalArea
import allure


class OrderList(BasePage):
    @allure.step('Кликаем на заказ')
    def click_order(self):
        self.click_element(Locators.BUTTON_ORDER_LIST)
        self.click_element(Locators.LIST_ORDER_FIRST_ORDER)
        self.wait_and_find(Locators.LIST_ORDER_MODAL_WINDOW_TEXT)

    @allure.step('Возвращаем текст модального окна')
    def return_text_modal(self):
        return self.return_text_element(Locators.LIST_ORDER_MODAL_WINDOW_TEXT)

    @allure.step('Создание заказа')
    def creation_order(self):
        self.open_page(settings.URL)
        PersonalArea.go_to_acc(self)
        PersonalArea.auth(self)
        self.open_page(settings.URL)
        BaseFunctions.add_ingridient(self)
        self.click_element(Locators.BUTTON_CREATE_ORDER)
        self.click_element(Locators.INGRIDIENT_BUTTON_CLOSE)


    @allure.step('Ищем последний заказ пользователя в Истории заказов, он равен первому заказу в Ленте заказов')
    def numbers_orders_are_the_same(self):
        self.creation_order()
        PersonalArea.transit_personal_area(self)
        self.click_element(Locators.PERSONAL_AREA_ORDERS_HISTORY)
        self.wait_and_find(Locators.ORDER_HISTORY_LAST_ORDER)
        number_new_order = self.return_text_element(Locators.ORDER_HISTORY_LAST_ORDER)
        BaseFunctions.transit_to_order_list(self)
        number_in_orders_list = self.return_text_element(Locators.LIST_ORDER_FIRST_ORDER_NUMBER)
        if number_new_order == number_in_orders_list:
            return True


    @allure.step('Находим номера заказов до и после заказа')
    def find_number_orders(self, locator):
        self.click_element(Locators.BUTTON_ORDER_LIST)
        self.wait_and_find(locator)
        return self.return_text_element(locator)

    @allure.step('Находим количество заказов за все время')
    def return_all_orders(self):
        return self.find_number_orders(Locators.LIST_ORDER_ALL_ORDERS)

    @allure.step('Находим количество заказов за день')
    def return_today_orders(self):
        return self.find_number_orders(Locators.LIST_ORDER_TODAY_ORDERS)

    @allure.step('Номер нового заказа появляется в разделе "В работе"')
    def number_in_work_equils_number_new_order(self):
        BaseFunctions.transit_to_order_list(self)
        number = self.find_number_orders(Locators.LIST_ORDER_FIRST_ORDER_NUMBER)
        number = number[1:7]
        number_in_work = self.find_number_orders(Locators.LIST_ORDER_ORDER_IN_WORK)
        number_in_work.replace('"', '')
        if number == number_in_work:
            return True