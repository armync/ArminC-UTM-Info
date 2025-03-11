# https://en.wikipedia.org/wiki/Topological_sorting
# https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

# Algoritmul lui Kahn -> O(nr_varfuri + nr_arce) <= O(nr_varfuri**2)
import graphviz
from collections import deque

fin = open("activitati.txt")
nr_varfuri = int(fin.readline())

g = graphviz.Digraph(format="png")
g.engine = "dot"

for varf in range(1, nr_varfuri+1):
    g.node(str(varf))

lista_succesori = {x: [] for x in range(1, nr_varfuri+1)}
nr_predecesori = [0] * (nr_varfuri + 1)
for linie in fin:
    x, y = [int(v) for v in linie.split()]
    lista_succesori[x].append(y)
    nr_predecesori[y] += 1
    g.edge(str(x), str(y))
fin.close()

g.view()

coada = deque()
for varf in range(1, nr_varfuri + 1):
    if nr_predecesori[varf] == 0:
        coada.append(varf)

sortare_topologica = []
while len(coada) > 0:
    varf_curent = coada.popleft()
    sortare_topologica.append(varf_curent)
    for vecin in lista_succesori[varf_curent]:
        nr_predecesori[vecin] -= 1
        if nr_predecesori[vecin] == 0:
            coada.append(vecin)

if len(sortare_topologica) != nr_varfuri:
    print("Nu exista nicio sortare topologica!")
else:
    print("O sortare topologica: ")
    print(*sortare_topologica)
