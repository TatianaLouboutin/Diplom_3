from locators.locators import Locators
from pages.orders_list import OrderList
import allure


class TestOrdersList:

    @allure.title("Проверка появления модального окна при клике на заказ")
    @allure.description("Открывается всплывающее окно с деталями при клике на заказ")
    def test_click_order(self, driver):
        orders_list = OrderList(driver)
        orders_list.click_order()
        assert orders_list.return_text_modal() == 'Cостав'


    @allure.title("Проверка: заказы пользователя из Истории заказов есть в Ленте заказов")
    @allure.description("Заказы пользователя из Истории заказов отображаются в Ленте заказов")
    def test_numbers_orders_are_the_same(self, driver):
        orders_list = OrderList(driver)
        assert orders_list.numbers_orders_are_the_same() == True

    @allure.title("Проверка увеличения счётчика заказов за всё время")
    @allure.description("Счетчик заказов за всё время увеличивается после создания заказа")
    def test_find_all_orders(self, driver):
        orders_list = OrderList(driver)
        number_before = orders_list.return_all_orders()
        orders_list.creation_order()
        number_after = orders_list.return_all_orders()
        assert int(number_after) - int(number_before) == 1

    @allure.title("Проверка увеличения счётчика заказов за день")
    @allure.description("Счетчик заказов за день увеличивается после создания заказа")
    def test_find_today_orders(self, driver):
        orders_list = OrderList(driver)
        number_before = orders_list.return_today_orders()
        orders_list.creation_order()
        number_after = orders_list.return_today_orders()
        assert int(number_after) - int(number_before) == 1

    @allure.title("Проверка появления номера заказа в разделе 'В работе'")
    @allure.description("В разделе 'В работе' появляется номер заказа")
    def test_order_in_work(self, driver):
        orders_list = OrderList(driver)
        orders_list.creation_order()
        assert orders_list.number_in_work_equils_number_new_order() == True
