import graphviz


def createDisjointSet(n):
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)

    return parent, rank


def findParent(x, parent):
    if x != parent[x]:
        parent[x] = findParent(parent[x], parent)
    return parent[x]


def unionValues(x, y, parent, rank):
    x_parent = findParent(x, parent)
    y_parent = findParent(y, parent)

    if x_parent != y_parent:
        x_rank = rank[x_parent]
        y_rank = rank[y_parent]
        if x_rank < y_rank:
            parent[x_parent] = y_parent
        elif x_rank > y_rank:
            parent[y_parent] = x_parent
        else:
            parent[x_parent] = y_parent
            rank[y_parent] += 1


f = open("graf_ponderat.txt")
nr_varfuri = int(f.readline())
lista_muchii = []
for linie in f:
    # x, y = extremitatile muchiei
    # p = ponderea muchiei
    x, y, p = [int(k) for k in linie.split()]
    lista_muchii.append((x, y, p))
f.close()

# testam aciclicitatea arborelui partial de cost minim curent considerand parintele unui varf ca fiind
# eticheta componentei conexe din care face parte varful respectiv (adica unul dintre varfurile sale)
# initial, toate varfurile sunt izolate, deci eticheta componentei sale conexe este chiar el
parent, rank = createDisjointSet(nr_varfuri + 1)

# sortam muchiile crescator dupa ponderile/costurile lor
lista_muchii.sort(key=lambda t: t[2])
# lista va contine muchiile arborelui partial de cost minim
muchii_apm = []
# numarul de muchii din arborele partial de cost minim curent
nr_muchii_apm = 0
# indexul muchiei curente
index_muchie_curenta = 0

# arborele partial de cost minim trebuie sa fie aciclic si sa aiba nr_varfuri-1 muchii
while nr_muchii_apm < nr_varfuri - 1:
    x, y, p = lista_muchii[index_muchie_curenta]
    parent_x = findParent(x, parent)
    parent_y = findParent(y, parent)
    # daca muchia curenta nu are extremitatile in aceeasi componenta curenta,
    # atunci o putem adauga la arborele partial de cost minim curent deoarece
    # nu formeaza cicluri cu muchiile din arborele partial de cost minim curent
    if parent_x != parent_y:
        muchii_apm.append((x, y, p))
        nr_muchii_apm += 1
        unionValues(parent_x, parent_y, parent, rank)
    index_muchie_curenta += 1


g = graphviz.Graph(format="png")
g.engine = "dot"

for varf in range(1, nr_varfuri+1):
    g.node(str(varf))

for muchie in lista_muchii:
    if muchie in muchii_apm:
        g.edge(str(muchie[0]), str(muchie[1]), str(muchie[2]), color = "red")
    else:
        g.edge(str(muchie[0]), str(muchie[1]), str(muchie[2]), color="black")

g.view()
