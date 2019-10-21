#initializari
nr_cuv = []
cuv_cu = []
cuv_ne = []
cuv_des = []
alfabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
#functile de verificare,schimbare si afisare cuvant
def verificare_lit(i,n):
    for litera in alfabet:
        if(litera==cuv_cu[n][i]):
            return(litera)

#introducere numar cuvant si verificare a lui
numar = input('introduceti numarul cuvantului:')
numar=int(numar)

index = 0
for lit in cuv_ne[numar]:
    if(lit=='*'):
        lit = verificare_lit(index,numar)
        cuv_ne[numar][index]=lit
        print(cuv_ne[numar])
    index +=1
#git first try

