produse = []
preturi = []
stocuri = []

while True:
    produs = input("\nNumele produsului: ")
    if produs.isdigit():
        break

    pret = float(input("Pretul produsului: "))
    stoc = int(input("Cantitatea produsului: "))

    produse.append(produs)
    preturi.append(pret)
    stocuri.append(stoc)

print('\n Informatii produse:')
print('\n')

for i in range(len(produse)):
    valoare_stoc = preturi[i] * stocuri[i]
    print(f'Produs: {produse[i]}')
    print(f'Pret: {preturi[i]} ron')
    print(f'Stoc: {stocuri[i]}')
    print(f'Valoare totala stoc: {valoare_stoc} ron')
