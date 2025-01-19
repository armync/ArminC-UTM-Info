f = open("numere.txt")
t = [int(x) for x in f.readline().split()]
f.close()

n = len(t)

lmax = [1] * n
pred = [-1] * n
for i in range(1, n):
    for j in range(i):
        if t[i] >= t[j] and 1 + lmax[j] > lmax[i]:
            lmax[i] = 1 + lmax[j]
            pred[i] = j

lmax_subsir = max(lmax)
print(f"Un subsir crescator cu lungimea maxima {lmax_subsir} este:")
poz_max = lmax.index(lmax_subsir)
subsir = []
while poz_max != -1:
    subsir.append(t[poz_max])
    poz_max = pred[poz_max]
subsir.reverse()
print(*subsir)