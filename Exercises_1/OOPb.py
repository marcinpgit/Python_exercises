# Demonstruje import modułów

import OOPa
import random

again = None
while again != "n":
    players = []
    num = OOPa.ask_number(question="Podaj liczbę graczy (2 - 5): ", low = 2, high = 5)
    for i in range(num):
        name = input("Nazwa gracza: ")
        score = random.randrange(100) + 1
        player = OOPa.Player(name, score)
        players.append(player)

    print("Oto wyniki gry: ")
    for player in players:
        print(player)

    again = OOPa.ask_yes_no("Czy chcesz zagrać ponownie? (t/n): ")