propozitie = str(input('Introdu propozitia: '))

punctuatii = '!?,.;:'
for semn in punctuatii:
    propozitie = propozitie.replace(semn,'')

cuvinte = propozitie.lower().split()

cuvinte_distincte = set(cuvinte)

print(f'Numarul total de cuvinte distincte este: {len(cuvinte_distincte)}')

print('\nLista de cuvinte distincte este:')
for cuvant in sorted(cuvinte_distincte):
    print(f'- {cuvant}')