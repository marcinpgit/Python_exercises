# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days


from datetime import date

data1 = date(2014, 7, 2)
data2 = date(2014, 7, 11)

ilosc_dni = data2 - data1
print(ilosc_dni)


