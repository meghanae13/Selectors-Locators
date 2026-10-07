from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):

        self.page = page

        self.checkout_heading = page.locator(
            "h1"
        )

        self.address_section = page.locator(
            "#address-book-entry-0"
        )

        self.continue_button = page.locator(
            "input[type='submit']"
        )

    def verify_checkout_page(self):

        expect(
            self.page
        ).to_have_url(
            lambda url: (
                "checkout" in url.lower()
                or "buy" in url.lower()
            )
        )

    def verify_address_section(self):

        expect(
            self.address_section
        ).to_be_visible()

    def continue_checkout(self):

        self.continue_button.first.click()