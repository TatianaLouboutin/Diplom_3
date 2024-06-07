import settings
from locators.locators import Locators
import allure
from pages.restore_pass import RestorePassword



class TestRestorePassword:
    @allure.title("Переход по ссылке Восстановить пароль")
    @allure.description("Нажататие ссылки Восстановить пароль ведет на страницу ввода почты")
    def test_transit_restore_pass(self, driver):
        restore_pass = RestorePassword(driver)
        restore_pass.transit_restore_pass()
        assert driver.current_url == settings.URL + settings.RESTORE_PASSWORD


    @allure.title("Проверка перехода на страницу восстановления пароля")
    @allure.description("Ввод почты и нажатие кнопки Восстановить ведет на страницу восстановления пароля")
    def test_enter_pass(self, driver):
        restore_pass = RestorePassword(driver)
        restore_pass.enter_pass()
        header = restore_pass.return_header()
        assert header.is_displayed()


    @allure.title("Проверка подсветки поля Показать пароль")
    @allure.description("Нажатие кнопки Показать пароль делает поле активным")
    def test_click_eye(self, driver):
        restore_pass = RestorePassword(driver)
        restore_pass.click_eye()
        active_input = restore_pass.return_active_input()
        assert active_input.is_displayed()
