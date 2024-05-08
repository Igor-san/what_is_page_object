from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_items_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def product_price_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_product_price = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_PRICE).text
        assert product_price == message_product_price, \
            f'Product price in basket must be {product_price}, but got {message_product_price}'

    def product_name_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print(f"product_name {product_name}")
        message_product_name = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_NAME).text
        assert product_name == message_product_name, \
            f'Product name in message must be {product_name}, but got {message_product_name}'

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Guest can see success message, but should not!"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Guest can see success message, but should not!"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message not disappeared!"
