import random

numar_secret = random.randint(1, 100)
print("Am ales un numar intre 1 si 100. Incearca sa il ghicesti!")

while True:
    incercare = int(input("Numar:"))
    if incercare > numar_secret:
        print("Numar prea mare")
    elif incercare < numar_secret:
        print("Numar prea mic")
    else:
        print("Felicitari! Ai ghicit.")
        break