f = open("exemplu.txt", "w")

'''
t = f.read()
t = f.readlines()

print(t, len(t))
'''

for linie in f:
    print(linie, end="")

'''
for k in range(1, 11):
    f.write(str(k) + "\n")
'''

f.close()