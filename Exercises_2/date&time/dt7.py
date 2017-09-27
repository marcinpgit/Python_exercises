# Write a Python program to add 5 seconds with the current time.
# Sample Data :
# 13:28:32.953088
# 13:28:37.953088

import datetime

dt = datetime.datetime.now()
print(dt)

print(dt + datetime.timedelta(seconds=5))