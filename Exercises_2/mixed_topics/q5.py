# Question 5
# Level 1
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters

class Wypisz(object):
    def __int__(self, s):
        self.s = ''

    def string_in(self):
        self.s = input('podaj tekst: ')

    def strin_out(self):
        print(self.s.upper())

tekst = Wypisz()
tekst.string_in()
tekst.strin_out()