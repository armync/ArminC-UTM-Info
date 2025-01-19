nr_zile = int(input("Numar de zile "))
curs_maxim = 0.0
zi_maxim = 0
fr_curs_maxim = 0

for zi in range(nr_zile):
    curs_crt = float(input(f"Cursul EURO/RON din ziua {zi+1} "))
    if curs_crt > curs_maxim:
        curs_maxim = curs_crt
        zi_maxim = zi+1
        fr_curs_maxim = 1
    elif curs_crt == curs_maxim:
        fr_curs_maxim = fr_curs_maxim +1
print(f"Cursul maxim EURO/RON este {curs_maxim} din ziua {zi_maxim}"
      f" si are frecventa {fr_curs_maxim}")
