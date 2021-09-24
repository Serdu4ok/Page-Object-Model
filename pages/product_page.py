import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        # Find name and price of book
        name_of_book = self.convert_to_text(*ProductPageLocators.NAME_OF_BOOK)
        price_of_book = self.convert_to_text(*ProductPageLocators.PRICE_OF_BOOK)

        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket btn is absent"
        self.click(ProductPageLocators.ADD_TO_BASKET_BTN)
        self.solve_quiz_and_get_code()

        # find msg after click on add to basket btn
        msg_name_of_book = self.convert_to_text(*ProductPageLocators.MSG_PRODUCT_HAS_BEEN_ADD)
        msg_price_of_book = self.convert_to_text(*ProductPageLocators.MSG_VALUE_BASKET)

        assert name_of_book == msg_name_of_book, "Name of book incorrect after add to basket"
        assert price_of_book == msg_price_of_book, "Price of book incorrect after add to basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), \
            "Success message is presented, but should not be"
        time.sleep(5)

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), \
            "Success message is presented, but should be disappeared"
