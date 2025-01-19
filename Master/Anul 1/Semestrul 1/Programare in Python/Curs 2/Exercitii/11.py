sir = str(input("Care este denumirea/sirul? "))
serie_cuvinte = sir.split() # imparte sirul in cuvinte individuale
acronim = ''.join([cuvant[0].upper() for cuvant in serie_cuvinte])
acronim_sep = '-'.join([cuvant[0].upper() for cuvant in serie_cuvinte])


# join concateneaza toate literele iar '' poate contine sau nu separator intre acronimele finale
# cuvant[0].upper() preia prin parcurgere fiecare prima litera transformand-o in majuscula

print(f"Acronimul este: {acronim}")
print(f"Acronimul separat este: {acronim_sep}")