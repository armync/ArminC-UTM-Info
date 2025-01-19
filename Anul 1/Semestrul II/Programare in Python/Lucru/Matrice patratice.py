# Laborator 6 - problema 4

n = int(input("n = "))

MA = [[i*n+j for j in range(n)] if i % 2 == 0
      else [i*n+j for j in range(n)][::-1] for i in range(n)]
print("\nMatricea a): ")
for linie in MA:
    print(*linie)

MB = [[min(i, j) for j in range(n)] for i in range(n)]
print("Matricea b): ")
for linie in MB:
    print(*linie)

MC = [[abs(i-j) for j in range(n)] for i in range(n)]
print("\nMatricea c): ")
for linie in MC:
    print(*linie)
