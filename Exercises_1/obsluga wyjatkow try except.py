# demonstruje obsługę wyjątków
# try / except

try:
    liczba = float(input("Podaj liczbę: "))
except:
    print("Wystąpił błąd!")

# specyfikacja z typem wyjątku
try:
    liczba2 = float(input("Wprowadź liczbę: "))
except ValueError:
    print("To nie była liczba!")

# obsługa kilku typów wyjątków
print()
for wartosc in (None, "Hej!"):
    try:
        print("Próba konwersji: ", wartosc, " ---> ", end = " ")
        print(float(wartosc))
    except TypeError:
        print("Możliwa jest tylko konwersja łańcucha lub liczby.")
    except ValueError:
        print("Możliwa jest tylko konwersja łańcucha cyfr.")

# pobierz argument wyjątku / klauzula else
try:
    liczba3 = float(input("\nPodaj jakąś liczbę: "))
except ValueError as e:
    print("To nie była liczba! Lub wyrażając to na spsób Pythona...")
    print(e)
else:
    print("Wprowadziłeś liczbę!!!")
