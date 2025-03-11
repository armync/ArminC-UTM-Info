#https://infogenius.ro/algoritmul-lui-lee/
#https://www.pbinfo.ro/probleme/1871/ubuph
#https://www.pbinfo.ro/probleme/1856/taxe2
#https://www.pbinfo.ro/probleme/2390/rj
#https://www.pbinfo.ro/probleme/2167/alee

import sys
from collections import deque

def afisare_matrice(matrice):
    m = len(matrice)
    n = len(matrice[0])
    for i in range(1, m-1):
        for j in range(1, n-1):
            aux = str(matrice[i][j]).rjust(3)
            print(aux, end=" ")
        print()

fin = open("labirint.txt")

nr_linii, nr_coloane = [int(x) for x in fin.readline().split()]

labirint = [[-1] * (nr_coloane+2)]
for linie in range(1, nr_linii+1):
    aux = [-1] + [int(x) for x in fin.readline().split()] + [-1]
    labirint.append(aux)
labirint.append([-1] * (nr_coloane+2))

celula_initiala = tuple([int(x) for x in fin.readline().split()])
celula_finala = tuple([int(x) for x in fin.readline().split()])

fin.close()

print("Labirintul:")
afisare_matrice(labirint)

if labirint[celula_initiala[0]][celula_initiala[1]] == -1:
    print("\nCelula initiala este inaccesibila!")
    sys.exit()

if labirint[celula_finala[0]][celula_finala[1]] == -1:
    print("\nCelula finala este inaccesibila!")
    sys.exit()


coada = deque()
coada.append(celula_initiala)
labirint[celula_initiala[0]][celula_initiala[1]] = 1
while len(coada) > 0 and labirint[celula_finala[0]][celula_finala[1]] == 0:
    celula_curenta = coada.popleft()
    lin_crt = celula_curenta[0]
    col_crt = celula_curenta[1]
    succesori = [(lin_crt-1, col_crt), (lin_crt, col_crt+1), (lin_crt+1, col_crt), (lin_crt, col_crt-1)]
    for celula_noua in succesori:
        if labirint[celula_noua[0]][celula_noua[1]] == 0:
            labirint[celula_noua[0]][celula_noua[1]] = labirint[celula_curenta[0]][celula_curenta[1]] + 1
            coada.append(celula_noua)

print("\nMatricea distantelor:")
afisare_matrice(labirint)

if labirint[celula_finala[0]][celula_finala[1]] == 0:
    print("\nNu exista niciun traseu de la celula initiala la celula finala!")
else:
    l_min = labirint[celula_finala[0]][celula_finala[1]]
    print(f"\nUn traseu cu lungimea minima {l_min} de la celula {celula_initiala} la celula {celula_finala}:")
    celula_curenta = celula_finala
    traseu = []
    while celula_curenta != celula_initiala:
        traseu.append(celula_curenta)
        lin_crt = celula_curenta[0]
        col_crt = celula_curenta[1]
        predecesori = [(lin_crt - 1, col_crt), (lin_crt, col_crt + 1), (lin_crt + 1, col_crt), (lin_crt, col_crt - 1)]
        for celula_noua in predecesori:
            if  labirint[celula_noua[0]][celula_noua[1]] == labirint[celula_curenta[0]][celula_curenta[1]] - 1:
                celula_curenta = celula_noua

traseu.append(celula_initiala)
traseu.reverse()
print(*traseu, sep=" -> ")