#Demonstruje argumenty nazwane i domyślne wartości parametrów

# parametry pozycyjne
def birthday(name, age):
    print("Szczęśliwych urodzin ", name, " Masz już ", age, " lat.")

#parametry z wartościami domyślnymi
def birthday2(name = "Ola", age = 2):
    print("Szczęśliwych urodzin ", name, " Masz już ", age, " lat.")

birthday("Ola", 2)
birthday(2, "Ola")
birthday(name = "Monika", age = 2)
birthday(age = 2, name = "Ola")
print()
birthday2()
birthday2(name = "Monika")
birthday2(age = 3)
birthday2(name = "Monia", age = 5)
birthday2("Monia", 5)

