# Stack Data Structure: https://www.geeksforgeeks.org/introduction-to-stack-data-structure-and-algorithm-tutorials/
# Stock Span Problem: https://www.geeksforgeeks.org/the-stock-span-problem/
# Stock Span Problem (online algorithm): https://algo.monster/liteproblems/901

# L = [50, 60, 70, 40, 80, 90 60, 80, 100] => S = [1, 2, 3, 1, 5, 6, 1, 2, 9]

import time
import random

# functie care cronometreaza o alta functie
def cronometrare(functie, lista):
    t = time.process_time()
    d = functie(lista)
    t = time.process_time() - t
    return t


# solutie 1 - O(n**2)
def solutie_1(P):
    n = len(P)
    S = [1] * n
    for i in range(1, n):
        j = i - 1
        while j >= 0 and P[j] <= P[i]:
            j -= 1
        if j == -1:
            S[i] = i + 1
        else:
            S[i] = i - j
    return S

# solutie 2 - O(n)
def solutie_2(P):
    n = len(P)
    S = [1] * n
    stiva = [0]
    for i in range(1, n):
        while len(stiva) > 0 and P[stiva[-1]] <= P[i]:
            stiva.pop()

        if len(stiva) == 0:
            S[i] = i + 1
        else:
            S[i] = i - stiva[-1]

        stiva.append(i)

    return S


nr_elem = 20000
val_max = 1000000000
L = [random.randint(1, val_max) for k in range(nr_elem)]

t1 = cronometrare(solutie_1, L)
print(f"Timp de executare 1: {t1:.6f} secunde")

t2 = cronometrare(solutie_2, L)
print(f"Timp de executare 2: {t2:.6f} secunde")
