# lista de nr intregi
L = [int(x) for x in input().split()]
rezultat = sorted(set(L), reverse = True)
print(rezultat)