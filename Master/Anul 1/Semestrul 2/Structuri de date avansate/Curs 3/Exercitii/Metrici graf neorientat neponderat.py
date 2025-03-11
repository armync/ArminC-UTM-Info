#https://en.wikipedia.org/wiki/Distance_(graph_theory)
#https://staff.fmi.uvt.ro/~mircea.marin/lectures/TGC/rasp3.pdf

import graphviz
from collections import deque


def BFS(graf_la, varf_initial):
    vizitat = set([varf_initial])
    coada = deque([varf_initial])
    nr_varfuri = len(graf_la)
    distante = [0] * (nr_varfuri + 1)
    while len(coada) > 0:
        varf_curent = coada.popleft()
        for varf_adiacent in graf_la[varf_curent]:
            if varf_adiacent not in vizitat:
                distante[varf_adiacent] = distante[varf_curent] + 1
                coada.append(varf_adiacent)
                vizitat.add(varf_adiacent)
    return distante


fin = open("graf.txt")

nr_varfuri = int(fin.readline())

g = graphviz.Graph(format="png")
g.engine = "circo"

for varf in range(1, nr_varfuri+1):
    g.node(str(varf))

lista_adiacenta = {x: [] for x in range(1, nr_varfuri + 1)}
for linie in fin:
    x, y = [int(v) for v in linie.split()]
    lista_adiacenta[x].append(y)
    lista_adiacenta[y].append(x)
    g.edge(str(x), str(y))

fin.close()

# ex[i] = excentricitatea varfului i
ex = [0] * (nr_varfuri + 1)
for varf in range(1, nr_varfuri + 1):
    ex[varf] = max(BFS(lista_adiacenta, varf))

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