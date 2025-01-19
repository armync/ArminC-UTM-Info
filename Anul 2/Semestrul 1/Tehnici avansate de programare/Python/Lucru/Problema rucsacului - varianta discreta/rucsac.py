f = open("rucsac.txt")
G = int(f.readline())

greutati = [0]
castiguri = [0]

for line in f:
    l = line.split()
    castiguri.append(int(l[0]))
    greutati.append(int(l[1]))

f.close()

n = len(greutati)-1

cmax = [[0] * (G + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, G + 1):
        if greutati[i] <= j:
            cmax[i][j] = max(cmax[i - 1][j], cmax[i - 1][j - greutati[i]] + castiguri[i])
        else:
            cmax[i][j] = cmax[i - 1][j]


print(f"Castigul maxim: {cmax[n][G]}")

i = n
j = G
while i != 0:
    if cmax[i][j] != cmax[i-1][j]:
        print(f"Obiectul {i}")
        j = j-greutati[i]
    i -= 1

