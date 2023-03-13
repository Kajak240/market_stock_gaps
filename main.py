
import pandas as pd
from csvParse import *

import calendar


csv_files = csvParser()
pd.options.display.max_rows = 9999 # pozwala na wyswietlanie duzej ilosci wartosci w outpucie (przy pracy na dataframesach)

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