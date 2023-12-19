import requests
# Inicjalizacja listy do przechowywania wczytanych linii
lines = []

# Otwarcie pliku i odczytanie zawartości linia po linii
with open('ticker_list.txt', 'r') as file:
    for line in file:
        # Usunięcie białych znaków z początku i końca linii, a następnie dodanie do listy
        lines.append(line.strip())


# Wyświetlenie wczytanych linii
for line in lines:
    output_filename = line + ".csv"
    ticker_url  = "https://stooq.com/q/d/l/?s=" + line + "&i=d"

    response = requests.get(ticker_url)

    # Sprawdzenie, czy żądanie było udane (status code 200 oznacza sukces)
    if response.status_code == 200:
        # Otwórz plik w trybie binarnym i zapisz w nim zawartość odpowiedzi
        with open(output_filename, 'wb') as output_file:
            output_file.write(response.content)
        print(f"Pobrano plik jako {output_filename}")
    else:
        print(f"Błąd podczas pobierania pliku. Kod statusu: {response.status_code}")