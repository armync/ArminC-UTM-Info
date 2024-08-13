# Se citeste o lista L formata din n numere intregi.
# Sa se afiseze o secventa S avand suma elemetelor maxima.
# Exemple:
# L = [-2, 5, 8, -7, 10, -45, 9, 2] => S = [5, 8, -7, 10]
# L = [-2, -5, -1, -7] => S = [-1]
# L = [2, 5, -1, 7] => S = [2, 5, -1, 7]
import random
import time

# Consideram n = len(L)

# Complexitate: O(n**3)
def varianta_1(L):
    smax = -10**9
    for i in range(len(L)):
        for j in range(i, len(L)):
            scrt = sum(L[i: j+1])
            if scrt > smax:
                smax = scrt
                st = i
                dr = j

    return smax, st, dr


# Complexitate: O(n**2)
def varianta_2(L):
    smax = -10**9
    for i in range(len(L)):
        scrt = 0
        for j in range(i, len(L)):
            scrt += L[j]
            if scrt > smax:
                smax = scrt
                st = i
                dr = j

    return smax, st, dr


# Complexitate: O(n) - algoritmul lui Kadane
def varianta_3(L):
    smax = -10 ** 9
    st_aux = st = dr = 0
    scrt = 0
    for i in range(len(L)):
        scrt += L[i]

        if scrt > smax:
            smax = scrt
            st = st_aux
            dr = i

        if scrt < 0:
            scrt = 0
            st_aux = i + 1

    return smax, st, dr


# L = [-2, 5, 8, -7, 10, -45, 9, 2]
# L = [-2, -5, -1, -7]
# L = [2, 5, -1, 7]

n = 1000
vmin = -1000
vmax = 1000
L = [random.randint(vmin, vmax) for i in range(n)]

start = time.time()
smax = varianta_1(L)
print(f"Suma maxima: {smax[0]}")
print(f"Secventa cu suma maxima: L[{smax[1]}] -> L[{smax[2]}]")
end = time.time()
print(f"Timp de executare varianta 1 -      O(n**3): {(end - start):.3f} secunde")

start = time.time()
smax = varianta_2(L)
print(f"\nSuma maxima: {smax[0]}")
print(f"Secventa cu suma maxima: L[{smax[1]}] -> L[{smax[2]}]")
end = time.time()
print(f"Timp de executare varianta 2 -      O(n**2): {(end - start):.3f} secunde")

start = time.time()
smax = varianta_3(L)
print(f"\nSuma maxima: {smax[0]}")
print(f"Secventa cu suma maxima: L[{smax[1]}] -> L[{smax[2]}]")
end = time.time()
print(f"Timp de executare varianta 3 -      O(n): {(end - start):.3f} secunde")
