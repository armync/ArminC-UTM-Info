import graphviz
from collections import deque

def citireGraf(nume_fisier):
    fin = open(nume_fisier)
    n = int(fin.readline())
    la = {x: [] for x in range(1, n+1)}
    for linie in fin:
        x, y = [int(v) for v in linie.split()]
        la[x].append(y)
        la[y].append(x)

    fin.close()
    return la


def DFS(graf_la, varf_initial):
    def parcurgere(varf_curent):
        vizitat.add(varf_curent)
        parcurgere_dfs.append(varf_curent)
        for varf_adiacent in graf_la[varf_curent]:
            if varf_adiacent not in vizitat:
                parcurgere(varf_adiacent)

    vizitat = set()
    parcurgere_dfs = []
    parcurgere(varf_initial)
    return parcurgere_dfs


def DFS_iterativ(graf_la, varf_initial):
    nr_varfuri = len(graf_la)
    vizitat = [False] * (nr_varfuri + 1)
    parcurgere_dfs = []
    stiva = deque()
    stiva.append(varf_initial)
    while len(stiva) > 0:
        varf_curent = stiva.pop()
        if not vizitat[varf_curent]:
            parcurgere_dfs.append(varf_curent)
            vizitat[varf_curent] = True
        for varf_adiacent in graf_la[varf_curent]:
            if not vizitat[varf_adiacent]:
                stiva.append(varf_adiacent)

    return parcurgere_dfs


def BFS(graf_la, varf_initial):
    def parcurgere(varf_curent):
        vizitat = set()
        coada = deque()
        coada.append(varf_curent)
        vizitat.add(varf_curent)
        while len(coada) > 0:
            varf_curent = coada.popleft()
            parcurgere_bfs.append(varf_curent)
            for varf_adiacent in graf_la[varf_curent]:
                if varf_adiacent not in vizitat:
                    coada.append(varf_adiacent)
                    vizitat.add(varf_adiacent)

    parcurgere_bfs = []
    parcurgere(varf_initial)
    return parcurgere_bfs


lista_adiacenta = citireGraf("graf.txt")

varf_initial = 1
pdr = DFS(lista_adiacenta, varf_initial)
pdi = DFS_iterativ(lista_adiacenta, varf_initial)
pb = BFS(lista_adiacenta, varf_initial)
print("Lista de adiacenta:", lista_adiacenta)
print(f"Parcurgerea DFS recursiva din varful {varf_initial}: {pdr}")
print(f"Parcurgerea DFS iterativa din varful {varf_initial}: {pdi}")
print(f"Parcurgerea BFS din varful {varf_initial}: {pb}")

g = graphviz.Graph(format="png")
g.engine = "circo"
for varf in lista_adiacenta:
    g.node(str(varf))
    for vecin in lista_adiacenta[varf]:
        if vecin > varf:
            g.edge(str(varf), str(vecin))
g.view()
