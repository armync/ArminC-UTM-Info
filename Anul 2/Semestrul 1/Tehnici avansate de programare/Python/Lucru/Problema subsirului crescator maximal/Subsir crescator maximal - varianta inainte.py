f = open("numere.txt")
t = [int(x) for x in f.readline().split()]
f.close()

n = len(t)

lmax = [1] * n
succ = [-1] * n
for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if t[i] <= t[j] and 1 + lmax[j] > lmax[i]:
            lmax[i] = 1 + lmax[j]
            succ[i] = j

lmax_subsir = max(lmax)
print(f"Un subsir crescator cu lungimea maxima {lmax_subsir} este:")
poz_max = lmax.index(lmax_subsir)
while poz_max != -1:
    print(t[poz_max], end=" ")
    poz_max = succ[poz_max]