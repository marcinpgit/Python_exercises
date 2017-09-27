# demonstruje właściwości

class Critter(object):
    """Wrtualny pupil"""

    def __init__(self, name):
        print("Urodził się nowy zwierzak.")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Pusty łańcuch znaków nie może być imieniem.")
        else:
            self.__name = new_name
            print("Zmiana imienia się powiodła")

    def talk(self):
        print("Cześć jestem :", self.name)


zwierz = Critter("Reksio")
zwierz.talk()

print()

print("Imię mojego zwierzaka to: ", zwierz.name)

print()

print("Próbuję zmienić imię na Pucek....")
zwierz.name = "Pucek"
print("Imię mojego zwierzaka to: ", zwierz.name)

print()

print("Próbuję zmienić imię na pusty łańcuch....")
zwierz.name = ""

print()

print("Imię mojego zwierzaka to: ")
print(zwierz.name)