# Sa se afiseze pe ce pozitii apare valoarea maxima
# dintr-o lista de numere

# Varianta 1 - calculam maximul si apoi determinam pozitiile pe care apare
# L = [int(x) for x in input("Elementele listei: ").split()]
# vmax = max(L)
# pozmax = []
# for i in range(len(L)):
#     if L[i] == vmax:
#         pozmax.append(i)
# print(f"Pozitiile pe care apare maximul {vmax}: {pozmax}")

# Varianta 2 - calculam maximul si apoi determinam pozitiile pe care apare
# L = [int(x) for x in input("Elementele listei: ").split()]
# vmax = max(L)
# pozmax = [i for i in range(len(L)) if L[i] == vmax]
# print(f"Pozitiile pe care apare maximul {vmax}: {pozmax}")

# Varianta 3 - actualizam dinamic pozitiile maximului
L = [int(x) for x in input("Elementele listei: ").split()]
vmax = L[0]
pozmax = [0]
for i in range(1, len(L)):
    if L[i] > vmax:
        vmax = L[i]
        pozmax = [i]
    elif L[i] == vmax:
        pozmax.append(i)
print(f"Pozitiile pe care apare maximul {vmax}: {pozmax}")
