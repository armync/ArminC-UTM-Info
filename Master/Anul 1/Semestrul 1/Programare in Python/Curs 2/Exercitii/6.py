a = int(input("Intervalul [a este: "))
b = int(input("Intervalul b] este: "))

for i in range(a, b+1):
    oglindit = 0
    numar = i

    while numar != 0:
        c = numar % 10
        oglindit = oglindit * 10 + c
        numar = numar // 10 # impartire intreaga (nu float)

    if i == oglindit:
        print(f"Numarul {i} este palindrom")
        break

else: print(f"Nu exista palindrom") # in afara for, doar dupa ce s-a parcurs tot
