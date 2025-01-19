import matplotlib.pyplot as plt


file = open("date.in")

histogram = {chr(i):0 for i in range(ord('a'), ord('z')+1)}

for line in file:
    line = line.strip().lower()
    for letter in line:
        if letter.isalpha():
                histogram[letter] += 1

# print(histogram)

file.close()

categories = list(histogram.keys())
values = list(histogram.values())

plt.bar(categories,values)
plt.xlabel("Letter")
plt.ylabel("Frequency")
plt.title("Letters histogram")

plt.show()