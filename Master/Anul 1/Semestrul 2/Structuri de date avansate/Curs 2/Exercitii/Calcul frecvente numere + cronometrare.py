# Program care calculează frecvența fiecărei valori distincte dintr-o listă de numere.

import time
import random
import collections

# Notatie: n = len(lista)

# complexitate: O(n**2)
def numarare_1(lista):
    d = {x: lista.count(x) for x in lista}
    return d

# complexitate: O(n*len(set(lista))
def numarare_2(lista):
    d = {x: lista.count(x) for x in set(lista)}
    return d

# complexitate: O(n*len(set(lista))
def numarare_3(lista):
    d = {}
    for i in range(len(lista) - 1):
        if lista[i] is not None:
            d[lista[i]] = 1
            for j in range(i+1, len(lista)):
                if lista[j] == lista[i]:
                    d[lista[i]] += 1
                    lista[j] = None
    return d


# complexitate: O(n*log2(n))
def numarare_4(lista):
    lista.sort()
    d = {}
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista) and lista[j] == lista[i]:
            j += 1
        d[lista[i]] = j - i
        i = j
    return d


# complexitate: O(n)
def numarare_5(lista):
    d = {}
    for x in lista:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d


# complexitate: O(n)
def numarare_6(lista):
    d = {x: 0 for x in set(lista)}
    for x in lista:
        d[x] += 1
    return d


# complexitate: O(n)
def numarare_7(lista):
    d = collections.defaultdict(int)
    for x in lista:
        d[x] += 1
    return d


# functie care cronometreaza o alta functie
def cronometrare(functie, lista):
    t = time.process_time()
    d = functie(lista)
    t = time.process_time() - t
    return t


nr_elem = 20000
val_max = 10000000
L = [random.randint(1, val_max) for k in range(nr_elem)]

t1 = cronometrare(numarare_1, L)
print(f"Timp de executare 1: {t1:.6f} secunde")

t2 = cronometrare(numarare_2, L)
print(f"Timp de executare 2: {t2:.6f} secunde")

Laux = L.copy()
t3 = cronometrare(numarare_3, Laux)
print(f"Timp de executare 3: {t3:.6f} secunde")

Laux = L.copy()
t4 = cronometrare(numarare_4, Laux)
print(f"Timp de executare 4: {t4:.6f} secunde")

t5 = cronometrare(numarare_5, L)
print(f"Timp de executare 5: {t5:.6f} secunde")

t6 = cronometrare(numarare_6, L)
print(f"Timp de executare 6: {t6:.6f} secunde")

t7 = cronometrare(numarare_7, L)
print(f"Timp de executare 7: {t7:.6f} secunde")