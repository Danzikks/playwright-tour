import re

import allure
from playwright.sync_api import expect

from pages.demosite.elements_text_box import ElementsTextBoxPage

@allure.title('Заполнение формы')
@allure.description('Проверяем создание формы')
def test_fill_name_email(page):
    page.goto("https://demoqa.com/elements")
    page.click('#item-0')
    elements_text_box = ElementsTextBoxPage(page)
    assert page.url == "https://demoqa.com/text-box"
    with allure.step('Вводим имя'):
        elements_text_box.fill_full_name('John')

    with allure.step('Вводим email'):
        elements_text_box.fill_email('john@mail.ru')

    with allure.step('Нажимаем submit'):
        elements_text_box.submit()
    expect(elements_text_box.get_full_name()).to_be_visible()
    expect(elements_text_box.get_email()).to_be_visible()

@allure.title('Невалидный email')
@allure.description('Ввод невалидного email')
def test_invalid_email(page):
    elements_text_box = ElementsTextBoxPage(page)
    page.goto("https://demoqa.com/elements")
    page.click('#item-0')
    assert page.url == "https://demoqa.com/text-box"
    with allure.step('Вводим имя'):
        elements_text_box.fill_full_name('John Bla Blabla')

    with allure.step('Вводим невалидный email'):
        elements_text_box.fill_email('nevalid_email')

    with allure.step('Ошибка клиентской валидации'):
        page.click('#submit')
        expect(elements_text_box.get_email()).to_have_class(re.compile(r"field-error"))


def test_full_fill(page):
    elements_text_box = ElementsTextBoxPage(page)
    page.goto("https://demoqa.com/elements")
    page.click('#item-0')
    assert page.url == "https://demoqa.com/text-box"
    elements_text_box.fill_full_name('John bla bla bla')
    elements_text_box.fill_email('dev@mail.ru')
    elements_text_box.fill_current_address('123 Main St')
    elements_text_box.fill_permanent_address('456 Elm St')
    elements_text_box.submit()
    expect(elements_text_box.output_div).to_be_visible()
    expect(elements_text_box.output_name).to_be_visible()
    expect(elements_text_box.output_email).to_be_visible()
    expect(elements_text_box.output_current_address).to_be_visible()
    expect(elements_text_box.output_permanent_address).to_be_visible()


