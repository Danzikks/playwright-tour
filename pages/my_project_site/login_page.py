from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_input = self.page.locator('#inputLogin')
        self.password_input = self.page.locator('#inputPassword')
        self.submit_button = self.page.get_by_role('button', name='Авторизоваться')

    def fill_login_input(self, login_input: str):
        self.login_input.fill(login_input)

    def fill_password_input(self, password_input: str):
        self.password_input.fill(password_input)

    def click_submit_button(self):
        self.submit_button.click()
