import random

print ("Wyczuwam prawdziwą energię. Twoje prawdziwe emocje znajdują odbicie na moim ekranie")

mood = random.randint (1,3)

if mood == 1:
    print ("\nJesteś w doskonałym humorze.")
elif mood == 2:
    print ("\nJesteś w obojętnym humorze.")
elif mood == 3:
    print ("\nJesteś w smutnym nastroju.")
else:
    print ("Nieprawidłowa wartość nastroju.")

input ("\n\nNaciśniej klawisz Enter aby zakończyć program.")


