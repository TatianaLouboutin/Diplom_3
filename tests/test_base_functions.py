from pages.base_functions import BaseFunctions
from locators.locators import Locators
import allure
import settings


class TestBaseFunction:

    @allure.title("Переход по кнопке Конструктор")
    @allure.description("Нажататие кнопки Конструктор ведет на главную страницу")
    def test_transit_to_сonstructor(self, driver):
        base_function = BaseFunctions(driver)
        base_function.transit_to_constructor(driver)
        assert driver.current_url == settings.URL

    @allure.title("Переход по кнопке Лента заказов")
    @allure.description("Нажататие кнопки Лента заказов ведет на страницу заказов")
    def test_transit_to_order_list(self, driver):
        base_function = BaseFunctions(driver)
        base_function.transit_to_order_list(driver)
        assert driver.current_url == settings.URL + settings.ORDER_LIST

    @allure.title("Клик на ингридиент")
    @allure.description("После нажататия на ингридиент появится всплывающее окно с деталями")
    def test_click_ingridient(self, driver):
        base_function = BaseFunctions(driver)
        base_function.click_ingridient(driver)
        assert driver.find_element(*Locators.INGRIDIENT_MODAL_WINDOW).is_displayed()


    @allure.title("Закрытие модального окна по нажатию крестика")
    @allure.description("Модальное окно закрывается по нажатию крестика")
    def test_close_ingridient(self, driver):
        base_function = BaseFunctions(driver)
        base_function.close_ingridient(driver)
        assert driver.find_element(*Locators.INGRIDIENT_BUTTON_CLOSE).is_displayed() == False

    @allure.title("Создание заказа авторизованным пользователем")
    @allure.description("Авторизованный пользователь может создать заказ")
    def test_create_order(self, driver):
        base_function = BaseFunctions(driver)
        base_function.create_order(driver)
        assert driver.find_element(*Locators.CREATE_ORDER).text == 'идентификатор заказа'



    @allure.title("Добавление ингридиента в заказ")
    @allure.description("Количество ингридиентов увеличилось после добавления в заказ")
    def test_add_ingridient(self, driver):
        base_function = BaseFunctions(driver)
        base_function.add_ingridient(driver)
        assert driver.find_element(*Locators.INGRIDIENT_COUNTER).text == '2'
