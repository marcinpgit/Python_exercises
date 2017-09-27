# Write a Python program to subtract five days from current date.
# Sample Date :
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17

from datetime import date, timedelta

data_wynik = date.today() - timedelta(7)

print(data_wynik)