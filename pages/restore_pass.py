from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.locators import Locators
from data import StellarBurgersData
import allure


class RestorePassword(BasePage):
    @allure.step('Нажимаем ссылку Восстановить пароль')
    def transit_restore_pass(self):
        self.click_element(Locators.AUTH_BUTTON_GO_TO_ACCOUNT)
        self.click_element(Locators.RESTORE_PASSWORD_LINK)


    @allure.step('Нажимаем ссылку Восстановить пароль и вводим email')
    def enter_pass(self):
        self.transit_restore_pass()
        self.wait_and_find(Locators.RESTORE_PASSWORD_INPUT_EMAIL).send_keys(StellarBurgersData.AUTH_EMAIL)
        self.click_element(Locators.RESTORE_PASSWORD_BUTTON_RESTORE)

    @allure.step('Возвращает хедер "Восстановление пароля"')
    def return_header(self):
        return self.wait_and_find(Locators.RESTORE_PASSWORD_HEDER)


    @allure.step('Нажимаем ссылку Восстановить пароль, вводим email, нажимаем Показать пароль')
    def click_eye(self):
        self.enter_pass()
        self.click_element(Locators.RESTORE_PASSWORD_ICON_SHOW_PASSWORD)

    @allure.step('Возвращает активное поле')
    def return_active_input(self):
        return self.wait_and_find(Locators.RESTORE_PASSWORD_INPUT_ACTIVE)