
import requests
import os
import time
def generate_csv_filenames(ticker_file = 'ticker_list.txt',output_directory='wse_stocks_csv/'):
    # Inicjalizacja listy do przechowywania nazw plików CSV
    csv_files = []

    # Inicjalizacja listy do przechowywania wczytanych linii
    lines = []

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Otwarcie pliku i odczytanie zawartości linia po linii
    with open(ticker_file, 'r') as file:
        for line in file:
            # Usunięcie białych znaków z początku i końca linii, a następnie dodanie do listy
            lines.append(line.strip())
            csv_files.append(line.strip() + ".csv")

    # Sprawdzenie daty modyfikacji najstarszego pliku
    min_mtime = time.time()  # Ustawienie na obecny czas jako wartość początkową
    for filename in os.listdir(output_directory):
        file_path = os.path.join(output_directory, filename)
        if os.path.isfile(file_path):
            mtime = os.path.getmtime(file_path)
            min_mtime = min(min_mtime, mtime)

    time_difference = time.time() - min_mtime
    if time_difference > 18 * 360:  # 18 godzin w sekundach
        for line in lines:
            output_filename = output_directory + line + ".csv"

            ticker_url  = "https://stooq.com/q/d/l/?s=" + line + "&i=d"

            response = requests.get(ticker_url)

            # Sprawdzenie, czy żądanie było udane (status code 200 oznacza sukces)
            if response.status_code == 200:
                # Otwórz plik w trybie binarnym i zapisz w nim zawartość odpowiedzi
                with open(output_filename, 'wb') as output_file:
                    output_file.write(response.content)
    else:
        print("Pobieranie pominięte, ostatnie pobranie miało miejsce mniej niż 18 godzin temu.")
    print(csv_files)

    return csv_files
