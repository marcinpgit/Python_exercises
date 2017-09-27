# Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

zdanie = input('podaj zdanie które zawiera duże i małe litery: ')

u = 0
l = 0

for k in zdanie:
    if k.islower():
        l += 1
    elif k.isupper():
        u += 1
    else:
        pass

print('Dużych liter w zdaniu jest {} a małych {}.'.format(u, l))