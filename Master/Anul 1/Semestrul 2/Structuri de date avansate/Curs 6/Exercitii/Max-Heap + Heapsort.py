# tablou = tabloul a carui structura de Max-Heap va fi refacuta
# nr_elemente = numarul de elemente din tablou
# index_curent = indexul de la care va incepe procesul de refacere a structurii de Max-Heap
# in jos in arborele binar sau, echivalent, in dreapta in tablou
def max_heapify(tablou, nr_elemente, index_curent):
    # vreau sa gasesc valoarea maxima dintre: valoarea elementului curent,
    # valoarea fiului sau stang si valoarea fiului sau drept
    index_fiu_stang = 2 * index_curent + 1
    index_fiu_drept = 2 * index_curent + 2

    # presupun ca valoarea elementului curent este mai mare decat valorile celor 2 fii
    index_maxim = index_curent

    # compar valoarea elementului curent cu valoarea fiului sau stang, daca acesta exista
    if index_fiu_stang < nr_elemente and tablou[index_fiu_stang] > tablou[index_maxim]:
        index_maxim = index_fiu_stang

    # compar valoarea elementului curent cu valoarea fiului sau drept, daca acesta exista
    if index_fiu_drept < nr_elemente and tablou[index_fiu_drept] > tablou[index_maxim]:
        index_maxim = index_fiu_drept

    # valoarea unuia dintre fii elementului curent este mai mare decat valoarea sa
    if index_maxim != index_curent:
        # interschimb elementul curent cu fiul cu valoare maxima
        tablou[index_curent], tablou[index_maxim] = tablou[index_maxim], tablou[index_curent]
        # refac structura de Max-Heap in subarborele fiului care continea valoarea maxima
        max_heapify(tablou, nr_elemente, index_maxim)


# creeaza un Max-Heap din tabloul respectiv
def makeMaxHeap(tablou):

    nr_elemente = len(tablou)

    # incep procesul de creare a Max-Heap-ului de la ultimul parinte,
    # elementul cu indexul nr_elemente//2 - 1, pana la radacina cu indexul 0
    for index in range(nr_elemente // 2 - 1, -1, -1):
        max_heapify(tablou, nr_elemente, index)


# Metoda de sortare Heapsort - O(n*log2(n))
def Heapsort(tablou):
    # cream Max-Heap-ul initial din elementele tabloului
    makeMaxHeap(tablou)

    # elementul maxim din tablou se afla acum pe prima pozitie, deci:
    # 1) il interschimbam cu ultimul element si
    # 2) refacem structura de Max-Heap a elementelor ramase, pornind din radacina (index 0)
    nr_elemente = len(tablou)
    for index in range(nr_elemente - 1, 0, -1):
        # pasul 1)
        tablou[0], tablou[index] = tablou[index], tablou[0]
        # pasul 2)
        max_heapify(tablou, index, 0)


T = [100, 70, 56, 14, 33, 77, 111, 12, 3, 22, 88, 220, 45, 66, 133, 20, 99]
print(f"Tabloul initial: {T}")
Heapsort(T)
print(f" Tabloul sortat: {T}")