class Critter(object):
    """Wirtyalny pupil z atrybutem name"""

    def __init__(self, name):
        print("Urodził się nowy zwierzak!")
        self.name = name

    def __str__(self):
        rep = "Obiekt klasy Critter\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("Cześć jestem ", self.name, "\n")


zwierz1 = Critter("Reksio")
zwierz1.talk()

zwierz2 = Critter("Pucek")
zwierz2.talk()

print("Wyświetlenie obiektu zwierz1:\n")
print(zwierz1)

