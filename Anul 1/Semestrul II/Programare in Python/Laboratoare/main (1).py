sir = "IonicaMinune"
print(f"Sirul original este {sir}")
sirNou = input("Pls input! ")
res = sir[0] + sir[int(len(sir)/2)] + sirNou + sir[-1]
print(f"Sirul redus este {res}")