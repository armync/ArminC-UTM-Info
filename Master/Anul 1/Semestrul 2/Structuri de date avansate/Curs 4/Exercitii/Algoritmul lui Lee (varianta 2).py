#https://infogenius.ro/algoritmul-lui-lee/
#https://www.pbinfo.ro/probleme/1871/ubuph
#https://www.pbinfo.ro/probleme/1856/taxe2
#https://www.pbinfo.ro/probleme/2390/rj
#https://www.pbinfo.ro/probleme/2167/alee

import sys
from collections import deque

class Punct:
    def __init__(self, lin, col):
        self.linie = lin
        self.coloana = col

    def __str__(self):
        return f"({self.linie}, {self.coloana})"
        # return "(" + str(self.linie) + ", " + str(self.coloana) + ")"

    def __eq__(self, other):
        return self.linie == other.linie and self.coloana == other.coloana


def afisare_matrice(matrice):
    for linie in matrice[1:]:
        for elem in linie[1:]:
            print(f"{elem: >3} ", end="")
        print()


f = open("labirint.in")

nr_linii, nr_coloane = [int(x) for x in f.readline().split()]

labirint = [[-1] * (nr_coloane + 2)]
for i in range(1, nr_linii + 1):
    aux = [-1] + [int(x) for x in f.readline().split()] + [-1]
    labirint.append(aux)
labirint.append([-1] * (nr_coloane + 2))

aux = [int(x) for x in f.readline().split()]
punct_initial = Punct(aux[0], aux[1])
aux = [int(x) for x in f.readline().split()]
punct_final = Punct(aux[0], aux[1])

f.close()

if labirint[punct_initial.linie][punct_initial.coloana] == -1:
    print("Punctul initial este inaccesibil!")
    sys.exit()

if labirint[punct_final.linie][punct_final.coloana] == -1:
    print("Punctul final este inaccesibil!")
    sys.exit()

print("Labirintul:")
afisare_matrice(labirint)

coada = deque()
coada.append(punct_initial)
labirint[punct_initial.linie][punct_initial.coloana] = 1

while len(coada) > 0 and labirint[punct_final.linie][punct_final.coloana] == 0:
    punct_curent = coada.popleft()
    linie_curenta = punct_curent.linie
    coloana_curenta = punct_curent.coloana
    succesori = [Punct(linie_curenta-1, coloana_curenta), Punct(linie_curenta+1, coloana_curenta),
                 Punct(linie_curenta, coloana_curenta-1), Punct(linie_curenta, coloana_curenta+1)]

    for punct_nou in succesori:
        if labirint[punct_nou.linie][punct_nou.coloana] == 0:
            labirint[punct_nou.linie][punct_nou.coloana] = labirint[punct_curent.linie][punct_curent.coloana] + 1
            coada.append(punct_nou)

if labirint[punct_final.linie][punct_final.coloana] == 0:
    print(f"Nu exista niciun drum de la punctul {punct_initial} la punctul {punct_final}!")
else:
    print("\nMatricea distantelor:")
    afisare_matrice(labirint)
    lungime_minima = labirint[punct_final.linie][punct_final.coloana]
    print(f"\nLungimea minima a unui drum de la punctul {punct_initial} la punctul {punct_final} este {lungime_minima}")
    print("\nUn drum de lungime minima: ")
    punct_curent = punct_final
    traseu = []
    while punct_curent != punct_initial:
        traseu.append(punct_curent)
        linie_curenta = punct_curent.linie
        coloana_curenta = punct_curent.coloana
        predecesori = [Punct(linie_curenta - 1, coloana_curenta), Punct(linie_curenta + 1, coloana_curenta),
                       Punct(linie_curenta, coloana_curenta - 1), Punct(linie_curenta, coloana_curenta + 1)]

        for punct_nou in predecesori:
            if labirint[punct_nou.linie][punct_nou.coloana] == labirint[punct_curent.linie][punct_curent.coloana] - 1:
                punct_curent = punct_nou
                break

    traseu.append(punct_initial)
    traseu.reverse()
    print(*traseu, sep=" -> ")
