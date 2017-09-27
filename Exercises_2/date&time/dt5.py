# Write a Python program to print yesterday, today, tomorrow.

from datetime import date, timedelta

print("today: ", date.today())

print("yesterday: ", date.today() - timedelta(1))

print("tommorrow: ", date.today() + timedelta(1))

