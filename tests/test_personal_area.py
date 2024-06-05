from pages.personal_area import PersonalArea
import settings
import allure

class TestPersonalArea:
    @allure.title("Проверка перехода по клику на ЛК")
    @allure.description("Переход по клику на ЛК")
    def test_transit_personal_area(self, driver):
        personal_area = PersonalArea(driver)
        personal_area.transit_personal_area(driver)
        assert driver.current_url == settings.URL + settings.LOGIN


    @allure.title("Проверка перехода по клику История заказов в ЛК")
    @allure.description("Переход по клику История заказов в ЛК")
    def test_transit_order_history(self, driver):
        personal_area = PersonalArea(driver)
        personal_area.transit_order_history(driver)
        assert driver.current_url == settings.URL + settings.ORDER_HISTORY


    @allure.title("Проверка разлогина в ЛК")
    @allure.description("Переход по клику Выход в ЛК")
    def test_logout(self, driver):
        personal_area = PersonalArea(driver)
        personal_area.logout(driver)
        assert driver.current_url == settings.URL + settings.LOGIN


