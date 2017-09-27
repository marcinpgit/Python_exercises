# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

rok = int(input("Podajrok: "))
miesiac = int(input("Podaj miesiąc: "))

print()
print(calendar.month(rok, miesiac))
