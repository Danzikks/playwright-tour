from playwright.sync_api import Page


class ElementsWebTablesPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_button = page.locator('#addNewRecordButton')
        self.first_name_input = page.locator('#userForm #firstName')
        self.last_name_input = page.locator('#userForm #lastName')
        self.email_input = page.locator('#userForm #userEmail')
        self.age_input = page.locator('#userForm #age')
        self.salary_input = page.locator('#userForm #salary')
        self.department_input = page.locator('#userForm #department')
        self.submit_button = page.locator('#userForm #submit')


    def fill_first_name(self, first_name: str):
        self.first_name_input.fill(first_name)

    def fill_last_name(self, last_name: str):
        self.last_name_input.fill(last_name)

    def fill_email(self, email: str):
        self.email_input.fill(email)

    def fill_age(self, age: str):
        self.age_input.fill(age)

    def fill_salary(self, salary: str):
        self.salary_input.fill(salary)

    def fill_department(self, department: str):
        self.department_input.fill(department)

    def submit(self):
        self.submit_button.click()