import queue

# # Varianta 1 - țevile se sudează în ordinea dată - GRESITA!!!
#
# L = [50, 20, 100, 60, 40, 20, 70, 10, 80, 100, 90]
# total = 0
# while len(L) > 1:
#     suma = L[0] + L[1]
#     total += suma
#     L.pop(0)
#     L.pop(0)
#     L.insert(0, suma)
#
# print(f"Cost total initial: {total}\n")
#
# # Varianta 2 - la fiecare pas se sudeaza cele mai scurte doua tevi
# # Complexitate: O(n * n * log2(n))
# L = [50, 20, 100, 60, 40, 20, 70, 10, 80, 100, 90]
# total = 0
# while len(L) > 1:
#     L.sort()
#     suma = L[0] + L[1]
#     total += suma
#     L.pop(0)
#     L.pop(0)
#     L.insert(0, suma)
#
# print(f"Cost total minim: {total}\n")

# Varianta 3 - se utilizeaza un Min-Heap pentru a extrage cele doua tevi cu lungime minima
# cu o complexitate optima de O(log2(n))
# Complexitate: O(...)
tevi = [50, 20, 100, 60, 40, 20, 70, 10, 80, 100, 90]

# creeze un Min-Heap din lungimile tevilor
pq = queue.PriorityQueue()
for index, valoare in enumerate(tevi):
    pq.put((valoare, f"T_{str(index)}"))

total = 0
nr_teava_noua = len(tevi)
while pq.qsize() > 1:
    # extrag cele doua tevi cu lungimi minime
    minim_1 = pq.get()
    minim_2 = pq.get()

    # adaug la costul total suma lungimilor lor
    suma = minim_1[0] + minim_2[0]
    total = total + suma

    teava_noua = f"T_{nr_teava_noua}"
    nr_teava_noua += 1
    print(f"Sudam tevile {minim_1[1]} si {minim_2[1]} si obtinem teava {teava_noua} cu lungimea {suma}")

    # reintroduc in coada cu prioritati lungimea tevii obtinuta
    # prin sudarea celor doua tevi cu lungimi minime
    pq.put((suma, teava_noua))

print(f"Cost total minim: {total}\n")




