from locators.locators import Locators
from data import StellarBurgersData
import allure
from pages.base_page import BasePage


class PersonalArea(BasePage):

    @allure.step('Нажимаем кнопку Войти в аккаунт')
    def go_to_acc(self):
        self.click_element(Locators.AUTH_BUTTON_GO_TO_ACCOUNT)


    @allure.step('Нажимаем кнопку ЛК')
    def transit_personal_area(self):
        self.click_element(Locators.PERSONAL_AREA_BUTTON)


    @allure.step('Вводит email и пароль, нажимаем кнопку Войти')
    def auth(self):
        self.wait_and_find(Locators.AUTH_EMAIL).send_keys(StellarBurgersData.AUTH_EMAIL)
        self.wait_and_find(Locators.AUTH_PASSWORD).send_keys(StellarBurgersData.AUTH_PASSWORD)
        self.click_element(Locators.AUTH_BUTTON_AUTH)
        self.wait_clickable(Locators.BUTTON_CREATE_ORDER)


    @allure.step('Шаг: Авторизация и переход в ЛК')
    def steps_auth(self):
        self.go_to_acc()
        self.auth()




    @allure.step('Нажимаем Историю заказов в ЛК ')
    def transit_order_history(self):
        self.steps_auth()
        self.transit_personal_area()
        self.click_element(Locators.PERSONAL_AREA_ORDERS_HISTORY)



    @allure.step('Нажимаем Выйти в ЛК')
    def logout(self):
        self.steps_auth()
        self.transit_personal_area()
        self.click_element(Locators.PERSONAL_AREA_BUTTON_LOGOUT)
        self.wait_clickable(Locators.AUTH_BUTTON_AUTH)

