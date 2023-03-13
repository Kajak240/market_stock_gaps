
import pandas as pd
import numpy as np
from csvParse import *

import calendar


csv_files = csvParser()
pd.options.display.max_rows = 9999 # pozwala na wyswietlanie duzej ilosci wartosci w outpucie (przy pracy na dataframe'ach)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


# luki w trendzie spadkowym (zwiastujace przyszly wzrost)

data = pd.read_csv(csv_files[0]) # zapisanie calej csv w dataframe

gaps = pd.DataFrame(columns=['IndexOfDate','Date','GapHigh','GapLow', 'MinPrice']) # robocza struktura dataframe'u

for i in range (1, len(data.index)): # petla przez cala csvke
    gap_high = data['LOW'].values[i-1] # zapisz najnizsza cene z dnia poprzedniego
    gap_low = data['HIGH'].values[i] # zapisz najwyzsza cene z dnia obecnego
    if gap_low < gap_high: # jezeli najwyzsza jest mniejsza od najnizszej, znaczy ze mamy luke
        new_gap = [i, str(data['DATE'].values[i]), gap_high, gap_low, gap_low] # utworz luke w postaci listy
        gaps.loc[len(gaps)] = new_gap # dopisz luke do dataframe'u z lukami

# nowe kolumny dla dataframe'u z lukami
#gaps["MinPrice"] = np.nan # NaN - utrzyma typ numeryczny
gaps["GapTouchDate"] = ""
gaps["GapClosureDate"] = ""
gaps["DaysToClose"] = np.nan

for i in range(len(gaps)):
    for j in range(gaps['IndexOfDate'].values[i] + 1, len(data.index) - (gaps['IndexOfDate'].values[i] + 1)):  # petla przez cala csvke
        if data['HIGH'].values[j] >= gaps['GapHigh'].values[i]: #domkniecie luki w ciagu jednego dnia
            gaps['GapClosureDate'].values[i] = data['DATE'].values[j]
            gaps['DaysToClose'].values[i] = int(j - gaps['IndexOfDate'].values[i])
            break
        elif data['HIGH'].values[j] >= gaps['GapLow'].values[i] and gaps['GapTouchDate'].values[i] == '':
            gaps['GapTouchDate'].values[i] = data['DATE'].values[j]
        elif data['LOW'].values[j] <= gaps['MinPrice'].values[i]:
            gaps['MinPrice'].values[i] = data['LOW'].values[j]

print(gaps)