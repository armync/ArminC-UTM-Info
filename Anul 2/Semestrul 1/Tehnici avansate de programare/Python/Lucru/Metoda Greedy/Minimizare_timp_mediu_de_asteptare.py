# t = [5, 2, 7, 3, 2, 4, 3]
# L = [(5, "P1"), (2, "P2"),...]
# 5 2 7 3 2 4 3

def afisare(L, msg):
    n = len(L)
    ta = [0] * n
    ta[0] = L[0][0]
    for i in range(1, n):
        ta[i] = ta[i - 1] + L[i][0]

    print()
    print(f"Timpii de asteptare {msg}:", *ta)
    print(f"Timpul mediu de asteptare {msg[:-1]}: {sum(ta) / n:.2f}")


t = [int(x) for x in input("Timpii individuali de servire: ").split()]

L = [(t[i], "P"+str(i+1)) for i in range(len(t))]
afisare(L, "initiali")

L.sort()
afisare(L, "optimi")



