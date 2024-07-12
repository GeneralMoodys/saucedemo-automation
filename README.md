Disini kita akan membuat script automation dengan fungsi LOGIN pada link https://www.saucedemo.com/v1/index.html

1. Install python pada sistem operasi
2. install selenium menggunakan python dengan command prompt, perintahnya "pip install selenium"
3. Download chromedriver dan jalankan perintah "pip install webdriver-manager" pada command prompt.
4. Buat file python.
5. Buat Script pada python,
   -  langkah awal import libraries 'from selenium import webdriver' adalah untuk Mengimpor modul webdriver dari Selenium, yang digunakan untuk mengendalikan browser.
   -  dilanjutkan dengan beberapa libraries yang lainnya 'from selenium.webdriver.common.by import By' libraries ini adalah untuk Mengimpor By, yang digunakan untuk menentukan strategi pencarian elemen (seperti ID, nama, kelas, dll.)
   -  libraries 'from selenium.webdriver.chrome.service import Service as ChromeService' adalah untuk Mengimpor Service dari Selenium dan menginisialisasi layanan untuk ChromeDriver.
   -  libraries 'from selenium.webdriver.chrome.options import Options' adalah untuk Mengimpor Options untuk mengatur parameter tambahan atau opsi saat menjalankan Chrome.
   -  libraries 'from webdriver_manager.chrome import ChromeDriverManager' adalah libraries yng bertugas untuk Mengimpor 'ChromeDriverManager' dari 'webdriver_manager', yang secara otomatis mengelola versi ChromeDriver yang sesuai.
   -  libraries 'import time' Mengimpor modul time untuk menggunakan fungsi seperti sleep yang memberikan waktu tunggu.

   // Setting opsi browser
      - chrome_options = Options()
   // buka browser dengan fullscreen/maximized
      - chrome_options.add_argument("--start-maximized")  
      
    // agar webdriver bisa mengendalikan browser chrome
      - driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
      
      try
    // Buka url yang sudah disediakan
      - driver.get("https://www.saucedemo.com/v1/index.html")

    // Menunggu membuka website sampai memuat dengan sepenuhnya
      - time.sleep(2)

    /// Mencari element dengan id "user-name" dan "password" kemudian disimpan pada "username" dan "password"
      - username = driver.find_element(By.ID, "user-name")
      - password = driver.find_element(By.ID, "password")

    // Lalu memasukkan username="standard_user" dan password="secret_sauce"
    // username bisa menggunakan "problem_user", "performance_glitch_user","performance_glitch_user"
      - username.send_keys("standard_user")
      - password.send_keys("secret_sauce")

    // cari button dan klik button
      - login_button = driver.find_element(By.ID, "login-button")
      - login_button.click()

    // Menunggu 5 detik sampai web berhasil memuat secara sepenuhnya/sukses
      - time.sleep(5)

    // Mengecek apakah pada url berhasil mengarah ke inventory.html, jika ya maka muncul "Login succesful!" jika tidak "login failed"
      - if "inventory.html" in driver.current_url:
      - print("Login successful!")
      - else:
      - print("Login failed.")

      
      - finally:
    // Menutup browser
      - driver.quit()



7.  Jalankan script file dengan cara "python saucedemo_automation.py"
