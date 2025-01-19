# deschide users.in si citeste datele
with open('users.in', 'r') as file: #read mode
    date_useri = {}

    for rand in file:
        # split linie in user, parola, nivel
        user, password, access_level = rand.strip().split(',')
        date_useri[user] = {'password': password, 'access_level': int(access_level)}

print("Lista utilizatori si nivel acces:")
for user, data in date_useri.items():
    print(f"Utilizatorul {user}, are nivelul de acces: {data['access_level']}")

# autentificare
print("\n -- Autentificare utilizator --")
username = input("Introdu utilizatorul: ")
password = input("Introdu parola: ")

# verificare autentificare
if username in date_useri:
    if date_useri[username]['password'] == password:
        print('Te-ai autentificat cu succes!')
        print(f'Bine ai venit, {username}! Nivelul tau de acces este: {date_useri[username]['access_level']}')
    else: print('Parola incorecta!')
else: print(f'Nu exista utilizatorul {username}!')

# ex. dictionar incarcat:
# date_useri = {
#     'ion': {'password': 'pass123', 'access_level': 1},
#     'stefan': {'password': 'securepass', 'access_level': 2},
#     'mirel': {'password': '1234', 'access_level': 3}
# }