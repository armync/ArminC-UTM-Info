L = [1, 3, 6, 8, 9, "Ana", [1, 2, 3]]
print(L)

L = [x+1 for x in range(20)]
print(L)
L = [x**2 if x%2==0 else -x**2 for x in range(20)]
print(L)

'''
# lista din val citite de la tastatura
L = [x for x in input("Valori: ").split()]
print(L)
'''

L = [x for x in range(10,100,10)]
print(L)
print(L[1:4])
del L[2]
print(L)
L[2:3] = []
print(L)

# operatori de relatie
L1 = [1, 2, 3, 10]
L2 = [1, 2, 4, "Ana"]
print(L1<L2)

''' error
L1 = [1, 2, 4, 10]
L2 = [1, 2, 4, "Ana"]
print(L1<L2)
'''

L1 = [1, 2, 4, 10]
L2 = [1, 2, 4, "Ana"]
print(L1==L2)

print(len([10,20,30, [10,20]]))

L=[-1,20,0,-4,100]
print(L)

L =[[-1,20],[0,-4],[100],[3,10,60,1,5,7]]
print(max(L))

L = [-1,20,0,-4,100]
print(sum(L))
print(sorted(L, reverse= True))

L = [-1,20,0,-4,100,20,8,20]
x = 20
n = L.count(x)
print(n)
L.append([1,4,10])
print(L)
L.extend([1,4,10])
print(L)
L.insert(20,1000)
print(L)
print(L.index(0))
x = 0
'''
if x in L:
    print(L.index(x))
else:
    print(f"val {x} nu se afla in {L}")
'''
try:
    p = L.index(x)
    print(f"val {x} se afla in pozitia {p}")
except ValueError:
    print(f"val {x} nu se afla in {L}")
'''
try:
    p = L.remove(x)
    print(f"val {x} a fost stearsa")
except ValueError:
    print(f"val {x} nu a fost gasita in {L}")
'''

'''
import time

nr_elemente = 500000
start = time.time()
lista = [x for x in range(nr_elemente)]
stop = time.time()
print(" Initializare: ", stop - start, "secunde")

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
print(" Operatorul +=: ", stop - start, "secunde")

start = time.time()
lista = [0] * nr_elemente
for x in range(nr_elemente):
    lista[x] = x
stop = time.time()
print(" Index: ", stop - start, "secunde")

start = time.time()
lista = []
for x in range(nr_elemente):
    lista = lista + [x]
stop = time.time()
print(" Operatorul +: ", stop - start, "secunde")
'''

'''
n = int(input("Numarul de elemente: "))
L = []
for i in range(n):
    x = int(input(f"Element {i+1} "))
    L.append(x)
print(L)
'''

'''
n = int(input("Numarul de elemente: "))
L = [0]*n
for i in range(n):
    L[i] = int(input("Element: "))
print(L)
'''

'''
sir = input("Elementele listei: ")
L = []
for x in sir.split():
    L.append(int(x))
print(L)
'''

'''
# D=[[1,2,3],[4,5,6]]
# 1 2 3
# 4 5 6
# Numarul de liste din lista: 2 (m)
# Numarul de elemente din fiecare lista: 3 (n)
m = int(input("Numar linii:"))
n = int(input("Numar coloane:"))
D=[]
for i in range(m):
    linie = []
    for j in range(n):
        x = int(input(f"D[{i} || {j}]"))
        linie.append(x)
    D.append(linie)
print(D)
'''

A = [1,2,3,4,5,6]
B = A
print(f"Liste initiale \n{A},\n{B}")
A[2] = 50
print(f"Liste modificate \n{A}\n{B}")

A = [1,2,3,4,5,6]
B = A.copy()
print(f"Liste initiale \n{A},\n{B}")
A[2] = 50
print(f"Liste modificate \n{A}\n{B}")

A = [1,2,3, [4, 5, 6]]
B = A.copy()
print(f"Liste initiale \n{A},\n{B}")
A[2] = 50
A[3][1] = 100
print(f"Liste modificate \n{A}\n{B}")

import copy
A = [1,2,3, [4, 5, 6]]
B = copy.deepcopy(A)
print(f"Liste initiale \n{A},\n{B}")
A[2] = 50
A[3][1] = 100
print(f"Liste modificate \n{A}\n{B}")

t = (1)
print(t, type(t))

t = 1, 2, "Ana"
print(t, type(t))

t = tuple("python")
print(t, type(t))

t = tuple(x+1 for x in range(10))
print(t, type(t))

'''
t = tuple(int(x) for x in input().split())
print(t, type(t))
'''

T = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
T = T[:3] + (101,) + T[4:]
print(T)

'''
#tuplu = tuple(x for x in range(10))
n = int(input("Nr elemente "))
lista = []
for i in range(n):
    x = int(input("Element "))
    lista.append(x)
    tuplu = tuple(lista)
print(lista)
'''

t = (1, 2, 3)
x, y, z = t
print("x=",x,"y=",y,"z=",z)

t = (1, 2, 3, 4, 5)
x, *y,z = t
print("x=",x,"y=",y,"z=",z)

t = (131, "Popa", "Ana", "Maria", 9.10)
grupa, *numeprenume, media = t
print(grupa,numeprenume,media)

s = "python"
print(hash(s))

s = 3.14
print(hash(s))

s= "testare"
print(hash(s))

t = "test"
print(hash(t))

t+="are"
print(hash(t))

s = {1,2,3}
print(s, type(s))

s = set()
print(s, type(s))

l = [1,2,3,1,2,3,4,5,6]
s = set(l)
print(s)

s = {x%8 for x in range(100000)}
print(s)

l = {"Ana", "Dana", "Ana"}
print(set(l))

l = {3.4,2.4,3.4,2.4}
print(set(l))

for x in s:
    print(x, end=" ")

S1 = {1,2,3,4,5,100}
S2 = {1,2,4}
print(S2<S1)
S3 = {4,1,2,1,4,4}
print(S3<=S2)