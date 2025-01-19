evaluari = []
num_studenti = int(input('Cati studenti sunt? '))

for i in range(num_studenti):
    nota = float(input(f'Introdu evaluarea studentului {i + 1}: '))
    evaluari.append(nota)

prag_excelent = float(input("Introduceti pragul pentru clasificarea 'Excelent': "))
prag_bun = float(input("Introduceti pragul pentru clasificarea 'Bun': "))
prag_suficient = float(input("Introduceti pragul pentru clasificarea 'Suficient': "))

clasificari = []
for notare in evaluari:
    if notare >= prag_excelent:
        clasificari.append("Excelent")
    elif notare >= prag_bun:
        clasificari.append("Bun")
    elif notare >= prag_suficient:
        clasificari.append("Suficient")
    else:
        clasificari.append("Insuficient")

print("\nClasificarile pentru notele introduse: ")


for i, (evaluare, clasificare) in enumerate(zip(evaluari, clasificari), start=1):
    print(f"Studentul {i} cu nota {evaluare} are clasificarea {clasificare}")

# ex. standard -
# evaluari = [9.5, 7.0, 5.2]
# clasificari = ['Excelent', 'Bun', 'Suficient']
#
# zip(): combina doua+ liste intr-un singur tulp
# (9.5, 'Excelent'), (7.0, 'Bun'), (5.2, 'Suficient')
#
# enumerate(): returneaza indexul cat si elementul
# ex. (1, (9.5, 'Excelent')), (2, (7.0, 'Bun')), (3, (5.2, 'Suficient'))
#
# start: index implicit
