f = open("agenda.in", "r")
agenda = {}

for line in f:
    line = line.strip()
    if line:
        line_aux = line.split(",")
        agenda[line_aux[0]] = [numar.strip() for numar in line_aux[1:]]

f.close()
print(agenda)

while True:
    x = input("Introduceti un nume: ")
    if not x:
        break
    print(agenda.get(x, f" {x} nu exista in agenda"))