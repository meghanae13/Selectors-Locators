from playwright.sync_api import Page, expect
from urllib.parse import unquote, urlparse, parse_qs


class SearchResultsPage:

    def __init__(self, page: Page):

        self.page = page

        self.product_cards = page.locator(
            '[data-component-type="s-search-result"]'
        )

    # --------------------------------------------------
    # Verify Search Results
    # --------------------------------------------------
    def verify_search_results(self):

        expect(
            self.product_cards.first
        ).to_be_visible()

    # --------------------------------------------------
    # Get Product Count
    # --------------------------------------------------
    def get_product_count(self):

        return self.product_cards.count()

    # --------------------------------------------------
    # Open First Product
    # --------------------------------------------------
    def open_first_product(self):

        first_card = self.product_cards.first

        links = first_card.locator("a")

        link_count = links.count()

        print(
            "Links inside first product card:",
            link_count
        )

        for i in range(link_count):

            link = links.nth(i)

            href = link.get_attribute("href")

            print(
                f"Link {i}: {href}"
            )

            if not href:
                continue

            # Decode Amazon URL
            decoded_href = unquote(href)

            print(
                f"Decoded Link {i}: {decoded_href}"
            )

            # --------------------------------------------------
            # Sponsored Amazon URL
            # --------------------------------------------------
            if "sspa/click" in decoded_href:

                parsed_url = urlparse(decoded_href)

                query_params = parse_qs(
                    parsed_url.query
                )

                product_urls = query_params.get("url")

                if product_urls:

                    product_url = unquote(
                        product_urls[0]
                    )

                    print(
                        "Extracted product URL:",
                        product_url
                    )

                    if product_url.startswith("/"):

                        product_url = (
                            "https://www.amazon.in"
                            + product_url
                        )

                    print(
                        "Navigating to product:",
                        product_url
                    )

                    self.page.goto(
                        product_url,
                        wait_until="domcontentloaded"
                    )

                    print(
                        "Product page URL:",
                        self.page.url
                    )

                    return

            # --------------------------------------------------
            # Direct Product URL
            # --------------------------------------------------
            elif "/dp/" in decoded_href:

                product_url = decoded_href

                if product_url.startswith("/"):

                    product_url = (
                        "https://www.amazon.in"
                        + product_url
                    )

                print(
                    "Opening direct product:",
                    product_url
                )

                self.page.goto(
                    product_url,
                    wait_until="domcontentloaded"
                )

                print(
                    "Product page URL:",
                    self.page.url
                )

                return

        # --------------------------------------------------
        # Product Not Found
        # --------------------------------------------------
        raise AssertionError(
            "No valid product URL was found "
            "in the first search result."
        )