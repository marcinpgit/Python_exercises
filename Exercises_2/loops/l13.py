# Write a Python program that accepts a string and calculate the number of digits and
# letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

tekst = input("podaj tekst: ")
j = 0
k = 0

for i in tekst:
    if i.isdigit():
        j += 1
    elif i.isalpha():
        k += 1
    else:
        pass

print("Liter: {}, Cyfr: {}".format(k, j))