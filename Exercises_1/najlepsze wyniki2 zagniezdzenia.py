# Najlepszy wynik - metody zagnieżdżania list i krotek

scores =[]
choice = None

while choice != "0":
    print (
    """
    --Najlepsze wyniki--
    
    0 - zakończ
    1 - pokaż wynik
    2 - dodaj wynik
    """
    )

    choice = input ("Wybierasz: ")
    print ()
    if choice == "0":
        print("Do widzenia!")
    elif choice == "1":
        print ("Najlepsze wyniki:")
        print ("GRACZ\tWYNIKI")
        for entry in scores:
            score, name = entry
            print (name, "\t", score)
    elif choice == "2":
        name = input ("Podaj nazwę gracza: ")
        score = int(input("Podaj jaki wynik gracz uzyskał: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print("Niestety ", choice, " nie jest prawidłowym wyborem!")

