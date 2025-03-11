import copy

import graphviz

# algoritmul Roy-Floyd-Warshall
def RFW(matrice_ponderi):
    distante = copy.deepcopy(matrice_ponderi)
    nr_varfuri = len(distante) - 1
    for k in range(1, nr_varfuri+1):
        for i in range(1, nr_varfuri + 1):
            for j in range(1, nr_varfuri + 1):
                distante[i][j] = min(distante[i][j], distante[i][k] + distante[k][j])
        # print(f"k = {k}")
        # for linie in distante[1:]:
        #     for element in linie[1:]:
        #         print(f"{element:>5}", sep=" ", end="")
        #     print()
        # print()

    return distante


fin = open("graf_ponderat.txt")

nr_varfuri = int(fin.readline())

g = graphviz.Graph(format="png")
g.engine = "dot"

matrice_ponderi = [[float("inf")] * (nr_varfuri+1) for k in range(1, nr_varfuri+2)]

for k in range(1, nr_varfuri+1):
    matrice_ponderi[k][k] = 0

for linie in fin:
    x, y, p = [int(v) for v in linie.split()]
    matrice_ponderi[x][y] = p
    matrice_ponderi[y][x] = p
    g.edge(str(x), str(y), str(p))

fin.close()

matrice_distante = RFW(matrice_ponderi)

# print(*matrice_distante, sep="\n")

# ex[i] = excentricitatea varfului i
ex = [0] * (nr_varfuri + 1)
for varf in range(1, nr_varfuri + 1):
    ex[varf] = max(matrice_distante[varf][1:])

print(f"Excentricitatile varfurilor: {ex[1:]}")
raza = min(ex[1:])
print(f"Raza grafului: {raza}")
diametrul = max(ex[1:])
print(f"Diametrul grafului: {diametrul}")
centrul = [i for i in range(1, nr_varfuri+1) if ex[i] == raza]
print(f"Centrul grafului: {centrul}")
periferia = [i for i in range(1, nr_varfuri+1) if ex[i] == diametrul]
print(f"Periferia grafului: {periferia}")


# for vf_crt in range(1, nr_varfuri+1):
#     g.node(str(vf_crt), xlabel=f"ex({vf_crt}) = {ex[vf_crt]}", style="filled")

for vf_crt in centrul:
    g.node(str(vf_crt), color="green", style="filled")

for vf_crt in periferia:
    g.node(str(vf_crt), color="red", style="filled")

g.view()