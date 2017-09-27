# inwentarz bohatera 3.0 - demonstruje listy

inventory = [ "miecz", "zbroja", "tarcza", "napój uzdrawiający"]

print ("\nElementy Twojego uzbrojenia to:\n")
for item in inventory:
    print (item)
input ("\nAby kontynuować grę naciśnij klawisz Enter.\n")

print ("Twój dobytek zawiera ", len(inventory), " elementy(ów).\n")
input ("\nAby kontynuować grę naciśnij klawisz Enter.\n")

if "napój uzdrawiający" in inventory:
    print ("\nDożyjesz dnia, w którym stoczysz walkę!\n")

index = int (input("\nWprowadź indeks elementu inwentarza: "))
print ("Pod indeksem ", index, " znajduje się", inventory[index])

start = int(input("\nWprowadź indeks oznaczający początek wycinka: "))
finish = int (input("\nWprowadź indeks oznaczający koniec wycinka: "))
print ("\nInwentarz w wybranym wycinku to ", inventory[start:finish])
input ("\nAby kontynuować grę naciśnij klawisz Enter.\n")

chest = ["złoto", "klejnoty"]
print ("\nZnajdujesz skrzynię, która zawiera\n", chest)
print ("Dodajesz zawartość skrzyni do swojego inwentarza.")
inventory += chest
print ("Twój aktualny inwentarz to:\n", inventory)
input ("\nAby kontynuować grę naciśnij klawisz Enter.\n")

print ("\nWymieniasz swój miecz na kuszę.\n")
inventory [0] = "kusza"
print ("\nTwój aktualny inwentarz to:\n", inventory)
input ("\nAby kontynuować grę naciśnij klawisz Enter.\n")

print ("Zużywasz swoje złoto i klejnoty na kulę do wróżenia.\n")
inventory [4:6] = ["kula do wróżenia"]
print ("\nTwój aktualny inwentarz to:\n", inventory)
input ("\nAby kontynuować grę naciśnij klawisz Enter.\n")

print ("\nW wielkiej bitwie Twoja tarcza zostaje zniszczona.\n")
del inventory [2]
print ("\nTwój aktualny inwentarz to:\n", inventory)
input ("\nAby kontynuować grę naciśnij klawisz Enter.\n")

print ("\nTwoja kusza i zbroja zostają skradzione przez złodziei.\n")
del inventory [:2]
print ("\nTwój aktualny inwentarz to:\n", inventory)




