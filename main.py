
import pandas as pd
import os
import fnmatch

dir_name = "wse_stocks/"

txt_files = fnmatch.filter(os.listdir(dir_name), '*.txt')

for i in range(len(txt_files)):
    txt_files[i] = dir_name + txt_files[i]

csv_files = txt_files.copy()

for i in range(len(txt_files)):
    csv_files[i] = txt_files[i].replace('.txt', '.csv')
    delete_list = ["<", ">"]
    with open(txt_files[i]) as fin, open(csv_files[i], "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
            fout.write(line)

#data = pd.read_csv(csv_files[0])
#print(data.columns)
#print(data.TICKER)