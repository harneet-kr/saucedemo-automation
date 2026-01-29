""" Products page Object model"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    """Product page locators and methods"""

    #Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    #Product buttons(examples)
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sace-labs-bike-light")

    def __init__(self, driver):
        """initialize product page"""
        super().__init__