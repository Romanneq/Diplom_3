from selenium.webdriver.common.by import By


class MainPageButtons:
    butt_main_page = [By.XPATH, ".//button[contains(@class, 'button_button_type_primary')]"]  # локатор кнопки "Войти в аккаунт" и "Оформить заказ" на главной странице сервиса
    pers_accoount = [By.XPATH, ".//p[text()='Личный Кабинет']"]  # локатор кнопки "Личный кабинет"
    order_feed = [By.XPATH, ".//p[text()='Лента Заказов']//parent::a"]  # локатор кнопки "Лента заказов"
    constructor = [By.XPATH, ".//p[text()='Конструктор']//parent::a"]  # локатор кнопки "Конструктор"


class MainPageElements:
    logo_burger = [By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo__')]"]  # локатор логотипа сервиса
    form_assemble_burger = [By.XPATH, ".//section[contains(@class, 'BurgerIngredients_ingredients')]"]  # локатор формы "Соберите бургер"
    ing_bul = [By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']"]  # локатор ингредиента булки
    popup_window = [By.XPATH, ".//h2[text()='Детали ингредиента']//parent::div"]  # локатор окна с деталями
    cross_in_win_ing = [By.XPATH, ".//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-10')]//following::button[1]"]  # локатор крестика в окне с деталями
    order_basket = [By.XPATH, ".//span[contains(@class, 'BurgerConstructor_basket__listContainer__')]"]  # локатор корзины заказа
    ing_in_ord_bul = [By.XPATH, ".//span[text()='Флюоресцентная булка R2-D3 (верх)']"]  # локатор булки в  корзине заказа
    count_ing = [By.XPATH, ".//ul[contains(@class, 'BurgerIngredients_ingredients__list__2A-mT')][1]/a[1]/div[1]/p"]  # локатор счетчика ингредиента булки
    win_ord_id = [By.XPATH, ".//img[contains(@class, 'Modal_modal__image__')]"]  # локатор отображения окна с ID заказа
    id_ord = [By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__')]"]  # локатор id заказа в окне оформленного заказа
