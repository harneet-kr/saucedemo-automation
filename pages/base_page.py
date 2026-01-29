"""Base page: common methods used by all pages"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage: 
    """Parent class for all the page objects"""

    def __init__(self, driver):
        """initialize with driver"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by_locator):
        """find element to wait"""
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))
    
    def enter_text(self, by_locator, text):
        """Clear and enter text"""
        element = self.find_element(by_locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        """get element text"""
        element = self.find_element(by_locator)
        return element.text
    
    def is_displayed(self, by_locator):
        """check if element is doispalyed"""
        try:
            element = self.find_element(by_locator)
            return element.is_displayed()
        except:
            return False
        
    def get_current_url(self):
        """Get current page url"""
        return self.driver.current_url
    
    