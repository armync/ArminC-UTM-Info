propozitie = input("Introdu propozitia: ")

#sterge punctuatiile
punctuatii = '!?,.;:'
for semn in punctuatii:
    propozitie = propozitie.replace(semn, '')

# imparte in cuvinte distincte dar si eliminare dubluri
cuvinte = propozitie.split()

# determina lungimea maxima
lungime_max = max(len(cuvant) for cuvant in cuvinte)
# len(cuvant) calc lungimea fiecarui cuvant
# for cuvant in cuvinte ietereaza fiecare element distinct, preluandu-l sub forma 'cuvant' din lista cuvinte

# cuvintele distincte de lungime maxima
cuv_dist = sorted(set(cuvant for cuvant in cuvinte if len(cuvant) == lungime_max))

# sorted ordoneaza cuvintele alfabetic
# set elimina duplicatele
# generator care introduce pas cu pas in memorie (eficienta)
# if len(cuvant) == lungime_max - pastreaza si filtreaza cuvintele cu lungime maxima
print(f"Cuvintele distincte de lungime maxima ({lungime_max}) sunt:")
print(", ".join(cuv_dist))
