import os
import fnmatch

def csvParser(txt_dir_name="wse_stocks/", csv_dir_name=None):
    """
    Funkcja csvParser zajmuje się przetwarzaniem plików tekstowych (.txt) zawierających dane giełdowe.
    Usuwa znaki '<' i '>' z pierwszej linii każdego pliku tekstowego, a następnie zapisuje
    zmodyfikowaną pierwszą linię i pozostałe linie do pliku CSV (.csv). Funkcja zwraca listę
    nazw wygenerowanych plików CSV.

    Args:
        txt_dir_name (str, optional): Ścieżka do katalogu zawierającego pliki tekstowe (.txt). Domyślnie "wse_stocks/".
        csv_dir_name (str, optional): Ścieżka do katalogu, gdzie mają być zapisane pliki CSV (.csv).
                                     Domyślnie tworzony jest podkatalog "csv/" w katalogu txt_dir_name, domyślnie "wse_stocks/" .

    Returns:
        List[str]: Lista nazw plików CSV utworzonych przez funkcję.
    """
    # Utwórz katalog wyjściowy, jeśli nie istnieje
    if csv_dir_name is None:
        csv_dir_name = os.path.join(txt_dir_name, "csv/")

    if not os.path.exists(csv_dir_name):
        os.makedirs(csv_dir_name)

    # Zbierz listę plików tekstowych (.txt) wejściowych
    txt_files = fnmatch.filter(os.listdir(txt_dir_name), '*.txt')

    # Generuj listę nazw plików CSV na podstawie plików tekstowych
    csv_files = [file.replace('.txt', '.csv') for file in txt_files]

    # Iteruj po parach plików tekstowych i plików CSV
    for txt_file, csv_file in zip(txt_files, csv_files):
        # Utwórz pełne ścieżki plików wejściowego i wyjściowego
        txt_file_path = os.path.join(txt_dir_name, txt_file)
        csv_file_path = os.path.join(csv_dir_name, csv_file)

        # Otwórz plik tekstowy w trybie tylko do odczytu i wczytaj pierwszą linię
        with open(txt_file_path, 'r') as fin:
            first_line = fin.readline().replace('<', '').replace('>', '')

        # Otwórz plik CSV w trybie do zapisu i zapisz zmodyfikowaną pierwszą linię oraz pozostałe linie
        with open(csv_file_path, 'w+') as fout:
            fout.write(first_line)
            fout.writelines(open(txt_file_path).readlines()[1:])

    # Zwróć listę nazw plików CSV
    return csv_files