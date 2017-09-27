import random

liczba_moja = int (input ("Użytkownik podaje swoją liczbę z przedziału 1-100: "))
liczba_p = ""

while liczba_moja != liczba_p:
       liczba_p = random.randrange(100)
       print (liczba_p)
       if liczba_p == liczba_moja:
           print ("Użytkowniku, Twoja liczba to :", liczba_p)
    


input ("\n\nNaciśnij enter aby zakończyć.")     
                   
    
