import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.find_url, "login is not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADRESS_FOR_LOGIN), "Email for login is not presented"
        assert self.is_element_present(*LoginPageLocators.PASS_FOR_LOGIN), "Pass for login is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADRESS_FOR_REGISTRATION), "Email for registration is " \
                                                                                          "not presented "
        assert self.is_element_present(*LoginPageLocators.PASS_FOR_REGISTRATION), "Pass for registration is not " \
                                                                                  "presented "
        assert self.is_element_present(*LoginPageLocators.PASS_CONFIRM_FOR_REGISTRATION), "Pass confirm for " \
                                                                                          "registration is not " \
                                                                                          "presented "

    def register_new_user(self, email, password):
        assert self.find_and_send_element(*LoginPageLocators.EMAIL_ADRESS_FOR_REGISTRATION, email), "Email doesn't " \
                                                                                                    "filled "
        assert self.find_and_send_element(*LoginPageLocators.PASS_FOR_REGISTRATION, password), "PASS doesn't filled"
        assert self.find_and_send_element(*LoginPageLocators.PASS_CONFIRM_FOR_REGISTRATION, password), "Confirm PASS " \
                                                                                                       "doesn't filled "
        self.click(LoginPageLocators.CONFIRM_REGISTRATION_BTN)



