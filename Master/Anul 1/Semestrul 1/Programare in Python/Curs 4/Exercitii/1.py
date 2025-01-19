f = open("numere.txt", "r")

lista_multimi = []

for linie in f:
    numere = set([int(i) for i in linie.split()])
    lista_multimi.append(numere)

print(lista_multimi)

f.close()

numere_comune = lista_multimi[0]
for i in range(1,len(lista_multimi)):
    numere_comune &= lista_multimi[i]

f = open("numere_comune.txt", "w")

for numar in numere_comune:
    f.write(str(numar)+" ")

f.close()