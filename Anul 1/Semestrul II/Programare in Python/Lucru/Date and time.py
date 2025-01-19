# https://docs.python.org/3/library/datetime.html

import datetime

# # Să se calculeze numărul de zile dintre două date calendaristice.
data_crt = datetime.date.today()
print(f"Data curenta: {data_crt.strftime('%d/%m/%Y')}")

data = datetime.date(2023, 8, 1)
print(f" Data dorita: {data.strftime('%d/%m/%Y')}")

diferenta = data_crt - data

print(f"   Diferenta: {abs(diferenta.days)} zile")


# # Să se afișeze în ce zi a săptămânii cade prima zi a fiecărei luni din anul curent.
# zile = ["Luni", "Marți", "Miercuri", "Joi", "Vineri", "Sâmbătă", "Duminică"]
# an_crt = datetime.date.today().year
# for luna_crt in range(1, 13):
#     data_crt = datetime.date(an_crt, luna_crt, 1)
#     print(f"{data_crt.strftime('%d/%m/%Y')} -> {zile[data_crt.weekday()]}")


# # Să se afișeze prima zi de luni din fiecare lună a anului curent.
# an_crt = datetime.date.today().year
# print("Prima zi de luni:")
# for luna_crt in range(1, 13):
#     zi_crt = 1
#     while datetime.date(an_crt, luna_crt, zi_crt).weekday() != 0:
#         zi_crt += 1
#
#     print(f"{datetime.date(an_crt, luna_crt, zi_crt).strftime('%d/%m/%Y')}")


# # Să se afișeze ziua de salariu din fiecare lună a anului curent.
# # Se presupune că salariul se încasează în prima zi lucrătoare după ziua de 15 din luna respectivă.
# an_crt = datetime.date.today().year
# zi_salariu = 15
# print("Zilele de salariu:")
# for luna_crt in range(1, 13):
#     data_crt = datetime.date(an_crt, luna_crt, zi_salariu)
#     if data_crt.weekday() == 5:
#         zi_aux = zi_salariu + 2
#     else:
#         if data_crt.weekday() == 6:
#             zi_aux = zi_salariu + 1
#         else:
#             zi_aux = zi_salariu
#
#     print(f"{datetime.date(an_crt, luna_crt, zi_aux).strftime('%d/%m/%Y')}")
