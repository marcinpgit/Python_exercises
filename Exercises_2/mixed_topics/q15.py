# Question 15
# Level 2
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

liczba = int(input('podaj liczbe: '))

c1 = int('%s' % liczba)
c2 = int('%s%s' % (liczba, liczba))
c3 = int('%s%s%s' % (liczba, liczba, liczba))
c4 = int('%s%s%s%s' % (liczba, liczba, liczba, liczba))

suma = c1 + c2 + c3 + c4

print(suma)