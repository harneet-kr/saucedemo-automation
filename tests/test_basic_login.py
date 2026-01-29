from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_successful():
    #Testcase: Verify user can login with valid credentials.
 # Step1: Setup broswer

 driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
 driver.maximize_window()

 #step 2: Navigate website
 driver.get("https://www.saucedemo.com")
 time.sleep(2)

 #Step 3: Finder username field and enter username
 username_field = driver.find_element(By.ID, "user-name")
 username_field.send_keys("standard_user")

 # Step4: Find password field and enter password
 password_field = driver.find_element(By.ID, "password")
 password_field.send_keys("secret_sauce")

 #step5: find login button and click on it
 login_button = driver.find_element(By.ID, "login-button")
 login_button.click()
 time.sleep(2)

 #step6: verify login successful 
 current_url = driver.current_url
 assert "inventory.html" in current_url, "Login failed - not a product page"

 print(f"Test passed: Login successful")

#step 7 close browser
 driver.quit()

#Run this file directly
if __name__ == "__main__":
 test_login_successful()


