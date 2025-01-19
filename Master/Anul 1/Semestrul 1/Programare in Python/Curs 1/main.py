'''
x = 2
y = 3.5
z = 4
print(x,y, sep="->")
print(x,y, end=" ")
print(z)
print(F"x = {x} y={y}")
print(F"x+y = {x+y}")
print("Tipul var x", type(x))
print("Tipul var y", type(y))
x="sir"
print("Tipul var x", type(x))
'''

'''
x = 2500
print(x)
print("Adresa de memorie a variabilei x", id(x))
y = x
print("Adresa de memorie a variabilei y", id(y))
y=y+100
print("Adresa de memorie a variabilei y", id(y))
x = 10
print("Tipul de data", type(x))
x = x/3
print("Tipul de data", type(x))
'''

'''
x = input("Introduceti anul nasterii ")
print("x=", x)
'''

'''
x = input("x = ")
y = input("y = ")
print("x=", type(x))
print("y=", type(x))
print(f"x + y = {x+y}")
'''

'''
x = int(input("x = "))
y = float(input("y = "))
print("x=", type(x))
print("y=", type(x))
print(f"x + y = {x+y}")
'''

'''
y = 3
x = 3
print(x>y)

x = "python"
c = "z"
print(c in x)

print(1.1+2.2)
print(1.1 + 2.2 == 3.3)

print(1.1+2.2 - 3.3<1e-9)

print(100 and "test")

# x = y = z = 3

x = 3
y = 4
aux = x
x = y
y = aux

print("x=", x, "y=", y)
'''

'''
x = int(input("x="))
y = int(input("y="))
maxim = x
if x<y:
    maxim = y
else:
    maxim = x
print("max = ", maxim)
'''

'''
#calculeaza valoarea abssoluta(modul) a unui numar dat
# a = 7 -> val = 7
# a= -7 -> val = 7

x = int(input("x="))
if x<0:
    x=-x
print("x = ", x)

#print(abs(x))
'''

'''
# [a,b], x -> care verifica daca x se afla interval
# [1,28], x=10
a = int(input("a="))
b = int(input("b="))
x = int(input("c="))

if a<=x<=b:
    print(x, "apartine", "[", a, ",", b, "]")
else:
    print(x, "nu apartine", "[", a, ",", b, "]")

a = int(input("a="))
if a > 0:
    print("Strict pozitiv")
#else:
#    if a==0:
elif a==0:
    print("Nul")
else:
    print("Negativ")
    '''
'''
# citim numere intregi cat timp citim val 0
x = int(input("x="))
k=0
while x!=0:
    x = int(input("x="))
    k = k+1
print("Nr. de elemente nenule ", k)
'''

'''
sir = "python"
for c in sir:
    print(c, end=" ")
'''
'''
lista = [1, 2, 3, 4]

for x in lista:
    if x%2==0:
        print(x)
'''

'''
for x in range(1, 11):
    if x%2==0:
        continue
    print(x, end = " ")
'''

'''
s = 0
while True:
    x = int(input("x ="))
    if x==0:
        break
    s += x
print("Suma: ", s)
'''

'''
#input n - nr de elemente
#cele n numere
n = int(input("n="))
for i in range(n):
    x = int(input("x="))
    if x<0:
        print("A fost citit un nr negativ")
        break
else:
    print("Toate elementele sunt pozitive")
'''
