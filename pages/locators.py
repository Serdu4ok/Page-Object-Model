from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    # LOGIN Form
    EMAIL_ADRESS_FOR_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASS_FOR_LOGIN = (By.CSS_SELECTOR, "#id_login-password")

    # Registration Form
    EMAIL_ADRESS_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_CONFIRM_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")

    CONFIRM_REGISTRATION_BTN = (By.CSS_SELECTOR, ".register_form .btn.btn-lg.btn-primary ")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_OF_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    SUCCESS_MSG = (By.XPATH, "//div[@id='messages']//div")
    MSG_PRODUCT_HAS_BEEN_ADD = (By.XPATH, "//div[@id='messages']//strong")
    MSG_VALUE_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    PRODUCT_LINK_IN_BASKET = (By.CSS_SELECTOR, ".basket-title.hidden-xs")
    MSG_BASKET_EMPTY = (By.XPATH, "//div[@id='content_inner']//p//a")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
