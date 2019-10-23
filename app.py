#initializari

nr_cuv = [] #array cu numar cuvinte
cuv_cu = [] #array cuvinte cunoscute
cuv_ne = [] #array cuvinte necunoscuteCBDPRLFMNSTV
vocale='EAOIU'
consoane='BCDFGHLMNPRSTVJKQWXYZ'
consoane_uz='CBDPRLFMNTSV'
consoane_neuz='GHJK'
consoane_neneuz='XZYQW'

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
    if(cuv_ne[n][i-1] in vocale):
        for consoana in consoane_uz:
            if(consoana==cuv_cu[n][i]):
                return(consoana)
        for vocala in vocale:
            if(vocala==cuv_cu[n][i]):
                return(vocala)
        for consoana in consoane_neuz:
            if(consoana==cuv_cu[n][i]):
                return(consoana)
        for consoana in consoane_neneuz:
            if(consoana==cuv_cu[n][i]):
                return(consoana)
    else:
        for vocala in vocale:
            if(vocala==cuv_cu[n][i]):
                return(vocala)
        for consoana in consoane_uz:
            if(consoana==cuv_cu[n][i]):
                return(consoana)
        for consoana in consoane_neuz:
            if(consoana==cuv_cu[n][i]):
                return(consoana)
        for consoana in consoane_neneuz:
            if(consoana==cuv_cu[n][i]):
                return(consoana)

def numar_incercari_lit(i,n):
    nr_incercari = 0
    if(cuv_ne[n][i-1] in vocale):
        for consoana in consoane_uz:
            if(consoana==cuv_cu[n][i]):
                nr_incercari+=1
                return(nr_incercari)
            nr_incercari+=1
        for vocala in vocale:
            if(vocala==cuv_cu[n][i]):
                nr_incercari+=1
                return(nr_incercari)
            nr_incercari+=1
        for consoana in consoane_neuz:
            if(consoana==cuv_cu[n][i]):
                nr_incercari+=1
                return(nr_incercari)
            nr_incercari+=1
        for consoana in consoane_neneuz:
            if(consoana==cuv_cu[n][i]):
                nr_incercari+=1
                return(nr_incercari)
            nr_incercari+=1
    else:
        for vocala in vocale:
            if(vocala==cuv_cu[n][i]):
                nr_incercari+=1
                return(nr_incercari)
            nr_incercari+=1
        for consoana in consoane_uz:
            if(consoana==cuv_cu[n][i]):
                nr_incercari+=1
                return(nr_incercari)
            nr_incercari+=1
        for consoana in consoane_neuz:
            if(consoana==cuv_cu[n][i]):
                nr_incercari+=1
                return(nr_incercari)
            nr_incercari+=1
        for consoana in consoane_neneuz:
            if(consoana==cuv_cu[n][i]):
                nr_incercari+=1
                return(nr_incercari)
            nr_incercari+=1

#rezolvarea cuvintelor si afisearea lor cat si a numarului de incercari necesare

numar_total_incercari = 0
numar = 0
for cuv in cuv_ne:
    index = 0
    nr_ic_cuv = 0
    print(cuv_ne[numar])
    for lit in cuv:
            if lit == '*':
                new_lit = verificare_lit(index, numar)
                nr_ic_lit = numar_incercari_lit(index, numar)
                list_cuv_ne = list(cuv_ne[numar])
                list_cuv_ne[index] = new_lit
                cuv_ne[numar] = "".join(map(str, list_cuv_ne))
            index += 1
            nr_ic_cuv=nr_ic_cuv + nr_ic_lit
    print('incercari cuv:',nr_ic_cuv)
    print(cuv_cu[numar])
    print('\n')
    numar_total_incercari = numar_total_incercari + (int(nr_ic_cuv))
    numar+=1
print('Numar total de incercari:',numar_total_incercari)

