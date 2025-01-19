# lista companie
vanzari_zilnice = [
    ["2025-01-20", 2500.50],
    ["2025-01-21", 1300.00],
    ["2025-01-23", 1723.12],
    ["2025-01-26", 323.92]
]

prag = float(input("Introdu suma minima pentru filtrare prag: "))

print(f"\nZilele cu vanzari peste {prag} lei: ")
for date in vanzari_zilnice:
    if date[1] > prag:
        print(f'In data de {date[0]}, suma toata incasata a fost: {date[1]} lei')