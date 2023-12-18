# Aplikacja Analizująca Wyceny Spółek na Giełdzie

## Opis

Projekt obejmuje aplikację napisaną w języku Python, która wspomaga analizę techniczną wycen spółek notowanych na polskiej giełdzie. Aplikacja korzysta z danych dostępnych w plikach dziennej notacji ASCII ze strony [Stooq](https://stooq.pl/db/h/).

## Struktura Katalogów

- `wse_stocks/`: Katalog zawierający pliki tekstowe (.txt) z danymi giełdowymi.
- `csv/`: Katalog zawierający pliki CSV (.csv) przetworzone przez aplikację.
- `gaps/`: Katalog, w którym zapisywane są pliki CSV zawierające informacje o lukach w trendzie spadkowym.

## Instalacja

1. Sklonuj repozytorium:

    ```bash
    git clone https://github.com/twoj-username/nazwa-repozytorium.git
    ```

2. Przejdź do katalogu projektu:

    ```bash
    cd nazwa-repozytorium
    ```

3. Zainstaluj wymagane biblioteki:

    ```bash
    pip install -r requirements.txt
    ```

## Użycie

1. Upewnij się, że pliki tekstowe z danymi giełdowymi znajdują się w katalogu `wse_stocks/`. Jeżeli nie ma, pobierz plik PL ASCII ze stooq.
2. Uruchom aplikację za pomocą pliku `main.py`:

    ```bash
    python main.py
    ```

3. Aplikacja przetworzy pliki tekstowe na pliki CSV, a następnie zidentyfikuje luki w trendzie spadkowym i zapisze wyniki do katalogu `gaps/`.

