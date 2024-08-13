# Laborator 6 - problema 3

n = int(input("n = "))
vmax = int("".join(sorted(str(n), reverse=True)))
print(f"Numarul maxim: {vmax}")

vmin = str(vmax)
poz_zero = vmin.find("0")
if poz_zero == -1:
    vmin = int(vmin[::-1])
else:
    vmin = vmin[poz_zero - len(vmin) - 1:] + vmin[0:poz_zero-1][::-1]

print(f"Numarul minim: {vmin}")
