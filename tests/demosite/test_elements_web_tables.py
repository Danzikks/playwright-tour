import allure

from pages.demosite.elements_web_tables import ElementsWebTablesPage
from playwright.sync_api import expect


@allure.title('Создание и удаление строки в таблице')
def test_create_registration_form_and_delete(page_quick_tour):
    elements_web_tables = ElementsWebTablesPage(page_quick_tour)
    page_quick_tour.goto("https://demoqa.com/elements")
    page_quick_tour.click('#item-3')
    assert page_quick_tour.url == "https://demoqa.com/webtables"
    with allure.step('Кнопка создание формы'):
        elements_web_tables.add_button.click()
    with allure.step('Заполнение формы'):
        elements_web_tables.fill_first_name('Alex')
        elements_web_tables.fill_last_name('Parker')
        elements_web_tables.fill_email('email@mail.ru')
        elements_web_tables.fill_age('15')
        elements_web_tables.fill_salary('1200')
        elements_web_tables.fill_department('Coach')
    with allure.step('Сохранение формы'):
        elements_web_tables.submit()
        page_quick_tour.screenshot(path="../../test_results/screenshot.png")

    with allure.step('Проверка создание строки в таблице'):
        row = page_quick_tour.locator('tr', has_text='email@mail.ru')
        expect(row).to_be_visible()
        expect(row).to_contain_text('Alex')
        expect(row).to_contain_text('Coach')
        expect(row).to_contain_text('Parker')
    with allure.step('удаление созданной строки'):
        row.locator("[title='Delete']").click()
        expect(row).not_to_be_visible()


@allure.title('Редактирование формы')
def test_update_form(page_quick_tour):
    page_quick_tour.goto("https://demoqa.com/elements")
    page_quick_tour.click('#item-3')
    assert page_quick_tour.url == "https://demoqa.com/webtables"

    with allure.step('Кнопка редактирования'):
        row = page_quick_tour.locator('tr', has_text='kierra@example.com')
        row.locator("[title='Edit']").click()
    elements_web_tables = ElementsWebTablesPage(page_quick_tour)

    with allure.step('Ввод новых значение в редактируемую форму'):
        elements_web_tables.fill_first_name('Браза')
        elements_web_tables.fill_last_name('Мой')
        elements_web_tables.fill_email('brasa@mail.ru')
    with allure.step('Сохрание формы редактирования'):
        elements_web_tables.submit()
        expect(row).not_to_be_visible()
        row = page_quick_tour.locator('tr', has_text='brasa@mail.ru')
        expect(row).to_be_visible()
        expect(row).to_contain_text('Браза')
        expect(row).to_contain_text('Мой')
