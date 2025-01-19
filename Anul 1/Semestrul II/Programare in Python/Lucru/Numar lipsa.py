# Fișierul text "numere.txt" conține n-1 numere distincte din mulțimea {1, 2,..., n}.
# Să se afișeze numărul lipsă x.
# Exemple:
# 2, 1, 5, 4 => x = 3
# 2, 3, 5, 4 => x = 1
# 2, 1, 3, 4 => x = 5


import random
import time


# Varianta 1 - complexitate O(n**2), unde n = len(L)
def nr_lipsa_1():
    f = open("numere.txt")
    L = [int(x) for x in f.readline().split()]
    f.close()

    n = len(L) + 1
    for x in range(1, n+1):
        if x not in L:
            print(f"x = {x}")
            break


# Varianta 2 - complexitate O(n*log2(n)), unde n = len(L)
def nr_lipsa_2():
    f = open("numere.txt")
    L = [int(x) for x in f.readline().split()]
    f.close()

    L.sort()

    n = len(L)
    for i in range(0, n):
        if L[i] != i+1:
            x = i+1
            break
    else:
        x = n+1

    print(f"x = {x}")


# Varianta 3 - complexitate O(n), unde n = len(L)
def nr_lipsa_3():
    f = open("numere.txt")
    L = {int(x) for x in f.readline().split()}
    f.close()

    n = len(L) + 1
    for x in range(1, n + 1):
        if x not in L:
            print(f"x = {x}")
            break


# Varianta 4 - complexitate O(n), unde n = len(L)
def nr_lipsa_4():
    f = open("numere.txt")
    L = {int(x) for x in f.readline().split()}
    f.close()

    n = len(L) + 1
    T = {x for x in range(1, n+1)}

    x = T - L
    print("x =", *x)


# Varianta 5 - complexitate O(n), unde n = len(L)
def nr_lipsa_5():
    f = open("numere.txt")
    L = [int(x) for x in f.readline().split()]
    f.close()

    n = len(L) + 1
    x = n*(n+1)//2 - sum(L)
    print(f"x = {x}")


n = 100_000

L = [str(x) for x in range(1, n+1)]
random.shuffle(L)
L.remove(L[random.randint(0, n-1)])

f = open("numere.txt", "w")
f.write(" ".join(L))
f.close()

ti = time.time()
nr_lipsa_1()
tf = time.time() - ti
print(f"Timp de executare pentru varianta 1: {tf:.3f} secunde\n")

ti = time.time()
nr_lipsa_2()
tf = time.time() - ti
print(f"Timp de executare pentru varianta 2: {tf:.3f} secunde\n")

ti = time.time()
nr_lipsa_3()
tf = time.time() - ti
print(f"Timp de executare pentru varianta 3: {tf:.3f} secunde\n")

ti = time.time()
nr_lipsa_4()
tf = time.time() - ti
print(f"Timp de executare pentru varianta 4: {tf:.3f} secunde\n")

ti = time.time()
nr_lipsa_5()
tf = time.time() - ti
print(f"Timp de executare pentru varianta 5: {tf:.3f} secunde")


# aux = L.copy()
# ti = time.time()
# frecvente_2(aux)
# tf = time.time() - ti
# print(f"\nTimp de executare pentru varianta 2: {tf:.3f} secunde")
#
# aux = L.copy()
# ti = time.time()
# frecvente_3(aux)
# tf = time.time() - ti
# print(f"\nTimp de executare pentru varianta 3: {tf:.3f} secunde")
#
# aux = L.copy()
# ti = time.time()
# frecvente_4(aux)
# tf = time.time() - ti
# print(f"\nTimp de executare pentru varianta 4: {tf:.3f} secunde")