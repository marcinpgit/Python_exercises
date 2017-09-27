inventory = ()

if not inventory:
    print ("Masz puste ręce.")

input ("\nAby kontynuować naciśnij klawisz Enter.")

inventory = ("miecz",
                            "zbroja",
                             "tarcza",
                             "napój uzdrawiający")

print ("\nWykaz zawartości krotki: ")
print (inventory)

print ("\nElementy Twojego wyposażenia:")
for item in inventory:
    print (item)

input ("\n\nNaciśnij enter aby zakończyć program.")
