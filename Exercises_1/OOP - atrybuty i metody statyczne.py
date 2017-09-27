# demonstruje atrybuty klasy i metody statyczne

class Critter(object):
    """Wirtualny pupil"""
    total = 0

    @staticmethod
    def status():
        print("Ogólna liczba zwierzków wynosi: ", Critter.total)

    def __init__(self, name):
        self.name = name
        print("Urodził się zwierzak!")
        Critter.total += 1

print("Uzyskanie dostępu do atrybutu Critter.total:", end = " ")
print(Critter.total)
print()

print("Tworzenie zwierzaków:")
zwierz1 = Critter("Zwierzak 1")
zwierz2 = Critter("Zwierzak 2")
zwierz3 = Critter("Zwierzak 3")

print(Critter.total)