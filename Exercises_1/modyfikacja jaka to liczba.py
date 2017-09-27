import random

number = random.randint(1, 5)

tries = 0

while tries < 3:
    guess = int (input ("Ta liczba to: "))
    tries += 1
    if number < guess:
        print ("za duża.")
    elif number > guess:
        print ("za mała.")
    elif number == guess:
        print ("Odgadłeś!!!!")
        break
while tries == 3 and number != guess:
    print ("Wykorzystałeś już wszystkie próby!")
    break

input ("\n\nNaciśniej klawisz enter aby zakończyć.")
