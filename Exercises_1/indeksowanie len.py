import random

word = "indeks"
print ("Wartość zmiennej word to: ",word,"\n")

high = len (word)
low = -len (word)

for i in range (10):
    position = random.randrange(low, high)
    print ("word[", position, "]\t", word[position])

input ("\nNaciśnij klawisz enter aby zakończyć.")
