# Write a Python program to print next 5 days starting from today

from datetime import date, timedelta

dzis = date.today()

for x in range(0, 5):
    print(dzis + timedelta(days=x))

