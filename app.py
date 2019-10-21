#initializari
nr_cuv = []
cuv_cu = []
cuv_ne = []
#citire din fisier csv
import csv
with open('cuvinte_de_verificat.csv') as csvfile:
    dateCSV = csv.reader(csvfile, delimiter=';')
    for row in dateCSV:
        nr = row[0]
        ne = row[1]
        cu = row[2]
        nr_cuv.append(nr)
        cuv_cu.append(cu)
        cuv_ne.append(ne)
    print(nr_cuv[1])
    print(cuv_ne[1])
    print(cuv_cu[1])
#functile de verificare,schimbare si afisare cuvant
#introducere numar cuvant si verificare a lui
#git first try

