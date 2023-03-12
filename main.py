
import pandas as pd

infile = "wse_stocks/1at.txt"
outfile = "wse_stocks/1at.csv"

delete_list = ["<", ">"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)

data = pd.read_csv(outfile)
print(data.columns)
print(data.TICKER)