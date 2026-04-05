from pages.elements_web_tables import ElementsWebTablesPage
from playwright.sync_api import expect

def test_create_registration_form(page):
    elements_web_tables = ElementsWebTablesPage(page)
    page.goto("https://demoqa.com/elements")
    page.click('#item-3')
    assert page.url == "https://demoqa.com/webtables"
    elements_web_tables.add_button.click()
    elements_web_tables.fill_first_name('blabla')
    elements_web_tables.fill_last_name('blabla')
    elements_web_tables.fill_email('email@mail.ru')
    elements_web_tables.fill_age('15')
    elements_web_tables.fill_salary('1200')
    elements_web_tables.fill_department('blabla')
    elements_web_tables.submit()
    page.screenshot(path="screenshots/screenshot.png")

