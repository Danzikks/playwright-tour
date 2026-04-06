from playwright.sync_api import Page

class ElementsRadioButtonPage:
    def __init__(self, page: Page):
        self.page = page
        self.radio_yes_button = self.page.locator('#yesRadio')
        self.radio_impressive_button = self.page.locator('#impressiveRadio')


    def click_yes_radio_button(self):
        self.radio_yes_button.click()

    def click_impressive_radio_button(self):
        self.radio_impressive_button.click()