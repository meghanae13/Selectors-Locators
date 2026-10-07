from playwright.sync_api import Page, expect
import re


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator(
            '[data-name="Active Items"] .sc-list-item'
        )

        self.quantity_dropdown = page.locator(
            'select[name^="quantity"]'
        )

        self.proceed_to_checkout_button = page.locator(
            'input[name="proceedToRetailCheckout"]'
        )

    def verify_cart_page(self):
        expect(
            self.page
        ).to_have_url(
            re.compile(r".*/gp/cart/.*")
        )

    def verify_cart_item_exists(self):
        expect(
            self.cart_items.first
        ).to_be_visible(timeout=10000)

    def get_cart_item_count(self):
        return self.cart_items.count()

    def proceed_to_checkout(self):
        expect(
            self.proceed_to_checkout_button
        ).to_be_visible(timeout=10000)

        self.proceed_to_checkout_button.click()
