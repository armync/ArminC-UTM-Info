# Queue Data Structure: https://www.geeksforgeeks.org/introduction-to-queue-data-structure-and-algorithm-tutorials/?ref=next_article_top
# Maximum of all subarrays of size K: https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

# P = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13], k = 4 => S = [10, 10, 10, 15, 15, 90, 90]

import time
import random
from collections import deque

# functie care cronometreaza o alta functie
def cronometrare(functie, lista, k):
    t = time.process_time()
    d = functie(lista, k)
    t = time.process_time() - t
    return t


# solutie 1 - O(n*k)
def solutie_1(P, k):
    n = len(P)
    S = []
    for i in range(n-k+1):
        S.append(max(P[i: i+k]))
    # print(S)
    return S


# solutie 2 - O(n)
def solutie_2(P, k):
    n = len(P)
    S = []
    coada = deque()
    for i in range(k):
        while len(coada) > 0 and P[i] >= P[coada[-1]]:
            coada.pop()
        coada.append(i)

    for i in range(k, n):
        S.append(P[coada[0]])

        while len(coada) > 0 and coada[0] <= i-k:
            coada.popleft()

        while len(coada) > 0 and P[i] >= P[coada[-1]]:
            coada.pop()
        coada.append(i)

    S.append(P[coada[0]])
    # print(S)
    return S


nr_elem = 20000
val_max = 100000
L = [random.randint(1, val_max) for k in range(nr_elem)]
k = random.randint(1, nr_elem)

t1 = cronometrare(solutie_1, L, k)
print(f"Timp de executare 1: {t1:.6f} secunde")

t2 = cronometrare(solutie_2, L, k)
print(f"Timp de executare 2: {t2:.6f} secunde")