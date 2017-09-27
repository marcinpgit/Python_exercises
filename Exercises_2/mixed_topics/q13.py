# Question 13
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

zdanie = input('podaj zdanie ktoóre zawiera litery i cyfry: ')
c = 0
l = 0

for i in zdanie:
    if i.isdigit():
        c += 1
    elif i.isalpha():
        l += 1
    else:
        pass

print('W zdaniu które podałeś jest {} cyfr i {} liter.'.format(c,l))


