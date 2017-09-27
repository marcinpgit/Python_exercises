
geek = {"Ola": "Mała dziewczynka", "Monika": "Mama Oli", "Żłobek": "Tam chodzi Ola"}
choice = None

while choice != 0:
    print(
        """
        Translator slangu komputerowego:
        
        0 - zakończ
        1 - znajdź termin
        2 - dodaj nowy termin
        3 - zmień definicję terminu
        4 - usuń termin
        """
    )

    choice = input("Wybierasz: ")
    baza = []

    if choice == "0":
        print("Żegnaj!!!")

    elif choice == "1":
        term = input("Jaki termin chcesz objaśnić?: ")
        if term in geek:
            definition = geek[term]
            print(term, " oznacza ", definition)
        else:
            print("Niestety, nie znam terminu", term)
    elif choice == "2":
        term = input("Dodaj nowy termin: ")
        if term not in geek:
            definition = input("Podaj definicję terminu: ")
            geek[term] = definition
            print("Termin", term, " został dodany.")
        else:
            print("Termin ", term, " już istnieje.")
    elif choice == "3":
        term = input("Jaki termin mam przedefiniować?")
        if term in geek:
            definition = input("Podaj nową definicję dla terminu: ")
            geek[term] = definition
            print("Termin ", term, " został przedefiniowany!")
        else:
            print("Wybrany termin nie istnieje, wybierz ponownie.")
    elif choice == "4":
        term = input("Podaj termin do usunięcia: ")
        if term in geek:
            del geek[term]
            print("Termin ", term, " został usunięty.")
        else:
            print("Podany termin ", term, " nie istnieje!!")