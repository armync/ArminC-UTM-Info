numar = int(input("Numarul:"))

print(f"Descompunerea in factori primi a numarului {numar}")

factor = 2
while numar != 1:
    exponent = 0
    while numar % factor == 0:
        exponent += 1
        numar /= factor
    if exponent > 0:
        print(f"{factor}^{exponent} * ", end="")
    factor += 1

print(f"\b\b \n")

