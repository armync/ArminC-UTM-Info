# preordine = r - s - d
from collections import deque


def preordine(varf_curent, arbore):
    if varf_curent != 0:
        # afisez informatia din varful curent
        print(varf_curent, end=" ")
        # reapelez functia pentru fiul stang al varfului curent
        preordine(arbore[0][varf_curent], arbore)
        # reapelez functia pentru fiul drept al varfului curent
        preordine(arbore[1][varf_curent], arbore)


# inordine = s - r - d
def inordine(varf_curent, arbore):
    if varf_curent != 0:
        # reapelez functia pentru fiul stang al varfului curent
        inordine(arbore[0][varf_curent], arbore)
        # afisez informatia din varful curent
        print(varf_curent, end=" ")
        # reapelez functia pentru fiul drept al varfului curent
        inordine(arbore[1][varf_curent], arbore)


# postordine = s - d - R
def postordine(varf_curent, arbore):
    if varf_curent != 0:
        # reapelez functia pentru fiul stang al varfului curent
        postordine(arbore[0][varf_curent], arbore)
        # reapelez functia pentru fiul drept al varfului curent
        postordine(arbore[1][varf_curent], arbore)
        # afisez informatia din varful curent
        print(varf_curent, end=" ")

# parcurgere pe niveluri (bfs)
def parcurgere_niveluri(varf_curent, arbore):
    if varf_curent == 0:
        return []

    coada = deque()
    parcurgere_bfs = []

    coada.append(varf_curent)
    nivel_curent = 0
    while len(coada) > 0:
        lungime_coada = len(coada)
        parcurgere_bfs.append([])

        for k in range(lungime_coada):
            varf_curent = coada.popleft()
            parcurgere_bfs[nivel_curent].append(varf_curent)
            if arbore[0][varf_curent] != 0:
                coada.append(arbore[0][varf_curent])
            if arbore[1][varf_curent] != 0:
                coada.append(arbore[1][varf_curent])

        nivel_curent += 1

    return parcurgere_bfs


# determinarea inaltimii unui arbore binar
def inaltime(varf_curent, arbore):
    if varf_curent == 0:
        return -1

    inaltime_subarbore_stang = inaltime(arbore[0][varf_curent], arbore)
    inaltime_subarbore_drept = inaltime(arbore[1][varf_curent], arbore)
    return 1 + max(inaltime_subarbore_stang, inaltime_subarbore_drept)


# determinarea sumei valorilor din varfurile unui arbore binar
def suma(varf_curent, arbore):
    if varf_curent == 0:
        return 0

    suma_subarbore_stang = suma(arbore[0][varf_curent], arbore)
    suma_subarbore_drept = suma(arbore[1][varf_curent], arbore)
    return varf_curent + suma_subarbore_stang + suma_subarbore_drept


fin = open("arbore_binar.txt")
radacina = int(fin.readline())

linie = fin.readline()
arbore = []
# arbore[0] = fii stangi
arbore.append([0] + [int(x) for x in linie.split()])
linie = fin.readline()
# arbore[1] = fii drepti
arbore.append([0] + [int(x) for x in linie.split()])
# arbore[0][k] = fiul stang al varfului k
# arbore[1][k] = fiul drept al varfului k

print("\nParcurgerea in preordine:")
preordine(radacina, arbore)
print()

print("\nParcurgerea in inordine:")
inordine(radacina, arbore)
print()

print("\nParcurgerea in postordine:")
postordine(radacina, arbore)
print()

print("\nParcurgerea pe niveluri:")
p_bfs = parcurgere_niveluri(radacina, arbore)
print(p_bfs)

h = inaltime(radacina, arbore)
print(f"\nInaltimea arborelui: {h}")

s = suma(radacina, arbore)
print(f"\nSuma valorilor din varfurile arborelui: {s}")



