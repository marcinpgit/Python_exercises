# gra a'la szubienica listy i słowniki - nie chce misię rysować wisielca to będzie 10 kresek

import random

HANGMAN = ("----------")
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("ksiegarnia", "slimak", "szkola", "python")

word = random.choice(WORDS)

so_far = "-" * len(word)

wrong = 0

used = []

print("Witaj w grze!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("Wykorzystałeś już następujące litery: ", used)
    print("Na razie zagadkowe słowo wygląda tak: ", so_far)
    guess = input("Podaj literę: ")
    guess = guess.lower()

    while guess in used:
        print("Wykorzystałeś już tą literę", guess)
        guess = input("Wprowadź literę: ")
        guess = guess.lower()
    used.append(guess)

    if guess in word:
        print("Tak, litera znajduje się w słowie.")
        # new nowa wersja zmiennej so_far, aby zawierała odgadniętą literę
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("Niestety ", guess, " nie wystepuje w zagadkowym złowie!")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("Przegrałeś!!!!!!!!!!!!!")
else:
    print("Gratulacje, odgadłeś!!")
    print("Zagadkowe słowo to: ", word)


