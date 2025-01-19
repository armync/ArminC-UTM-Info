while True:
    an = int(input("Introduceti anul: "))
    if an==0:
        break
    if an%4==0 and (an%100!=0 or an%400==0):
        print("An bisect")
    else:
        print("Nu este bisect")