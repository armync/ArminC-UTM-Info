#https://en.wikipedia.org/wiki/Topological_sorting
#https://www.geeksforgeeks.org/topological-sorting/

import networkx as nx
import matplotlib.pyplot as plt

def sortare_topologica(graf_la):
    def DFS(varf_curent):
        vizitat[varf_curent] = True
        for varf_adiacent in graf_la[varf_curent]:
            if not vizitat[varf_adiacent]:
                DFS(varf_adiacent)
        sortare.append(varf_curent)

    nr_varfuri = len(graf_la)
    vizitat = [False] * (nr_varfuri + 1)
    sortare = []
    for varf in range(1, nr_varfuri+1):
        if not vizitat[varf]:
            DFS(varf)

    sortare.reverse()
    return sortare


fin = open("activitati.txt")
nr_varfuri = int(fin.readline())
lista_muchii = []
lista_adiacente = {x: [] for x in range(1, nr_varfuri+1)}
for linie in fin:
    x, y = [int(v) for v in linie.split()]
    lista_muchii.append((x, y))
    lista_adiacente[x].append(y)
fin.close()

sortare = sortare_topologica(lista_adiacente)

if len(sortare) != nr_varfuri:
    print("Nu exista nicio sortare topologica a datelor de intrare!")
else:
    print(f"O sortare topologica a datelor de intrare: {sortare}")


G = nx.DiGraph()
G.add_edges_from(lista_muchii)
nx.draw_shell(G, with_labels=True, node_color="yellow", font_color="red", font_weight="bold")
plt.show()

