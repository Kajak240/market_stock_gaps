
import pandas as pd

import os
import fnmatch
import calendar

pd.options.display.max_rows = 9999 # pozwala na wyswietlanie duzej ilosci wartosci w outpucie (przy pracy na dataframesach)

dir_name = "wse_stocks/"

txt_files = fnmatch.filter(os.listdir(dir_name), '*.txt') # tworzy zmienna z nazwami wszystkich plikow .txt

for i in range(len(txt_files)):
    txt_files[i] = dir_name + txt_files[i] # do kazdego elementu listy z nazwa pliku dodaje sciezke wzgledna (wse_stocks/nazwa_pliku.txt)

csv_files = txt_files.copy() # tworzy kopie 1:1 poprzedniej listy plikow

for i in range(len(txt_files)):
    csv_files[i] = txt_files[i].replace('.txt', '.csv') # modyfikuje nazwe pliku w kopii z .txt na .csv
    delete_list = ["<", ">"] # znaki do usuniecia z zawartosci pliku
    with open(txt_files[i]) as fin, open(csv_files[i], "w+") as fout: # petla przechodzi przez wszystkie pliki txt i tworzy pliki .csv
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "") #usuwa znaki do usuniecia z kazdego slowa w linijce w pliku
            fout.write(line) #zapisuje przetwarzana linijke do pliku .csv

# luki w trendzie spadkowym (zwiastujace przyszly wzrost)
data = pd.read_csv(csv_files[0])

gaps = pd.DataFrame(columns=['DATE','GAPHIGH','GAPLOW'])

for i in range (1, len(data.index)):
    gap_high = data['LOW'].values[i-1]
    gap_low = data['HIGH'].values[i]
    if gap_low < gap_high:
        new_gap = [str(data['DATE'].values[i]), gap_high, gap_low]
        gaps.loc[len(gaps)] = new_gap

print(gaps)