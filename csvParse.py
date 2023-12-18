import os
import fnmatch

# usage poniższej funkcji:  funkcja przynajmniej póki co nie przyjmuje argumentów, ale nieglupim by było dodać jako parametr chociazby nazwe pliku, jezeli pusta to wszystkie?
# tak czy inaczej,

def csvParser():
    #TODO: gdyby utworzyc plik przechowujacy najwyzsza dotychczas przeladowana date mozna by ograniczyc ilosc przeladowywan plikow (a moze i zrobić incrementa?)
    txt_dir_name = "wse_stocks/"

    csv_dir_name = txt_dir_name + "csv/"

    if not os.path.exists(csv_dir_name):
        os.makedirs(csv_dir_name)

    txt_files = fnmatch.filter(os.listdir(txt_dir_name), '*.txt') # tworzy zmienna z nazwami wszystkich plikow .txt
    csv_files = fnmatch.filter(os.listdir(csv_dir_name), '*.csv') # tworzy zmienna z nazwami wszystkich plikow .csv

    if len(csv_files) != len(txt_files):

        csv_files = txt_files.copy()

        delete_list = ["<", ">"]  # znaki do usuniecia z zawartosci pliku

        for i in range(len(txt_files)):

            csv_files[i] = txt_files[i].replace('.txt', '.csv')  # modyfikuje nazwe pliku w kopii z .txt na .csv

            txt_files[i] = txt_dir_name + txt_files[i] # do kazdego elementu listy z nazwa pliku dodaje sciezke wzgledna (wse_stocks/nazwa_pliku.txt)
            csv_files[i] = csv_dir_name + csv_files[i] # do kazdego elementu listy z nazwa pliku dodaje sciezke wzgledna (wse_stocks/nazwa_pliku.txt)
            # do cipy to jest, mozna by tylko z jednej linijki usuwac te znaki, i tylko na niej wywolac funkcje replace
            with open(txt_files[i]) as fin, open(csv_files[i], "w+") as fout: # petla przechodzi przez wszystkie pliki txt i tworzy pliki .csv
                for line in fin:
                    for word in delete_list:
                        line = line.replace(word, "") # usuwa znaki do usuniecia z kazdego slowa w linijce w pliku
                    fout.write(line) # zapisuje przetwarzana linijke do pliku .csv
    else:
        for i in range(len(csv_files)):
            csv_files[i] = csv_dir_name + csv_files[i]  # do kazdego elementu listy z nazwa pliku dodaje sciezke wzgledna (wse_stocks/nazwa_pliku.txt)
    return csv_files
