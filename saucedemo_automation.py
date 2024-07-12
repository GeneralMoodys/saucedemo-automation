from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start the browser maximized

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open the URL
    driver.get("https://www.saucedemo.com/v1/index.html")

    # Wait for the page to load
    time.sleep(2)

    # Find username and password fields
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    # Enter username and password
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    # Find and click the login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Wait for login to complete
    time.sleep(3)

    # Perform actions after login, for example, checking if the login was successful
    if "inventory.html" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed.")

finally:
    # Close the browser
    driver.quit()
