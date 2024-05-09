from selenium.webdriver.common.by import By

class BasePageLocators():
    # локаторы для BasePage
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    # локаторы для BasketPage
    BASKET_TEXT_ABOUT_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a")

class LoginPageLocators():
    # локаторы для Login form
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # локаторы для Registration form
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FORM = (By.NAME, 'registration-email')
    REGISTER_PASS_FORM = (By.NAME, 'registration-password1')
    REGISTER_CONFIRM_PASS_FORM = (By.NAME, 'registration-password2')
    REGISTER_BUTTON = (By.NAME, "registration_submit")
class ProductPageLocators:
    # локаторы для ProductPage
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ADD_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alertinner>strong")
    ADD_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages >.alert:last-child > .alertinner > p:first-child > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages >.alert:first-child > .alertinner')