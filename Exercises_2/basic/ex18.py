# Write a Python program to count the number 4 in a given list.

a = [1, 2, 4, 5, 6, 4, 7, 4]
j = 0

for i in a:
    if i == 4:
        j += 1
print(j)