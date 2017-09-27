# Write a Python program to find those numbers which are divisible by 7
# and multiple of 5, between 1500 and 2700 (both included).

zakres = range(1500, 2701)
tablica = []

for i in zakres:
    if i % 7 == 0 and i % 5 == 0:
        tablica.append(str(i))
        print(','.join(tablica))
    # print(tablica)
