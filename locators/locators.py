from selenium.webdriver.common.by import By


class Locators:


    RESTORE_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")                 # Ссылка Восстановить пароль
    RESTORE_PASSWORD_INPUT_EMAIL = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")   # Поле ввода email
    RESTORE_PASSWORD_BUTTON_RESTORE = (By.XPATH, ".//button[text()='Восстановить']")         # Кнопка Восстановить
    RESTORE_PASSWORD_HEDER = (By.XPATH, ".//h2[text()='Восстановление пароля']")             # Хедер Восстановление пароля
    RESTORE_PASSWORD_ICON_SHOW_PASSWORD = (By.XPATH, ".//div[@class='input__icon input__icon-action']")    # Иконка глаза, показать/скрыть пароль
    RESTORE_PASSWORD_INPUT_ACTIVE = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']") # Подсветка поля ввода пароля

    PERSONAL_AREA_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")                       # Кнопка Личный кабинет
    PERSONAL_AREA_ORDERS_HISTORY = (By.XPATH, ".//a[text()='История заказов']")              # История заказов в ЛК
    PERSONAL_AREA_BUTTON_LOGOUT = (By.XPATH, ".//button[text()='Выход']")                    # Кнопка Выход в ЛК

    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")                            # Кнопка Конструктор
    BUTTON_ORDER_LIST = (By.XPATH, ".//p[text()='Лента Заказов']")                           # КНопка Лента заказов
    BUTTON_CREATE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")                   # Кнопка Оформить заказ

    INGRIDIENT_BULKI_NAME = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']") # Игридиент
    INGRIDIENT_MODAL_WINDOW = (By.XPATH, ".//h2[text()='Детали ингредиента']")               # Всплывающее окно Детали ингридиента
    INGRIDIENT_BUTTON_CLOSE = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")  # Крестик закрытия
    INGRIDIENT_ADD = (By.XPATH, ".//span[text()='Перетяните булочку сюда (верх)']")          # Место для заказа
    INGRIDIENT_COUNTER = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']/div/p")# Счетчик ингридиента
    INGRIDIENT_PRICE = (By.XPATH, ".//p[@class='text text_type_digits-medium mr-3']")        # Цена заказа
    INGRIDIENT_NAME_IN_CHECK = (By.XPATH, ".//span[text()='Краторная булка N-200i (верх)']") # Имя булки в чеке

    AUTH_BUTTON_GO_TO_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")            # Кнопка Войти в аккаунт
    AUTH_BUTTON_AUTH = (By.XPATH, ".//button[text()='Войти']")                               # Кнопка Войти
    AUTH_EMAIL = (By.XPATH, ".//input[@name='name']")                                        # Поле ввода логина
    AUTH_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")                                   # Поле ввода пароля

    CREATE_ORDER = (By.XPATH, ".//p[text()='идентификатор заказа']")                         # Хедер 'идентификатор заказа'

    LIST_ORDER_FIRST_ORDER = (By.XPATH, ".//ul/li[1]/a[@class='OrderHistory_link__1iNby']")  # Первый заказ в списке заказов
    LIST_ORDER_FIRST_ORDER_NUMBER = (By.XPATH, ".//div[@class = 'OrderFeed_contentBox__3-tWb']/ul/li[1]/a/div/p[@class='text text_type_digits-default']") # Номер первого заказа в Ленте заказов
    LIST_ORDER_MODAL_WINDOW_TEXT = (By.XPATH, ".//p[text()='Cостав']")                       # Текст модального окна
    ORDER_HISTORY_LAST_ORDER = (By.XPATH, ".//li[@class='OrderHistory_listItem__2x95r mb-6'][last()]/a/div/p") # Последний заказ в истории заказов
    LIST_ORDER_ORDER_IN_WORK = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']") # Номер заказа в работе
    LIST_ORDER_ALL_ORDERS = (By.XPATH, ".//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']") # Выполнено заказов за все время
    LIST_ORDER_TODAY_ORDERS = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/parent::*/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']") # Выполнено заказов за сегодня

