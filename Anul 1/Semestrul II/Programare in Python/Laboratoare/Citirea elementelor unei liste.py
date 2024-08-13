# Varianta 1
# n = int(input("Numarul de elemente din lista: "))
# L = []
# for k in range(n):
#     x = int(input("Valoare: "))
#     L.append(x)
#     # L += [x]
#
# print(f"Lista citita: {L}")

# Varianta 2
# n = int(input("Numarul de elemente din lista: "))
# # L = [0 for x in range(n)]
# L = [0] * n
# for k in range(n):
#     L[k] = int(input("Valoare: "))
#
# print(f"Lista citita: {L}")

# Varianta 3
# linie = input("Elementele listei: ")
# subsiruri = linie.split()
# L = [int(aux) for aux in subsiruri]
# print(f"Lista citita: {L}")

# Varianta 4
L = [int(aux) for aux in input("Elementele listei: ").split()]
print(f"Lista citita: {L}")
