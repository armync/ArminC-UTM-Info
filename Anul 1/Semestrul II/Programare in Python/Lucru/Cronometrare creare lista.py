import time

nr_elemente = 100_000

start = time.time()
lista = [x for x in range(nr_elemente)]
stop = time.time()
print("   Initializare: ", stop - start, "secunde")

start = time.time()
lista = []
for x in range(nr_elemente):
    lista.append(x)
stop = time.time()
print("Metoda append(): ", stop - start, "secunde")

start = time.time()
lista = []
for x in range(nr_elemente):
    lista += [x]
stop = time.time()
print("  Operatorul +=: ", stop - start, "secunde")

start = time.time()
lista = [0 for x in range(nr_elemente)]
for x in range(nr_elemente):
    lista[x] = x
stop = time.time()
print("       Indexare: ", stop - start, "secunde")

start = time.time()
lista = []
for x in range(nr_elemente):
    lista = lista + [x]
stop = time.time()
print("   Operatorul +: ", stop - start, "secunde")

