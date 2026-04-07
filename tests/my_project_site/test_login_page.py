from time import sleep

from pages.my_project_site.login_page import LoginPage
from playwright.sync_api import expect

def test_login_page(page):
    page.goto('https://quick-tour.dprusakov.ru/login')
    login_page = LoginPage(page)
    login_page.fill_login_input('test')
    login_page.fill_password_input('123456')
    login_page.click_submit_button()
    assert page.url == 'https://quick-tour.dprusakov.ru/'

