s = {1, 2, 2, 2, 1, 1, 4, 3, 1, 1, 2, 4, 4}
print(s)

s = set("exemplare")
print(s)

s = {x % 3 for x in range(1000)}
print(s)

s = {12, 33, 100, 12, 33, 3 ,33, 899}
for x in s:
    print(x)

s = {12, 33, 100, 12, 33, 3 ,33, 899}
print(12 in s)

s = {12, 33, 100, 12, 33, 3 ,33, 899}
t = {33, 899, 12}
print(t < s)

A = {1, 3, 4, 7}
B = {1, 2, 3, 4, 6, 8}
print("Reuniunea:", A | B) # {1, 2, 3, 4, 6, 7, 8}
print("Intersectia:", A & B) # {1, 3, 4}
print("Diferenta A|B:", A - B) # {7}
print("Diferenta B|A:", B - A) # {8, 2, 6}
print("Diferenta simetrica:", A ^ B) # {2, 6, 7, 8}

print(max(A))
print(sum(B))
print(sorted(B))

A = {1,3,5}
A.add(100)
A.add(1000)

A.update([2000,4000,6000])
print(sorted(A))

A.add("testare")
A.update("testare")
A.discard(300)
print(A)

A = {1, 3, 5}

print (A)

x = 3

try:
    A.remove(x)
    print(f"Valoarea {x} a fost stearsa")
except:
    print(f"Valoarea {x} nu exista in multime")

print(A)

A = {1,3,5}
B = {2,5,4}

#A.add(B)

A = frozenset({1,3,5})
B = frozenset({2,5,4,6})

M = {A,B}

print(M)

T = [100, 200, 777, 300, 7, 25, 10, 500, 60]

L= [100,25,7,700,100,100,25,7,300,10]

for valoare in set(L):
    print(f"Valoarea {valoare} apare de {L.count(valoare)} ori")

d = {"Popa Ion": 9.50, "Popa Ana": 8.75, "Popescu Gheorghe": 9.00}
print(d)

d["Popa Ana"] += 0.50
print(d)

del d["Popa Ion"]
print(d)

d["Ionescu Ion"] = 800
print(d)

d["Georgescu Anca"] = 8.00
print(d)

d["Ionescu Ion"] = 10.00
print(d)

stud = "Piscupescu Maria"
try:
    print(f"{stud} are nota {d[stud]}")
except:
    print(f"{stud} nu exista!")

print(d.get(stud))

import random
#V = [100, 25,300,700,100,100,25,7,300]
V = [random.randint(1,100) for k in range(1000)]

for valoare in set(V):
    print(f"Valoarea {valoare} apare de {V.count(valoare)} ori")

'''
# d = {valoare: frecventa}
d = {valoare: 0 for valoare in set(V)}
for valoare in V:
    if valoare in d:
        d[valoare] += 1

for valoare in d:
    print(f"Valoarea {valoare} apare de {d[valoare]} ori")
'''

dv = {"A": 3, "J": 2, "P": 0}
x = dv.pop("K",-100)
print(x)
print(dv)

L = [("Marinescu Ioana", 152, 9.85),
     ("Constantinescu Ion", 151, 7.70),
     ("Popescu Ion", 151, 9.70),
     ("Filip Anca", 152, 9.70)]

d_grupe = {151: [ ("Constantinescu Ion", 7.70), ("Popescu Ion", 9.70)],
           152: [ ("Marinescu Ioana", 9.85),  ("Filip Anca", 9.70)]}

grupa = 151
nume = "Popescu Ion"
for student in d_grupe[grupa]:
    if student[0] == nume:
        print(f"{nume} -> {student[1]}")

'''
nume_student = "Popescu Ion"

for student in L:
    if student[0] == nume_student:
        print(f"{student[0]} -> {student[2]}")
'''
'''
d_nume = {}
for student in L:
    d[student[0]] = (student[1], student[2])
print(d_nume)
'''