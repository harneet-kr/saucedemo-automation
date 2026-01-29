from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestSaucedemo:
    """Group of related tests"""
    
    def setup_method(self):
        """Runs BEFORE each test - sets up browser"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        time.sleep(1)
    
    def teardown_method(self):
        """Runs AFTER each test - closes browser"""
        time.sleep(1)
        self.driver.quit()
    
    def login(self, username, password):
        """Helper method to login"""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
    
    def test_valid_login(self):
        """Test Case 1: Login with valid credentials"""
        self.login("standard_user", "secret_sauce")
        
        # Verify login successful
        assert "inventory.html" in self.driver.current_url
        print("✅ Test 1 Passed: Valid login successful")
    
    def test_invalid_login(self):
        """Test Case 2: Login with invalid credentials"""
        self.login("invalid_user", "wrong_password")
        
        # Verify error message appears
        error = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert error.is_displayed()
        assert "username and password do not match" in error.text.lower()
        print("✅ Test 2 Passed: Error message shown for invalid login")
    
    def test_locked_user(self):
        """Test Case 3: Login with locked user"""
        self.login("locked_out_user", "secret_sauce")
        
        # Verify locked user error
        error = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert "locked out" in error.text.lower()
        print("✅ Test 3 Passed: Locked user error shown")
    
    def test_add_to_cart(self):
        """Test Case 4: Add product to cart"""
        # Login first
        self.login("standard_user", "secret_sauce")
        
        # Click "Add to cart" for first product
        add_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_button.click()
        time.sleep(2)
        
        # Navigate directly to cart page (more reliable)
        self.driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(2)
        
        # Verify we're on cart page
        assert "cart.html" in self.driver.current_url
        
        # Verify item is in cart
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 1, f"Expected 1 item in cart, found {len(cart_items)}"
        
        print("✅ Test 4 Passed: Product added to cart")
    
    def test_remove_from_cart(self):
        """Test Case 5: Remove product from cart"""
        # Login and add product
        self.login("standard_user", "secret_sauce")
        
        # Add product to cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        
        # Navigate directly to cart page
        self.driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(2)
        
        # Verify we're on cart page
        assert "cart.html" in self.driver.current_url
        
        # Verify item is in cart first
        cart_items_before = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items_before) == 1, "Cart should have 1 item before removal"
        
        # Find and click the remove button
        remove_button = self.driver.find_element(By.CSS_SELECTOR, "button[class*='cart_button']")
        remove_button.click()
        time.sleep(1)
        
        # Verify cart is now empty
        cart_items_after = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items_after) == 0, f"Cart should be empty, but has {len(cart_items_after)} items"
        
        print("✅ Test 5 Passed: Product removed from cart")
# Run with pytest: pytest tests/test_basic_scenarios.py -v -s