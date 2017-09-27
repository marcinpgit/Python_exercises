# Question 17
# Level 2
#
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from
# console input. The transaction log format is shown as following:
# D 100
# W 200
# ??
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

bilans = 0

while True:
    s = input("podaj operacje z kwotą oddzielone spacją: ")

    if not s:
        break

    wartosc = s.split(" ")
    operacja = wartosc[0]
    kwota = int(wartosc[1])

    if operacja == "D":
        bilans += kwota
    elif operacja == "W":
        bilans -= kwota
    else:
        pass

print(bilans)