from playwright.sync_api import Page, expect


class SignInPage:

    def __init__(self, page: Page):
        self.page = page

        self.email_input = page.locator("#ap_email")
        self.continue_button = page.locator(
            "input#continue"
        )

        self.password_input = page.locator("#ap_password")
        self.signin_button = page.locator(
            "#signInSubmit"
        )

        self.create_account_link = page.locator(
            "#createAccountSubmit"
        )

    def verify_signin_page(self):
        expect(
            self.email_input
        ).to_be_visible()

    def enter_email(self, email: str):
        self.email_input.fill(email)

    def click_continue(self):
        self.continue_button.click()

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_signin(self):
        self.signin_button.click()

    def open_create_account(self):
        self.create_account_link.click()