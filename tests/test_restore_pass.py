import settings
from locators.locators import Locators
import allure
from pages.restore_pass import RestorePassword



class TestRestorePassword:
    @allure.title("Переход по ссылке Восстановить пароль")
    @allure.description("Нажататие ссылки Восстановить пароль ведет на страницу ввода почты")
    def test_transit_restore_pass(self, driver):
        restore_pass = RestorePassword(driver)
        restore_pass.transit_restore_pass(driver)
        assert driver.current_url == settings.URL + settings.RESTORE_PASSWORD


    @allure.title("Проверка перехода на страницу восстановления пароля")
    @allure.description("Ввод почты и нажатие кнопки Восстановить ведет на страницу восстановления пароля")
    def test_enter_pass(self, driver):
        restore_pass = RestorePassword(driver)
        restore_pass.enter_pass(driver)
        assert driver.find_element(*Locators.RESTORE_PASSWORD_HEDER).is_displayed()


    @allure.title("Проверка подсветки поля Показать пароль")
    @allure.description("Нажатие кнопки Показать пароль делает поле активным")
    def test_click_eye(self, driver):
        restore_pass = RestorePassword(driver)
        restore_pass.click_eye(driver)
        assert driver.find_element(*Locators.RESTORE_PASSWORD_INPUT_ACTIVE).is_displayed()
