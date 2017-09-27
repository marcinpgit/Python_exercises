import random

print ("Program rzuca 100 razy monetą i zlicza ilość reszek i orzełków.\n")

moneta = 0
orzel = 0
reszka = 0

while moneta < 100:
    moneta += 1
    rzut = random.randint (1, 2)
    if rzut == 1:
            print ("orzeł")
            orzel += 1
    else:
            print ("reszka")
            reszka += 1

print (orzel)
print (reszka)

 
    




input ("\nNaciśnij klawisz enter aby zakończyć.")
