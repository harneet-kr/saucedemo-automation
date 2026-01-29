"""Tests using Page object Model
Clean, readable, maintainable tests"""

import pytest

class TestLoginWithPOM:
    """Login tests using Page Object Model"""

    def test_successful_login(self, login_page, product_page):
        """Test sucessful login"""
        #Perform login
        login_page.login("standard_user", "secret_sauce")

        #Verify on product page
        assert product_page.is_on_products_page()
        assert product_page.get_page_title() == "Products"
        print("Login scuessful with POM")

    def test_invalid_credentials(self, login_page):
            """Test login with invalid credentials"""
            #Attempt login with wrong credentials
            login_page.login("invalid_user", "wrong_password")

            #Verify error message
            assert login_page.is_error_displayed()
            assert "do not match" in login_page.get_error_message()
            print("error message displayed correctly")

    @pytest.mark.parametrize("username, password, expected_error", [
            ("","secret_sauce", "Username is required"),
            ("standard_user", "Password is required"),
            ("", "", "Username is required"),
        ])

    def test_empty_fields(self, login_page, username, password, expected_error):
            """Test login with empty fields - Data driven Test"""
            login_page.login(username, password)

            assert login_page.is_empty_displayed()
            error_text = login_page.get_error_message()
            assert expected_error in error_text
            print(f"Error shown for empty fields: {expected_error}")

class TestShoppingCart:
    """Shopping cart tests"""
    def test_add_single_product(self, login_page, products_page):
        """Test adding one product to cart"""
        # Login
        login_page.login("standard_user", "secret_sauce")
        
        # Add product
        products_page.add_backpack_to_cart()
        
        # Verify cart count
        assert products_page.get_cart_count() == "1"
        print("✅ Product added to cart")
    
    def test_add_multiple_products(self, login_page, products_page):
        """Test adding multiple products"""
        # Login
        login_page.login("standard_user", "secret_sauce")
        
        # Add two products
        products_page.add_backpack_to_cart()
        products_page.add_bike_light_to_cart()
        
        # Verify cart count
        assert products_page.get_cart_count() == "2"
        print("✅ Multiple products added")
    
    def test_remove_product(self, login_page, products_page):
        """Test removing product from cart"""
        # Login and add product
        login_page.login("standard_user", "secret_sauce")
        products_page.add_backpack_to_cart()
        
        # Remove product
        products_page.remove_backpack_from_cart()
        
        # Verify cart is empty
        assert products_page.get_cart_count() == "0"
        print("✅ Product removed successfully")
    
    def test_cart_page_items(self, login_page, products_page, cart_page):
        """Test items show correctly in cart page"""
        # Login and add products
        login_page.login("standard_user", "secret_sauce")
        products_page.add_backpack_to_cart()
        products_page.add_bike_light_to_cart()
        
        # Go to cart
        products_page.click_cart()
        
        # Verify cart page
        assert cart_page.get_page_title() == "Your Cart"
        assert cart_page.get_cart_items_count() == 2
        print("✅ Cart page shows correct items")


class TestCheckoutFlow:
    """Complete checkout process tests"""
    
    def test_complete_purchase(self, login_page, products_page, 
                               cart_page, checkout_page):
        """Test end-to-end purchase flow"""
        # Step 1: Login
        login_page.login("standard_user", "secret_sauce")
        
        # Step 2: Add product
        products_page.add_backpack_to_cart()
        
        # Step 3: Go to cart
        products_page.click_cart()
        
        # Step 4: Proceed to checkout
        cart_page.click_checkout()
        
        # Step 5: Fill checkout info
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        
        # Step 6: Finish order
        checkout_page.click_finish()
        
        # Step 7: Verify success
        success_msg = checkout_page.get_success_message()
        assert "Thank you for your order" in success_msg
        print("✅ Complete purchase flow successful")
    
    @pytest.mark.parametrize("first,last,zip", [
        ("Alice", "Smith", "90210"),
        ("Bob", "Johnson", "10001"),
        ("Charlie", "Brown", "60601"),
    ])
    def test_checkout_different_users(self, login_page, products_page,
                                     cart_page, checkout_page, 
                                     first, last, zip):
        """Test checkout with different user data"""
        login_page.login("standard_user", "secret_sauce")
        products_page.add_backpack_to_cart()
        products_page.click_cart()
        cart_page.click_checkout()
        checkout_page.fill_checkout_info(first, last, zip)
        checkout_page.click_finish()
        
        assert "Thank you" in checkout_page.get_success_message()
        print(f"✅ Checkout successful for {first} {last}")
