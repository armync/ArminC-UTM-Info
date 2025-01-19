from queue import PriorityQueue

fin = open("spectacole.txt")
L = []
k = 0
for linie in fin:
    aux = linie.split("-")
    k += 1
    L.append(("S" + str(k), aux[0], aux[1].strip()))
fin.close()

L.sort(key=lambda t: t[1])

sali = PriorityQueue()
sali.put((L[0][2], [L[0]]))
for sp in L[1:]:
    sp_min = sali.get()
    if sp[1] >= sp_min[0]:
        sp_min = (sp[2], ) + (sp_min[1], )
        sp_min[1].append(sp)
    else:
        sali.put((sp[2], [sp]))
    sali.put(sp_min)

fout = open("programari_sali.txt", "w")
k = 0
while not sali.empty():
    k += 1
    fout.write(f"Sala {k}:\n")
    sala_crt = sali.get()
    for sp_crt in sala_crt[1]:
        fout.write(f"\t{sp_crt[0]}   {sp_crt[1]}-{sp_crt[2]}\n")
    fout.write("\n")
fout.close()