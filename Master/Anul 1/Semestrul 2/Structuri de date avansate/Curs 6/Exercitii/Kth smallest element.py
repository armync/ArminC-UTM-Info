# https://www.geeksforgeeks.org/kth-smallest-largest-element-in-unsorted-array/
import heapq

# lista de valori
L = [100, 70, 56, 14, 33, 77, 111, 12, 3, 22, 88, 220, 45, 66, 133, 20, 99]
# caut cele mai mari k valori
k = 3

# Varianta 1 - sortarea crescatoare a listei si extragerea ultimelor k elemente
# Complexitate: O(n*log2(n) + k) ~ O(n*log2(n))
L.sort()
print(f"Cele mai mari {k} elemente: {L[-k:]}")


# Varianta 2 - creez un Max-Heap din lista si apoi extrag de k ori maximul din Max-Heap
# Complexitate: O(n + k*log2(n)) ~ O(n) daca avem k << n
L = [100, 70, 56, 14, 33, 77, 111, 12, 3, 22, 88, 220, 45, 66, 133, 20, 99]
Laux = [-x for x in L]
k = 3

heapq.heapify(Laux)
print(f"\nCele mai mari {k} elemente:", end = " ")
for i in range(k):
    maxim = heapq.heappop(Laux)
    print(-maxim, end=" ")


# Varianta 3 - creez un Min-Heap din primele k valori din lista
# si apoi compar fiecare valoare ramasa in lista cu minimul din Min-Heap.
# Daca valoarea curenta din lista este mai mare decat minimul din Min-Heap,
# atunci extrag valoarea minima din Min-Heap si inserez valoarea curenta din lista
# Complexitate: O(k + (n-k)*log2(k)) ~ O(k + n - k) ~ O(n) indiferent de valoarea k

L = [100, 70, 56, 14, 33, 77, 111, 12, 3, 22, 88, 220, 45, 66, 133, 20, 99]
k = 3

min_heap = L[:k]
heapq.heapify(min_heap)
for element in L[k:]:
    if element >= min_heap[0]:
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, element)

print(f"\n\nCele mai mari {k} elemente: {min_heap}")