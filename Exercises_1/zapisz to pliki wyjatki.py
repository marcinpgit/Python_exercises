# zapisz to demonstruje zapisywanie danych do pliku tekstowego

print("Utwórz plik tekstowyza pomocą metody write().\n")
plik_tekst = open("zapisz_to.txt", "w")

plik_tekst.write("Wiersz 1\n")
plik_tekst.write("Linia 2\n")
plik_tekst.write("Ostatni wiersz 3\n")

plik_tekst.close()

print("Odczytanie zawartości nowo utworzonego pliku:")
plik_tekst = open("zapisz_to.txt", "r")
print(plik_tekst.read())



print("\nUtworzenie pliku tekstowego za pomocą metody writelines().\n")
plik_text = open("zapisz_to2.txt", "w")

plik_text.writelines(["Linia 1\n", "Wiersz 2\n", "Ostatnia linia 3\n"])

plik_text.close()

print("\nOdczytanie zawartości nowo utworzonego pliku:")
plik_text = open("zapisz_to2.txt", "r")
print(plik_text.read())
plik_text.close()

