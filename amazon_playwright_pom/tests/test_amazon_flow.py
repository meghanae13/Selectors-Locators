from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestAmazonEcommerceFlow:

    def test_amazon_ecommerce_flow(self, amazon_page):

        page = amazon_page
      
        # STEP 1: VERIFY HOME PAGE
      
        home_page = HomePage(page)

        home_page.verify_home_page()

        print("Home page loaded successfully")

        # STEP 2: SEARCH PRODUCT
      
        product_name = "laptop"

        home_page.search_product(product_name)

        search_results = SearchResultsPage(page)

        search_results.verify_search_results()

        product_count = search_results.get_product_count()

        print(
            f"Search completed. "
            f"Products displayed: {product_count}"
        )

        assert product_count > 0

        # STEP 3: OPEN FIRST PRODUCT
      
        search_results.open_first_product()

        product_page = ProductPage(page)

        product_page.verify_product_page()

        product_title = product_page.get_product_title()

        print(
            f"Selected product: {product_title}"
        )

        assert product_title != ""

        # STEP 4: ADD PRODUCT TO CART
       
        product_page.add_to_cart()

        product_page.verify_added_to_cart()

        print(
            "Product added to cart successfully"
        )

        # STEP 5: OPEN CART

        product_page.open_cart()

        cart_page = CartPage(page)

        cart_page.verify_cart_page()

        print(
            "Cart page opened successfully"
        )

        # STEP 6: VERIFY CART ITEM
    
        cart_page.verify_cart_item_exists()

        item_count = cart_page.get_cart_item_count()

        print(
            f"Cart contains {item_count} item(s)"
        )

        assert item_count > 0

        # STEP 7: CHECKOUT SIMULATION

        cart_page.proceed_to_checkout()

        print(
            "Checkout process initiated"
        )

        print(
            "Checkout simulation completed."
        )

        print(
            "No real order was placed."
        )
