from playwright.sync_api import Page, expect


class HomePage:

    def __init__(self, page: Page):

        self.page = page

        self.search_box = page.locator(
            "#twotabsearchtextbox"
        )

        self.search_button = page.locator(
            "#nav-search-submit-button"
        )

        self.account_list = page.locator(
            "#nav-link-accountList"
        )

        self.cart_icon = page.locator(
            "#nav-cart"
        )

    def verify_home_page(self):

        print("Current URL:", self.page.url)

        print("Page title:", self.page.title())

        print(
            "Search box count:",
            self.search_box.count()
        )

        print(
            "Page text:",
            self.page.locator("body").inner_text()[:1000]
        )

    def search_product(self, product_name: str):

        self.search_box.fill(product_name)
        self.search_button.click()