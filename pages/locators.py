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

