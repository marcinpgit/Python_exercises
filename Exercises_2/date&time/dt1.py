# Write a Python script to display the
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

import datetime
import time

print("current date and time: ", datetime.datetime.now())

print("current year: ", datetime.date.today().strftime("%Y") )

print("month of year: ", datetime.date.today().strftime("%B"))

print("week number of the year: ", datetime.date.today().strftime("%W"))

print("weekday of the week: ", datetime.date.today().strftime("%w"))

print("day of year: ", datetime.date.today().strftime("%j"))

print("day of the month: ", datetime.date.today().strftime("%d"))

print("day of the week: ", datetime.date.today().strftime("%A"))

