# marynowanie/pickling
# demonstruje marynowanie i odkładanie na półkę

import pickle, shelve

print("Marynowanie list.")
rodzaj = ["łagodny", "pikantny", "kwaszony"]
ksztalt = ["cały", "krojony wzdłuż", "w plasterkach"]
producent = ["Dawton", "Klimex", "Vortumnus"]

plik = open("marynowane.dat", "wb")

pickle.dump(rodzaj, plik)
pickle.dump(ksztalt, plik)
pickle.dump(producent, plik)
plik.close()

print("\nOdmarynowanie list.")
plik = open("marynowane.dat", "rb")
print(rodzaj)
print(ksztalt)
print(producent)
plik.close()

print("\nOdkładanie listy na półkę.")
polka = shelve.open("marynowane2.dat")

polka["rodzaj"] = ["łagodny", "pikantny", "kwaszony"]
polka["ksztalt"] = ["cały", "krojony wzdłuż", "w plasterkach"]
polka["producent"] = ["Dawton", "Klimex", "Vortumnus"]
polka.sync()

print("\nPobieranie list z półki.")
print("prodecent - ", polka["producent"])
print("kształt - ", polka["ksztalt"])
print("rodzaj - ", polka["rodzaj"])
polka.close()


