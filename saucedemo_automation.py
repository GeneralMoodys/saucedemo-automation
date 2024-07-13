from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Atur opsi chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start the browser maximized

# menginisialisasi webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

try:
    # Membuka URL
    driver.get("https://www.saucedemo.com/v1/index.html")

    # Ketika membuka url menunggu selama 5 detik sampe memuat web secara sempurna
    time.sleep(5)

    # mencari id user-name dan id password
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")

    # Memasukkan id username= "standard_user" dan password = "secret_sauce"
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    # Cari id login-button dan klik tombol login-button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Menunggu selama 5 detik saat web memuat hingga selesai
    time.sleep(5)

    # Menampilkan ketika login berhasil maka muncul pesan "Login successful!" jika gagal maka "Login failed"
    if "inventory.html" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed.")

finally:
    # Setelah automation login dilakukan maka browser akan tertutup
    driver.quit()
