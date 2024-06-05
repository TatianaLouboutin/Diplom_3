from pages.personal_area import PersonalArea
from locators.locators import Locators
import allure


class BaseFunctions(PersonalArea):

    @allure.step('Нажимаем кнопку Личный кабинет')
    def transit_to_personal_area(self, driver):
        self.click_element(Locators.PERSONAL_AREA_BUTTON)

    @allure.step('Нажимаем кнопку Конструктор')
    def transit_to_constructor(self, driver):
        self.click_element(Locators.BUTTON_CONSTRUCTOR)


    @allure.step('Нажимаем кнопку Лента заказов')
    def transit_to_order_list(self, driver):
        self.click_element(Locators.BUTTON_ORDER_LIST)


    @allure.step('Клик на ингридиент')
    def click_ingridient(self, driver):
        self.click_element(Locators.INGRIDIENT_BULKI_NAME)


    @allure.step('Закрываем модальное окно ингридиента нажатием крестика')
    def close_ingridient(self, driver):
        self.click_element(Locators.INGRIDIENT_BULKI_NAME)
        self.click_element(Locators.INGRIDIENT_BUTTON_CLOSE)
        self.wait_abcent(Locators.INGRIDIENT_BUTTON_CLOSE)

    @allure.step('Авторизация и оформление заказа')
    def create_order(self, driver):
        self.go_to_acc(driver)
        self.auth(driver)
        self.click_element(Locators.BUTTON_CREATE_ORDER)
        self.wait_and_find(Locators.CREATE_ORDER)


    @allure.step('Добавляем ингридиент в заказ')
    def add_ingridient(self, driver):
        self.drag_drop(Locators.INGRIDIENT_BULKI_NAME, Locators.INGRIDIENT_ADD, Locators.INGRIDIENT_NAME_IN_CHECK)


