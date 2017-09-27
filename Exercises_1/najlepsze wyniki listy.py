# Najlepszy wynik - metody listy

scores = []
choice = None

while choice != "0":
    print (
    """
    Najlepsze wyniki
    
    0 - zakończ
    1 - pokaż wynik
    2 - dodaj wynik
    3 - usuń wynik
    4 - posortuj wynik
    """
)
    choice = input("Wynierasz: ")

    if choice == "0":
        print ("Do widzenia")
    elif choice == "1":
        print ("Najlepszy wynik")
        for score in scores:
            print (score)
    elif choice == "2":
        score = int (input ("Jaki wynik uzyskałeś: "))
        scores.append (score)
    elif choice == "3":
        score = int (input ("Który wynik chcesz usunąć: "))
        if score in scores:
            scores.remove(score)
        else:
            print (score, " nie ma na liście wyników.")
    elif choice == "4":
        scores.sort(reverse = True)
    else:
        print (choice, " nie jest tu prawidłowym wyborem.")


