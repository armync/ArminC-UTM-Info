p = int(input("Cat costa jucaria dorita de Gigel? "))
s = 0
z = 0

while s < p:
    z += 1
    s = s + int(input(f"Cat depunde Gigel in ziua {z}? "))

if s >= p:
    print(f"Gigel a mai ramas cu {s-p} lei in urma jucariei")
    print(f"Gigel a economisit in medie, {s/z} lei per zi (total {z} zile)")

