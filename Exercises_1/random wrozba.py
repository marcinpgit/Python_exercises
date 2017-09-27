import random
print ("\tProgram losuje ciastko z wróżbą od 1 do 5.")

wrozba = random.randrange(5) + 1

if wrozba == 1:
    print ("Pierwsza wróżba")
elif wrozba ==2:
    print ("Druga wróżba")
elif wrozba == 3:
    print ("Trzecia wróżba")
elif wrozba == 4:
    print ("Czwarta wróżba")
elif wrozba == 5:
    print ("Piąta wróżba")

input ("\nAby zakończyć naciśnij klawisz enter.")
