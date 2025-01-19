a = int(input("a = "))
b = int(input("b = "))

print("Alege tipul de operatie: ")
print(" 1. Adunare")
print(" 2. Scadere")
print(" 3. Inmultire")
print(" 4. Impartire")

x = int(input())

if x == 1:
    print(f"Adunarea este: {a + b}")
elif x== 2:
    print(f"Scaderea este: {a - b}")
elif x==3:
    print(f"Inmultirea este: {a * b}")
elif x==4:
    print(f"Impartirea este: {a / b}")
