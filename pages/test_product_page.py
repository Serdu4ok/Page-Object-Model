import pytest

from pages.basket_page import BasketPage
from pages.generate_data import GenerateData
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.parametrize('link', GenerateData.generate_link_for_product(10, *[7]))
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()


@pytest.mark.parametrize('link', GenerateData.generate_link_for_product(10, *range(10)))
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', GenerateData.generate_link_for_product(10, *range(10)))
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
    page.should_not_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize('link', GenerateData.generate_link_for_product(1))
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.msg_basket_is_empty()

