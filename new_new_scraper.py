from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Otwórz przeglądarkę
driver = webdriver.Chrome()

# Przejdź do strony
driver.get("https://stooq.com/db/")

try:

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p'))
        )
    except Exception as e:
        print(f"Błąd podczas oczekiwania na załadowanie strony: {e}")

    #button_selector = "body > div > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button"
    button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p')

    # Naciśnij przycisk
    button.click()


    # Kliknij 'setting files content'
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '// *[ @ id = "f13"] / a'))
        )
    except Exception as e:
        print(f"Błąd podczas oczekiwania na załadowanie strony: {e}")
    button = driver.find_element(By.XPATH, '// *[ @ id = "f13"] / a')

    button.click()
    time.sleep(5)
    """


    # Kliknij 'deselect all'
    deselect_all_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Deselect All']")))
    deselect_all_button.click()

    # Wybierz opcję 'WSE_Stocks' w kategorii 'Poland'
    wse_stocks_checkbox = driver.find_element(By.XPATH, "//input[@value='WSE_Stocks']")
    wse_stocks_checkbox.click()

    # Kliknij 'save configuration'
    save_config_button = driver.find_element(By.XPATH, "//input[@value='Save Configuration']")
    save_config_button.click()

    # Poczekaj na odświeżenie strony
    time.sleep(5)

    # Znajdź i pobierz najnowszy plik z kolumny 'daily (d)'
    latest_daily_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='daily (d)']/../../following-sibling::tr[1]//a")))
    latest_daily_link.click()
"""
except Exception as e:
    print("Wystąpił błąd:", e)

finally:
    # Zamknij przeglądarkę po zakończeniu
    driver.quit()