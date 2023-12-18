import os
import fnmatch
from concurrent.futures import ThreadPoolExecutor

def process_file(txt_file, txt_dir_name, csv_dir_name):
    """
    Funkcja pomocnicza przetwarzająca pojedynczy plik tekstowy na podstawie ścieżek i usuwająca niepotrzebne znaki.
    """
    txt_file_path = os.path.join(txt_dir_name, txt_file)
    csv_file = txt_file.replace('.txt', '.csv')
    csv_file_path = os.path.join(csv_dir_name, csv_file)

    # Otwórz plik tekstowy w trybie tylko do odczytu i wczytaj pierwszą linię
    with open(txt_file_path, 'r') as fin:
        first_line = fin.readline().replace('<', '').replace('>', '')

    # Sprawdź, czy plik tekstowy nie jest pusty
    if not first_line.strip():
        print(f"Skipping empty file: {txt_file}")
        return None

    # Otwórz plik CSV w trybie do zapisu i zapisz zmodyfikowaną pierwszą linię oraz pozostałe linie
    with open(csv_file_path, 'w+') as fout:
        fout.write(first_line)
        fout.writelines(open(txt_file_path).readlines()[1:])

    return csv_file


def csvParser(txt_dir_name="wse_stocks/", csv_dir_name=None, num_threads=os.cpu_count()):
    """
    Funkcja csvParser zajmuje się przetwarzaniem plików tekstowych (.txt) zawierających dane giełdowe.
    Usuwa znaki '<' i '>' z pierwszej linii każdego pliku tekstowego, a następnie zapisuje
    zmodyfikowaną pierwszą linię i pozostałe linie do pliku CSV (.csv). Funkcja korzysta z wielowątkowości
    w celu przyspieszenia przetwarzania.

    Args:
        txt_dir_name (str, optional): Ścieżka do katalogu zawierającego pliki tekstowe (.txt). Domyślnie "wse_stocks/".
        csv_dir_name (str, optional): Ścieżka do katalogu, gdzie mają być zapisane pliki CSV (.csv).
                                     Domyślnie tworzony jest podkatalog "csv/" w katalogu txt_dir_name.
        num_threads (int, optional): Liczba wątków użytych do przetwarzania plików. Domyślnie liczba watkow dostepna w PC.

    Returns:
        List[str]: Lista nazw plików CSV utworzonych przez funkcję.
    """
    if csv_dir_name is None:
        csv_dir_name = os.path.join(txt_dir_name, "csv/")

    if not os.path.exists(csv_dir_name):
        os.makedirs(csv_dir_name)

    # Zbierz listę plików tekstowych (.txt) wejściowych
    txt_files = fnmatch.filter(os.listdir(txt_dir_name), '*.txt')

    # Utwórz ThreadPoolExecutor z określoną liczbą wątków
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Uruchom funkcję process_file dla każdego pliku tekstowego
        results = list(executor.map(process_file, txt_files, [txt_dir_name] * len(txt_files), [csv_dir_name] * len(txt_files)))

    # Usuń None z listy wyników (pliki, które były puste)
    results = [result for result in results if result is not None]

    return results