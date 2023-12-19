from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from PIL import Image
import pytesseract

import requests

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'


# Inicjalizacja przeglądarki
driver = webdriver.Chrome()

# Adres URL do otwarcia
url = 'https://stooq.pl/db/h/'

# Otwórz stronę
driver.get(url)

# Poczekaj 2 sekundy (możesz dostosować czas oczekiwania)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p'))
    )
except Exception as e:
    print(f"Błąd podczas oczekiwania na załadowanie strony: {e}")


# Zlokalizuj przycisk za pomocą selektora CSS (przykład, dostosuj do swojej strony)
button_selector = "body > div > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button"
button = driver.find_element(By.CSS_SELECTOR, button_selector)

# Naciśnij przycisk
button.click()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[5]/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr[4]/td[3]/a'))
    )
except Exception as e:
    print(f"Błąd podczas oczekiwania na załadowanie strony: {e}")


button_selector = "#t1 > a"
button = driver.find_element(By.CSS_SELECTOR, button_selector)

button.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="cpt_cd"]/img'))
    )
except Exception as e:
    print(f"Błąd podczas oczekiwania na załadowanie strony: {e}")

image_element = driver.find_element(By.XPATH, '//*[@id="cpt_cd"]/img')

image_url = image_element.get_attribute('src')

# Pobierz obrazek za pomocą requests
response = requests.get(image_url)
image_data = BytesIO(response.content)

# Otwórz obrazek przy użyciu PIL
image = Image.open(image_data)

# Zapisz obrazek na dysku
image.save('captcha.jpg')

captcha_image = Image.open('captcha.jpg')

recognized_text = pytesseract.image_to_string(captcha_image)

print(recognized_text)

# Zamknij przeglądarkę
driver.quit()
