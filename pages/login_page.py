"""
Login Page Object Model
Contains all elements and actions for login page
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Login page locators and methods"""

    #locators(stored as class variables)
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        """Initialize login page"""
        super().__init(driver)
        self.driver.get("https://www.saucedemo.com")

    def enter_username(self, username):
        """Enter username in username field"""
        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        """Enter password in password field"""
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """check if error message is shown"""
        return self.is_displayed(self.ERROR_MESSAGE)