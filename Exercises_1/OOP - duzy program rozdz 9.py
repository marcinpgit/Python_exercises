# opiekun zwierzaka
# wirtualny pupil, którym należy się opiekować

class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'szczęśliwy'
        elif unhappiness <= 10:
            m = 'zadowolony'
        elif unhappiness <= 15:
            m = 'podenerwowany'
        else:
            m = 'wściekły'
        return m

    def talk(self):
        print("Mam na imię ", self.name, " i jestem ", self.mood, " teraz\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Mniam, mniam, dziękuję!!!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Hura!!!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
        zwierz_name = input("Podaj imię zwierzaka: ")
        zwierz = Critter(zwierz_name)

        choice = None
        while choice != 0:
            print("""
        Opiekun zwierzaka
        
        0 - zakończ program
        1  -słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem
        """)

            choice = input("Wybierasz: ")

            if choice == "0":
                print("Do widzenia!")

            elif choice == "1":
                zwierz.talk()

            elif choice == "2":
                zwierz.eat()

            elif choice == "3":
                zwierz.play()

            else:
                print("Nieznany wybór!!!")

main()