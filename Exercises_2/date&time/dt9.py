# Write a Python program to print yesterday, today, tomorrow.

import datetime

tdelta = datetime.timedelta(days=1)

tday = datetime.date.today()
print("today: ", tday)

yday = tday - tdelta
print("yesterday: ", yday)

tomorrow = tday + tdelta
print("tomorrow: ", tomorrow)
