class Critter(object):
    """Wirtualny pupil z konstruktorem __init__ (inaczej metodą inicjalizacji"""

    def __init__(self):
        print("Urodził się nowy zwierzak!!!")

    def talk(self):
        print("Cześć jestem instancją klasy Critter.")

zwierz1 = Critter()
zwierz2 = Critter()

print()

zwierz1.talk()
zwierz2.talk()