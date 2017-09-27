# Write a Python program to check a string represent an integer or not.
# Expected Output:
#
# Input a string: Python
# The string is not an integer.

tekst = input("Podaj tekst do weryfikacji str/int: ")

if tekst.isalpha():
    print("string")

elif tekst.isdigit():
    print("integer")

else:
    print("string oraz integer")