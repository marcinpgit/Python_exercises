print ("Wprowadź początkowy i końcowy indeks wycinka łańcucha 'pizza': ")
print ("Aby zakończyć  tworzenie wycinków, w odpowiedzi na monit 'Początek:'\n"
       + "naciśnij klawisz Enter.")

word = "pizza"
start = None
while start != "":
    start = input ("\nPoczątek: ")

    if start:
        start = int (start)

        finish = int (input ("Koniec: "))

        print ("word[", start, ":", finish, "] to", end = " ")
        print (word[start : finish])

input ("\nAby zakończyć program naciśniej enter.")
