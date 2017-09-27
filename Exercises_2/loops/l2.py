# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

temp = input("Podaj temp w C lub F: ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
    rezultat = int(round((9 * degree) / 5 + 32))
    skala = "Farenheit"

elif i_convention.upper() == "F":
    rezultat = int(round((degree - 32) * 5 / 9))
    skala = "Celsius"

else:
    print("Nieprawidłowowprowadzona temp!!")

print("Temperatura w {} wynosi {} stopni.".format(skala, rezultat))




