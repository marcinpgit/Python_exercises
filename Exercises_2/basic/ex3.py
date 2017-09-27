# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

word = str(input("Podaj słowo: "))

if word == word[::-1]:
    print("Palindrom.")
else:
    print("Nie palindrom.")