import allure
import pytest

from pages.my_project_site.login_page import LoginPage


@allure.title('Логин с валидными данными')
@allure.description('Проверяем успешный вход')
@allure.severity(severity_level=allure.severity_level.BLOCKER)
def test_login_page(page_quick_tour):
    with allure.step('Открываем страницу'):
        page_quick_tour.goto('login')

    login_page = LoginPage(page_quick_tour)

    with allure.step('Вводим данные'):
        login_page.fill_login_input('test')
        login_page.fill_password_input('123456')

    with allure.step('Нажимаем кнопку войти'):
        login_page.click_submit_button()

    assert page_quick_tour.url == 'https://quick-tour.dprusakov.ru/'

@allure.title('Авторизация с невалидными данными')
@pytest.mark.parametrize("login, password", [
    ('test', '123456 '),
    ('', '123456'),
    ('123456', '123456'),
])
def test_negative_login_page(page_quick_tour, login, password):
    page_quick_tour.goto('login')
    login_page = LoginPage(page_quick_tour)
    with allure.step(f"вводим login: {login}"):
        login_page.fill_login_input(login)
    with allure.step(f"вводим password: {password}"):
        login_page.fill_password_input(password)
    with allure.step('нажимаем на кнопку авторизации'):
        login_page.click_submit_button()
    assert page_quick_tour.url == 'https://quick-tour.dprusakov.ru/login'
