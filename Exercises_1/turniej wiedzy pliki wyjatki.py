# turniej wiedzy
# odczytuje dane ze zwykłego pliku tekstowego

import sys

def otworz_plik(otworz_plik, mode):
    """Otwórz plik"""
    try:
        plik = open(nazwa_pliku, mode)
    except IOError as e:
        print("Nie można otworzyć pliku ", nazwa_pliku, " program zostanie zakończony.\n, e")
        sys.exit()
    else:
        return plik

def nast_linia(plik):
    """Zwróć kolejny wiersz pliku kwiz po sformatowaniu go."""
    linia = plik.readline()
    linia = linia.replace("/", "\n")
    return linia

def nast_blok(plik):
    """Zwróć kolejny blok danych z pliku kwiz"""
    kategoria = nast_linia(plik)

    pytanie = nast_linia(plik)

    odpowiedz = []
    for i in range(4):
        odpowiedz.append(nast_linia(plik))

    poprawna = nast_linia(plik)
    if poprawna:
        poprawna = poprawna[0]

    wyjasnienie = nast_linia(plik)

    return kategoria, pytanie, odpowiedz, poprawna, wyjasnienie

def witam(tytul):
    """Powitanie i pobranie nazwy gracza"""
    print("\tWitaj w turnieju wiedzy!")
    print("\t\t", tytul, "\n")

# Zainicjowanie gry
def main():
    trivia_plik = open("kwiz.txt", "r")
    tytul = nast_linia(trivia_plik)
    witam(tytul)
    score = 0
# Pobierz pierwszy blok / zadanie pytania
    kategoria, pytanie, odpowiedz, poprawna, wyjasnienie = nast_blok(trivia_plik)
    while kategoria:
# zadaj pytanie
        print(kategoria)
        print(pytanie)
        for i in range(4):
            print("\t", i + 1, "-", odpowiedz[i])
# pobranie odpowiedzi
        odpowiedz = input("Jaka jest Twoja odpowiedź?: ")
# sprawdź odpowiedź

    if odpowiedz == poprawna:
        print("Poprawna odpowiedź.", end = " ")
        score += 1
    else:
        print("\nOdpowiedź niepoprawna.", end = " ")
    print(wyjasnienie)
    print("Wynik: ", score)
# pobranie kolejnego bloku / pytania
    kategoria, pytanie, odpowiedz, poprawna, wyjasnienie = nast_blok(trivia_plik)
# zakończenie gry
    trivia_plik.close()

    print("To było ostatnie pytanie.")
    print("Twój końcowy wynik wynosi: ", score)

# uruchomienie funkcji main
main()
