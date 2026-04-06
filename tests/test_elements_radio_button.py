from playwright.sync_api import expect

from pages.elements_radio_button import ElementsRadioButtonPage


def test_elements_radio_button(page):
    page.goto('https://demoqa.com/radio-button')
    elements_radio_button = ElementsRadioButtonPage(page)
    elements_radio_button.click_yes_radio_button()
    text_question = page.locator('div', has_text='Do you like the site?')
    text_answer = text_question.locator('p', has_text='You have selected')
    answer_span = text_answer.locator('span')
    expect(answer_span).to_contain_text('Yes')
    elements_radio_button.click_impressive_radio_button()
    expect(answer_span).to_contain_text('Impressive')