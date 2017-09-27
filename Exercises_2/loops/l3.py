# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then
# the prompt appears again until the guess is correct, on successful guess,
# user will get a "Well guessed!" message, and the program will exit.

import random

los = random.randrange(1, 10)
guess = None
print(los)

while guess != los:
    guess = int(input("Podaj liczbe z przedziału 1 - 9: "))
    if guess != los:
        print("Zgaduj dalej.")

print("Brawo zgadłeś, wylosowana liczba to {}.".format(los))

