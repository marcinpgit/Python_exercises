print ("\nProgram wybiera losowo słowo, które gracz musi odgadnąć.\n")

import random

WORDS = ("kot", "pies", "komunikat", "dom", "niebo")
word = random.choice (WORDS)
ile_liter = len(word)

print ("W wylosowanym słowie przez komputer znajduje się ", ile_liter, " liter.\n")

szansa = 0
odp = " "

while odp != word and szansa < 3:
    szansa += 1
    litera = input("Podaj literkę, która występuje w słowie: ")
    if litera in word:
            print ("\ntak")
    else:
            print ("\nnie")
    odp = input ("\nPodaj słowo, które wylosował komputer: ")
    if odp == word:
        print ("\nBrawo zgadłeś.")
    else:
        print ("\nZła odpowiedź.")

# Program mógłby działać lepiej