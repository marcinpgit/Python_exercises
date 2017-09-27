# demonstruje zmienne i atrybuty prywatne

class Critter(object):
    def __init__(self, name, mood):
        print("Urodził się nowy zwierak")
        self.name = name        # atrybut publiczny
        self.__mood = mood        # atrybut prywatny

    def talk(self):
        print("Jestem ", self.name)
        print("W tej chwili czuję się ", self.__mood, "\n")

    def __private_method(self):
        print("To jest metoda prywatna.")

    def public_method(self):
        print("To jest metoda publiczna.")
        self.__private_method()

zwierz1 = Critter("Reksio", "szczęśliwy")
zwierz1.talk()

zwierz1.public_method()