import allure
from playwright.sync_api import expect

from pages.demosite.elements_radio_button import ElementsRadioButtonPage


@allure.title('Проверка нажатий на радио батоны')
@allure.severity(allure.severity_level.TRIVIAL)
def test_elements_radio_button(page_quick_tour):
    page_quick_tour.goto('https://demoqa.com/radio-button')
    elements_radio_button = ElementsRadioButtonPage(page_quick_tour)
    with allure.step("тыкаем на 'yes'"):
        elements_radio_button.click_yes_radio_button()
        text_question = page_quick_tour.locator('div', has_text='Do you like the site?')
        text_answer = text_question.locator('p', has_text='You have selected')
        answer_span = text_answer.locator('span')
        expect(answer_span).to_contain_text('Yes')

    with allure.step("тыкаем на Impressive"):
        elements_radio_button.click_impressive_radio_button()
        expect(answer_span).to_contain_text('Impressive')
