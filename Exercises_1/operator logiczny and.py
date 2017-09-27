print ("\tEksluzywna sieć komputerowa")
print (" \tTylko dla członków!\n")

security = 0

username = ""
while not username:
    username = input ("Użytkownik: ")

password = ""
while not password:
    password = input ("Hasło: ")

if username == "Marcin" and password == "sekret":
        print ("Cześć Marcin")
        secusity = 5
elif username == "Ola" and password == "sekret1":
        print ("Cześć Ola")
        security = 3
else:
    print ("Nieudana próba logowania do systemu.")

input ("\nNaciśniej klawisz enter aby zakończyć.")
    
