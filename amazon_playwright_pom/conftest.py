import pytest
from playwright.sync_api import Page


@pytest.fixture
def amazon_page(page: Page):

    try:
        page.goto(
            "https://www.amazon.in/",
            wait_until="commit",
            timeout=60000
        )

    except Exception as e:
        print("Amazon navigation warning:", e)

    # Give Amazon some time to render
    page.wait_for_timeout(5000)

    return page