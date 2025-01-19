f = open("sclm.in")
n = int(f.readline())
t = [int(x) for x in f.readline().split()]
f.close()

lmax = [1] * n
succ = [-1] * n
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if t[i] < t[j] and 1 + lmax[j] > lmax[i]:
            lmax[i] = 1 + lmax[j]
            succ[i] = j

g = open("sclm.out", "w")
lmax_subsir = max(lmax)
g.write(str(lmax_subsir) + '\n')

poz_max = lmax.index(lmax_subsir)

while poz_max != -1:
    g.write(str(poz_max + 1) + " ")
    poz_max = succ[poz_max]
g.close()
