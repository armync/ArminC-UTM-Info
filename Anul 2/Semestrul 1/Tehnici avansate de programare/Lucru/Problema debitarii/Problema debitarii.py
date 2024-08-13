# parametrii functiei = coordonatele dreptunghiului curent
def arie_maxima(xst_crt, yst_crt, xdr_crt, ydr_crt):
    global xg, yg, xst_max, yst_max, xdr_max, ydr_max

    # pozg = indexul primei gauri din drepuntghiul curent
    # sau -1 daca nu exista nicio gaura in el
    pozg = -1
    for i in range(len(xg)):
        if (xst_crt < xg[i] < xdr_crt) and (yst_crt < yg[i] < ydr_crt):
            pozg = i
            break

    # nu exista nicio gaura in dreptunghiul curent
    if pozg == -1:
        # compar aria dreptunghiului curent cu aria maxima
        if (xdr_crt - xst_crt) * (ydr_crt - yst_crt) > \
           (xdr_max - xst_max) * (ydr_max - yst_max):
            xst_max, yst_max = xst_crt, yst_crt
            xdr_max, ydr_max = xdr_crt, ydr_crt
    else:
        arie_maxima(xst_crt, yst_crt, xg[pozg], ydr_crt)
        arie_maxima(xg[pozg], yst_crt, xdr_crt, ydr_crt)
        arie_maxima(xst_crt, yg[pozg], xdr_crt, ydr_crt)
        arie_maxima(xst_crt, yst_crt, xdr_crt, yg[pozg])



f = open("placa.txt")

# citim coordonatele placii initiale
linie = f.readline().split()    #linie = ["1","1"]
xst_init = int(linie[0])
yst_init = int(linie[1])

linie = f.readline().split()    #linie = ["7","5"]
xdr_init = int(linie[0])
ydr_init = int(linie[1])

# citim coordonatele gaurilor
xg = []
yg = []                    #o gaura are coordonatele (xg[i], yg[i])
for linie in f:
    aux = linie.split()         # aux = ["3","2"]
    xg.append(int(aux[0]))
    yg.append(int(aux[1]))

f.close()

# coordonatele dreptunghiului de arie maxima fara gauri
xst_max = yst_max = xdr_max = ydr_max = 0

# apelam functia arie_maxima
arie_maxima(xst_init, yst_init, xdr_init, ydr_init)
amax = (xdr_max - xst_max) * (ydr_max - yst_max)
print(f"Dreptunghiul cu aria maxima {amax} fara gauri: "
      f"({xst_max}, {yst_max}) -> ({xdr_max}, {ydr_max})")