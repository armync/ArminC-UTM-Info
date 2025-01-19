n = int(input("Cati studenti sunt? "))
minim = 0
maxim = 25

for i in range(1, n):
    print(f"Ce interval orar are stundetul {i}?")
    # a, b apartin de N, unde a < b
    a = int(input("a = "))
    b = int(input("b = "))

    if a > minim:
        minim = a
    if b < maxim:
        maxim = b

input(f"Intervalul in care toti studentii pot participa este [{minim},{maxim}]")
