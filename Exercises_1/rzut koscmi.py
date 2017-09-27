import random

die1 = random.randint (1,6)
die2 = random.randrange (6) + 1

total = die1 + die2

print ("Wyrzuciłeś ", die1, " oraz ", die2, " i uzyskałeś sumę ", total)

input ("\n\nWciśnij klawisz enter aby zakończyć program")
