import pytest
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.urls import MainPageUrl
from .pages.urls import BasketPageUrl


@pytest.mark.login
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MainPageUrl.main_page_url)
    page.open()
    page.should_be_main_page()
    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_page()


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MainPageUrl.main_page_url)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_basket_page()
    basket.should_be_no_goods_in_basket()
    basket.should_be_empty_basket_message()


@pytest.mark.language
def test_guest_can_change_language(browser):
    page = MainPage(browser, MainPageUrl.main_page_url)
    page.open()
    page.should_be_main_page()
    page.change_language()
    page.should_be_changed_language()


@pytest.mark.search
def test_guest_can_search_products(browser):
    page = MainPage(browser, MainPageUrl.main_page_url)
    page.open()
    page.should_be_main_page()
    page.searching_products()
    page.should_be_searched_product()


@pytest.mark.add_to_basket
def test_guest_can_add_to_basket_from_main_page(browser):
    page = MainPage(browser, MainPageUrl.main_page_url)
    page.open()
    page.should_be_main_page()
    page.change_language()
    page.should_be_changed_language()
    page.adding_to_basket_from_main_page()
    page.go_to_basket()
    basket = BasketPage(browser, BasketPageUrl.basket_url)
    basket.should_be_basket_page()
    basket.should_be_goods_in_basket()
