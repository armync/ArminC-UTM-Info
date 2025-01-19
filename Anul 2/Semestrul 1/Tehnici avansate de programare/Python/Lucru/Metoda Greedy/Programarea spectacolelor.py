fin = open("spectacole.in")
sp = []
for linie in fin:
    aux = linie.split()
    h = aux[0].split("-")
    t = (h[0], h[1], " ".join(aux[1:]))
    sp.append(t)
fin.close()

sp.sort(key=lambda t: t[1])

solutie = [sp[0]]
for s in sp[1:]:
    if s[0] >= solutie[-1][1]:
        solutie.append(s)

fout = open("spectacole.out", "w")
for s in solutie:
    fout.write(s[0] + "-" + s[1] + " " + s[2] + "\n")
fout.close()









