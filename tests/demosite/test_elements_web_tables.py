from time import sleep

from pages.demosite.elements_web_tables import ElementsWebTablesPage
from playwright.sync_api import expect


def test_create_registration_form_and_delete(page):
    elements_web_tables = ElementsWebTablesPage(page)
    page.goto("https://demoqa.com/elements")
    page.click('#item-3')
    assert page.url == "https://demoqa.com/webtables"
    elements_web_tables.add_button.click()
    elements_web_tables.fill_first_name('Alex')
    elements_web_tables.fill_last_name('Parker')
    elements_web_tables.fill_email('email@mail.ru')
    elements_web_tables.fill_age('15')
    elements_web_tables.fill_salary('1200')
    elements_web_tables.fill_department('Coach')
    elements_web_tables.submit()
    page.screenshot(path="../screenshots/screenshot.png")
    row = page.locator('tr', has_text='email@mail.ru')
    expect(row).to_be_visible()
    expect(row).to_contain_text('Alex')
    expect(row).to_contain_text('Coach')
    expect(row).to_contain_text('Parker')
    row.locator("[title='Delete']").click()
    expect(row).not_to_be_visible()
    sleep(3)


def test_update_form(page):
    page.goto("https://demoqa.com/elements")
    page.click('#item-3')
    assert page.url == "https://demoqa.com/webtables"
    row = page.locator('tr', has_text='kierra@example.com')
    row.locator("[title='Edit']").click()
    elements_web_tables = ElementsWebTablesPage(page)
    elements_web_tables.fill_first_name('Браза')
    elements_web_tables.fill_last_name('Мой')
    elements_web_tables.fill_email('brasa@mail.ru')
    elements_web_tables.submit()
    expect(row).not_to_be_visible()
    row = page.locator('tr', has_text='brasa@mail.ru')
    expect(row).to_be_visible()
    expect(row).to_contain_text('Браза')
    expect(row).to_contain_text('Мой')
