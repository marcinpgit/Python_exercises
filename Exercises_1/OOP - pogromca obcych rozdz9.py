# Pogromca obcych
# Demonstruje współdziałanie obiektów

class Player(object):
    """Gracz w grze"""
    def blast(self, enemy):
        print("Gracz razi wroga")
        enemy.die()

class Alien(object):
    """Obcy w grze"""
    def die(self):
        print("Obcy umiera.....")

print("\t\t\tGRA ŚMIERĆ OBCEGO")
hero = Player()
invader = Alien()
hero.blast(invader)