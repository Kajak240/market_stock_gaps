from selenium import webdriver

# Ścieżka do sterownika przeglądarki (np. dla Chrome)

# Inicjalizacja przeglądarki
driver = webdriver.Chrome()

# Adres URL do otwarcia
url = 'https://example.com'

# Otwórz stronę
driver.get(url)

# Pobierz tytuł strony
page_title = driver.title
print("Tytuł strony:", page_title)

# Zamknij przeglądarkę
driver.quit()