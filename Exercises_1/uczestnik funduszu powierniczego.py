print (
    """
            Uczestnik Funduszu Powierniczego

Program sumuje Twoje miesięczne wydatki.

Wprowadź swoje miesięczne wymagane koszty. Ponieważ jesteś bogaty, zignoruj grosze i wprowadź kwoty w pełnych złotych
"""
    )

car = input ("Serwis Insigni: ")
car = int (car)

rent = int (input ("Apartament na Lawendowym: "))
jet = int (input ("Wynajem samolotu: "))
gifts = int (input ("Podarunki: "))

food = input ("Obiady w restauracjach: ")
food = int (food)

staff = int (input ("Personel osobisty - kucharze, kierowca, służba domowa: "))

suma = car + rent + jet + gifts + food + staff

print ("\nOgółem = ", suma)

input ("\n\nNaciśnij klawisz Enter aby zakończyć")
