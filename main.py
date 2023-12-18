
import pandas as pd
import numpy as np
from csvParse import *

import calendar

#todo: https://stooq.com/t/?i=513 tutaj jest lista tickerow ktora mozna by pobierac  jakims scrapperem?
#todo: jezeli jest tutaj to jest czescia wig20: https://stooq.com/t/?i=532
#todo: jezeli jest tutaj to jest czescia wig40: https://stooq.com/t/?i=533
#todo: jezeli jest tutaj to jest czescia wig80: https://stooq.com/t/?i=533
#todo: reszta to pozostale

csv_files = csvParser()

ticker_names = pd.read_excel('Book.xlsx')

pd.options.display.max_rows = 9999 # pozwala na wyswietlanie duzej ilosci wartosci w outpucie (przy pracy na dataframe'ach)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

# luki w trendzie spadkowym (zwiastujace przyszly wzrost)

# for i in csv_files # wymagana by byla zmiana w linijkach przy czytaniu i zapisywaniu csv
threadnum = len(csv_files) # zlicz ile jest plikow i zapisz ilosc pod katem wielowatkowosci
# for i in range(threadnum) # chyba najlepsza opcja, wtedy wiemy ile utworzyć watkow? jakby tego len
# data = pd.read_csv(csv_files[0]) # zapisanie calej csv w dataframe - wersja jednoplikowa
for k in range(20):
    data = pd.read_csv(csv_files[k])

    gaps = pd.DataFrame(columns=['IndexOfDate', 'Date', 'GapHigh', 'GapLow', 'MinPrice']) # robocza struktura dataframe'u

    for i in range(1, len(data.index)): # petla przez cala csvke
        gap_high = data['LOW'].values[i-1] # zapisz najnizsza cene z dnia poprzedniego
        gap_low = data['HIGH'].values[i] # zapisz najwyzsza cene z dnia obecnego
        if gap_low < gap_high: # jezeli najwyzsza jest mniejsza od najnizszej, znaczy ze mamy luke
            new_gap = [i, str(data['DATE'].values[i]), gap_high, gap_low, gap_low] # utworz luke w postaci listy
            gaps.loc[len(gaps)] = new_gap # dopisz luke do dataframe'u z lukami

    # nowe kolumny dla dataframe'u z lukami

    gaps["GapTouchDate"] = ""
    gaps["GapClosureDate"] = ""
    gaps["DaysToClose"] = np.nan

    for i in range(len(gaps)):
        for j in range(gaps['IndexOfDate'].values[i] + 1, len(data.index)):  # petla przez cala csvke
            if data['HIGH'].values[j] >= gaps['GapHigh'].values[i]: # domkniecie luki w ciagu jednego dnia
                gaps['GapClosureDate'].values[i] = data['DATE'].values[j]
                gaps['DaysToClose'].values[i] = int(j - gaps['IndexOfDate'].values[i])
                gaps['GapTouchDate'].values[i] = data['DATE'].values[j]
                break
            elif data['HIGH'].values[j] >= gaps['GapLow'].values[i] and gaps['GapTouchDate'].values[i] == '':
                gaps['GapTouchDate'].values[i] = data['DATE'].values[j]
            elif data['LOW'].values[j] <= gaps['MinPrice'].values[i]:
                gaps['MinPrice'].values[i] = data['LOW'].values[j]

    # print(gaps)
    nullList = ['', None]
    filtered_gaps = gaps[gaps['GapTouchDate'].isin(nullList)]
    #filtered_gaps.to_csv(csv_files[0][:-4] + '_gaps.csv')
    filtered_gaps.to_csv('gaps/' + csv_files[k][:-4] + '_gaps.csv')