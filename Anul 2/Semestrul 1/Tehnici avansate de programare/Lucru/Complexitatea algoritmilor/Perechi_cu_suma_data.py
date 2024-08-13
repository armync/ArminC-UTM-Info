# Se citeste o lista L formata din n numere naturale sortate strict crescator
# si un numar natural S. Sa se afiseze toate perechi din lista data
# cu proprietatea ca suma elementelor din pereche este egala cu S.
# Exemplu:
# L = [2, 5, 9, 10, 11, 16, 20, 45, 90]
# S = 21
# Solutie: (5, 16), (10, 11)

import time

# Consideram n = len(L)

# Complexitate: O(n**2)
def varianta_1(L, S):
    sol = []
    for i in range(len(L)):
        if L[i] >= S // 2:
            break
        try:
            p = L[i+1:].index(S-L[i])
            sol.append((L[i], L[p+i+1]))
        except ValueError:
            pass

    return sol

# Complexitate: O(n*log2(n))
def varianta_2(L, S):
    sol = []
    for i in range(len(L)):
        if L[i] >= S // 2:
            break
        st = i+1
        dr = len(L)-1
        while st <= dr:
            mij = (st + dr) // 2
            if L[mij] == S - L[i]:
                sol.append((L[i], L[mij]))
                break
            elif S - L[i] < L[mij]:
                dr = mij - 1
            else:
                st = mij + 1

    return sol


# Complexitate: O(n) - cu memorie suplimentara pentru set
def varianta_3(L, S):
    sol = []
    # Complexitate: O(n)
    valori = set(L)
    for i in range(len(L)):
        if L[i] >= S // 2:
            break
        if S - L[i] in valori:
            sol.append((L[i], S - L[i]))
    return sol


# Complexitate: O(n) - fara memorie suplimentara
def varianta_4(L, S):
    sol = []
    st = 0
    dr = len(L) - 1
    while st < dr:
        if L[st] + L[dr] == S:
            sol.append((L[st], L[dr]))
            st += 1
            dr -= 1
        elif L[st] + L[dr] < S:
            st += 1
        else:
            dr -= 1

    return sol

# L = [2, 5, 9, 10, 11, 16, 20, 45, 90]
# S = 21

n = 1000000
L = [x for x in range(1, n+1)]
S = 900000

start = time.time()
# aux = varianta_1(L, S)
end = time.time()
# print(aux)
print(f"Timp de executare varianta 1 -      O(n**2): {(end - start):.3f} secunde")

start = time.time()
# aux = varianta_2(L, S)
end = time.time()
# print(aux)
print(f"Timp de executare varianta 2 - O(n*log2(n)): {(end - start):.3f} secunde")

start = time.time()
aux = varianta_3(L, S)
end = time.time()
# print(aux)
print(f"Timp de executare varianta 3 -         O(n): {(end - start):.3f} secunde")

start = time.time()
aux = varianta_4(L, S)
end = time.time()
# print(aux)
print(f"Timp de executare varianta 4 -         O(n): {(end - start):.3f} secunde")