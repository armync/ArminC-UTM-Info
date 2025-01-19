f = open("monede.txt")
P = int(f.readline())
v = [int(x) for x in f.readline().split()]
f.close()

nrmin = [P+1] * (P+1)
nrmin[0] = 0
pred = [-1] * (P+1)

for i in range(1, P+1):
    for j in range(len(v)):
        if v[j] <= i and 1 + nrmin[i-v[j]] < nrmin[i]:
            nrmin[i] = 1 + nrmin[i-v[j]]
            pred[i] = v[j]

if nrmin[P] == P+1:
    print("Suma nu poate fi platita!")
else:
    print(f"Suma {P} poate fi platita folosind minim {nrmin[P]} monede:")
    i = P
    sol = ""
    while pred[i] != -1:
        sol += str(pred[i]) + "$ + "
        i = i - pred[i]
    print(sol[:-2])