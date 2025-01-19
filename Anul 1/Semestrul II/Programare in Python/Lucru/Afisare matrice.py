# m = numarul de linii
import random

m = 4
# n = numarul de coloane
n = 17

#  1  2  3  4  5
#  6  7  8  9 10
# 11 12 13 14 15
# M = [[i*n+j+1 for j in range(n)] for i in range(m)]
M = [[random.randint(1, 1000) for j in range(n)] for i in range(m)]
valmax = max([max(linie) for linie in M])
lmax = len(str(valmax)) + 1
print("Matricea: ")
for linie in M:
    for element in linie:
        print(f"{element:{lmax}}", end=" ")
    print()
