nr_cutii = int(input("Numarul de cutii pe raft: "))
cod_cautat = int(input("Cod cutie cautat:"))
pozitie_st = pozitie_dr = None

for k in range(nr_cutii):
    cod_crt = int(input(f"cod cutie {k+1} "))
    if cod_crt == cod_cautat:
        if pozitie_st is None:
            pozitie_st = k+1
        else:
            pozitie_dr = k+1

if pozitie_st is None:
    print(f"Cutia {cod_cautat} nu se afla pe raft")
elif pozitie_dr is None:
    print(f"Cutia {cod_cautat} apare o singura data pe pozitia {pozitie_st}")
else:
    print(f"Cutia {cod_cautat} apare pe pozitia "
          f"{pozitie_st} si pe {pozitie_dr}")