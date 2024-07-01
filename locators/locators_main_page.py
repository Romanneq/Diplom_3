from selenium.webdriver.common.by import By


class MainPageButtons:
    BUTT_MAIN_PAGE = [By.XPATH, ".//button[contains(@class, 'button_button_type_primary')]"]  # локатор кнопки "Войти в аккаунт" и "Оформить заказ" на главной странице сервиса
    PERS_ACCOUNT = [By.XPATH, ".//p[text()='Личный Кабинет']"]  # локатор кнопки "Личный кабинет"
    ORDER_FEED = [By.XPATH, ".//p[text()='Лента Заказов']//parent::a"]  # локатор кнопки "Лента заказов"
    CONSTRUCTOR = [By.XPATH, ".//p[text()='Конструктор']//parent::a"]  # локатор кнопки "Конструктор"


class MainPageElements:
    LOGO_BURGER = [By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo__')]"]  # локатор логотипа сервиса
    FORM_ASSEMBLE_BURGER = [By.XPATH, ".//section[contains(@class, 'BurgerIngredients_ingredients')]"]  # локатор формы "Соберите бургер"
    ING_BUL = [By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']"]  # локатор ингредиента булки
    POPUP_WINDOW = [By.XPATH, ".//h2[text()='Детали ингредиента']//parent::div"]  # локатор окна с деталями
    CROSS_IN_WIN_ING = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened__')]/div[contains(@class, 'Modal_modal__container__')]//button"]  # локатор крестика в окне с деталями
    ORDER_BASKET = [By.XPATH, ".//span[contains(@class, 'BurgerConstructor_basket__listContainer__')]"]  # локатор корзины заказа
    ING_IN_ORD_BUL = [By.XPATH, ".//span[text()='Флюоресцентная булка R2-D3 (верх)']"]  # локатор булки в  корзине заказа
    COUNT_ING = [By.XPATH, ".//ul[contains(@class, 'BurgerIngredients_ingredients__list')][1]/a[1]/div[1]/p"]  # локатор счетчика ингредиента булки
    WIN_ORD_ID = [By.XPATH, ".//img[contains(@class, 'Modal_modal__image__')]"]  # локатор отображения окна с ID заказа
    ID_ORD = [By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow_')]"]  # локатор id заказа в окне оформленного заказа
