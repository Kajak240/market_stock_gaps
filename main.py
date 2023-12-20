"""wraz z moim kolegą kamilem który ma ksywe freeku bylsimy ostatnio w tatrach i bardzo dobrze to wspominam"""

import os
import pandas as pd
import numpy as np
from new_scraper import generate_csv_filenames
import multiprocessing

def find_price_gaps(data):
    """
    Znajduje luki w trendzie spadkowym na podstawie danych giełdowych.

    Args:
        data (pd.DataFrame): DataFrame zawierający dane giełdowe.

    Returns:
        pd.DataFrame: DataFrame zawierający informacje o lukach w trendzie spadkowym.
    """
    gaps = pd.DataFrame(columns=['IndexOfDate', 'Date', 'GapHigh', 'GapLow', 'MinPrice'])

    for i in range(1, len(data.index)):
        gap_high = data['LOW'].values[i - 1]
        gap_low = data['HIGH'].values[i]
        if gap_low < gap_high:
            new_gap = [i, str(data['DATE'].values[i]), gap_high, gap_low, gap_low]
            gaps.loc[len(gaps)] = new_gap

    return gaps

def process_gaps(gaps, data):
    """
    Przetwarza znalezione luki w trendzie spadkowym.

    Args:
        gaps (pd.DataFrame): DataFrame zawierający informacje o lukach.
        data (pd.DataFrame): DataFrame zawierający dane giełdowe.

    Returns:
        pd.DataFrame: DataFrame zawierający przetworzone informacje o lukach.
    """
    gaps["GapTouchDate"] = ""
    gaps["GapClosureDate"] = ""
    gaps["DaysToClose"] = np.nan

    for i in range(len(gaps)):
        for j in range(gaps['IndexOfDate'].values[i] + 1, len(data.index)):
            if data['HIGH'].values[j] >= gaps['GapHigh'].values[i]:
                gaps['GapClosureDate'].values[i] = data['DATE'].values[j]
                gaps['DaysToClose'].values[i] = int(j - gaps['IndexOfDate'].values[i])
                gaps['GapTouchDate'].values[i] = data['DATE'].values[j]
                break
            elif data['HIGH'].values[j] >= gaps['GapLow'].values[i] and gaps['GapTouchDate'].values[i] == '':
                gaps['GapTouchDate'].values[i] = data['DATE'].values[j]
            elif data['LOW'].values[j] <= gaps['MinPrice'].values[i]:
                gaps['MinPrice'].values[i] = data['LOW'].values[j]

    return gaps

def process_file_and_save(csv_file):
    try:

        data = pd.read_csv("wse_stocks_csv/" + csv_file)

    except pd.errors.EmptyDataError:
        print(f"Empty file: {csv_file}")
    except pd.errors.ParserError:
        print(f"Error parsing CSV file: {csv_file}")

    except Exception as e:
        print(f"Error reading CSV file: {csv_file}")
        print(f"Error details: {e}")

    try:
        # Znajdź luki w trendzie spadkowym
        gaps = find_price_gaps(data)

        # Przetwórz znalezione luki
        processed_gaps = process_gaps(gaps, data)

        # Filtrowanie luki, które nie zostały dotknięte
        nullList = ['', None]
        filtered_gaps = processed_gaps[processed_gaps['GapTouchDate'].isin(nullList)]

    except Exception as e:
        print(f"Error processing data for file: {csv_file}")
        print(f"Error details: {e}")
        # Zapisz przetworzone luki do pliku CSV

    output_file = 'gaps/' + csv_file[:-4] + '_gaps.csv'
    filtered_gaps.to_csv(output_file)



if __name__ == "__main__":
    # Wczytaj dane giełdowe z plików CSV
    csv_files = generate_csv_filenames()
    threadnum = os.cpu_count()

    # Utwórz pulę procesów i zmapuj funkcję process_file_and_save na listę plików
    with multiprocessing.Pool(processes=threadnum) as pool:
        pool.map(process_file_and_save, csv_files)