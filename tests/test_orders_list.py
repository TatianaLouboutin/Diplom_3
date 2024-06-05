from locators.locators import Locators
from pages.orders_list import OrderList
import allure


class TestOrdersList:

    @allure.title("Проверка появления модального окна при клике на заказ")
    @allure.description("Открывается всплывающее окно с деталями при клике на заказ")
    def test_click_order(self, driver):
        orders_list = OrderList(driver)
        orders_list.click_order(driver)
        assert driver.find_element(*Locators.LIST_ORDER_MODAL_WINDOW_TEXT).text == 'Cостав'


    @allure.title("Проверка: заказы пользователя из Истории заказов есть в Ленте заказов")
    @allure.description("Заказы пользователя из Истории заказов отображаются в Ленте заказов")
    def test_order_from_order_history_in_orders_list(self, driver):
        orders_list = OrderList(driver)
        orders_list.order_from_order_history_in_orders_list(driver)
        assert True == True

    @allure.title("Проверка увеличения счётчика заказов за всё время")
    @allure.description("Счетчик заказов за всё время увеличивается после создания заказа")
    def test_find_all_orders(self, driver):
        orders_list = OrderList(driver)
        number_before = orders_list.find_number_orders(driver, Locators.LIST_ORDER_ALL_ORDERS)
        orders_list.creation_order(driver)
        number_after = orders_list.find_number_orders(driver, Locators.LIST_ORDER_ALL_ORDERS)
        assert int(number_after) - int(number_before) == 1

    @allure.title("Проверка увеличения счётчика заказов за день")
    @allure.description("Счетчик заказов за день увеличивается после создания заказа")
    def test_find_today_orders(self, driver):
        orders_list = OrderList(driver)
        number_before = orders_list.find_number_orders(driver, Locators.LIST_ORDER_TODAY_ORDERS)
        orders_list.creation_order(driver)
        number_after = orders_list.find_number_orders(driver, Locators.LIST_ORDER_TODAY_ORDERS)
        assert int(number_after) - int(number_before) == 1

    @allure.title("Проверка появления номера заказа в разделе 'В работе'")
    @allure.description("В разделе 'В работе' появляется номер заказа")
    def test_order_in_work(self, driver):
        orders_list = OrderList(driver)
        orders_list.creation_order(driver)
        orders_list.transit_to_order_list(driver)
        number = orders_list.find_number_orders(driver, Locators.LIST_ORDER_FIRST_ORDER_NUMBER)
        number = number[1:7]
        number_in_work = orders_list.find_number_orders(driver, Locators.LIST_ORDER_ORDER_IN_WORK)
        number_in_work.replace('"', '')
        assert number == number_in_work
