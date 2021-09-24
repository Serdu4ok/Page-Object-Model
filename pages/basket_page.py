from pages.base_page import BasePage
from pages.locators import BasePageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_LINK_IN_BASKET), "Product is present in basket"

    def msg_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.MSG_BASKET_EMPTY), "Msg that basket empty is absent"

