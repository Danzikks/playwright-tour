from playwright.sync_api import Page


class ElementsTextBoxPage:
    def __init__(self, page: Page):
        self.page = page
        self.full_name_input = page.locator('#userName')
        self.email_input = page.locator('#userEmail')
        self.current_address_input = page.locator('#currentAddress')
        self.permanent_address_input = page.locator('#permanentAddress')
        self.submit_button = page.locator('#submit')
        self.output_div = page.locator('#output')
        self.output_name = page.locator('#output #name')
        self.output_email = page.locator('#output #email')
        self.output_current_address = page.locator('#output #currentAddress')
        self.output_permanent_address = page.locator('#output #permanentAddress')

    def fill_full_name(self, full_name: str):
        self.full_name_input.fill(full_name)

    def fill_email(self, email: str):
        self.email_input.fill(email)

    def fill_current_address(self, cur_address: str):
        self.current_address_input.fill(cur_address)

    def fill_permanent_address(self, perm_address: str):
        self.permanent_address_input.fill(perm_address)

    def get_output(self):
        return self.output_div

    def submit(self):
        self.submit_button.click()

    def get_full_name(self):
        return self.full_name_input

    def get_email(self):
        return self.email_input

    def get_current_address(self):
        return self.current_address_input

    def get_permanent_address(self):
        return self.permanent_address_input

