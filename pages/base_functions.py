from pages.base_page import BasePage
from pages.personal_area import PersonalArea
from locators.locators import Locators
from data import StellarBurgersData
import allure


class BaseFunctions(BasePage):

    @allure.step('Нажимаем кнопку Личный кабинет')
    def transit_to_personal_area(self):
        self.click_element(Locators.PERSONAL_AREA_BUTTON)

    @allure.step('Нажимаем кнопку Конструктор')
    def transit_to_constructor(self):
        self.click_element(Locators.BUTTON_CONSTRUCTOR)


    @allure.step('Нажимаем кнопку Лента заказов')
    def transit_to_order_list(self):
        self.click_element(Locators.BUTTON_ORDER_LIST)


    @allure.step('Клик на ингридиент')
    def click_ingridient(self):
        self.click_element(Locators.INGRIDIENT_BULKI_NAME)

    @allure.step('Появилось модальное окно')
    def appear_modal(self):
        return self.wait_and_find(Locators.INGRIDIENT_MODAL_WINDOW)


    @allure.step('Закрываем модальное окно ингридиента нажатием крестика')
    def close_ingridient(self):
        self.click_element(Locators.INGRIDIENT_BUTTON_CLOSE)
        self.wait_abcent(Locators.INGRIDIENT_BUTTON_CLOSE)

    @allure.step('Проверяем закрытие модального окна и появление ингридиентов')
    def check_closing_modal(self):
        if self.wait_and_find(Locators.INGRIDIENT_BULKI_NAME):
            return True



    @allure.step('Авторизация и оформление заказа')
    def create_order(self):
        PersonalArea.go_to_acc(self)
        PersonalArea.auth(self)
        self.wait_clickable(Locators.BUTTON_CREATE_ORDER)
        self.click_element(Locators.BUTTON_CREATE_ORDER)
        self.wait_and_find(Locators.CREATE_ORDER)


    @allure.step('Возвращаем текст заказа')
    def return_text_order(self):
       return self.return_text_element(Locators.CREATE_ORDER)


    @allure.step('Добавляем ингридиент в заказ')
    def add_ingridient(self):
        self.drag_drop(Locators.INGRIDIENT_BULKI_NAME, Locators.INGRIDIENT_ADD, Locators.INGRIDIENT_NAME_IN_CHECK)


    @allure.step('Возвращаем количество ингридиентов')
    def return_number_of_ingridient(self):
        return self.return_text_element(Locators.INGRIDIENT_COUNTER)



