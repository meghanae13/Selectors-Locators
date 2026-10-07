from playwright.sync_api import Page, expect


class ProductPage:

    def __init__(self, page: Page):
        self.page = page

        # Visible product title
        self.product_title = page.locator(
            "span#productTitle"
        )

        # Visible Add to Cart button
        self.add_to_cart_button = page.locator(
            "#add-to-cart-button:visible"
        ).first

        self.buy_now_button = page.locator(
            "#buy-now-button"
        )

        self.cart_confirmation = page.locator(
            "#sw-gtc"
        )

    def verify_product_page(self):
        expect(
            self.product_title
        ).to_be_visible()

    def get_product_title(self):
        return self.product_title.inner_text().strip()

    def add_to_cart(self):
        expect(
            self.add_to_cart_button
        ).to_be_visible(timeout=10000)

        self.add_to_cart_button.click()

    def verify_added_to_cart(self):
        expect(
            self.cart_confirmation
        ).to_be_visible(timeout=10000)

    def open_cart(self):
        self.page.locator(
            "#nav-cart"
        ).click()