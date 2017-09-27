print ("Program liczy za użytkownika.\n")

x = int(input("Wprowadź liczbę początkową: "))
y = int(input ("Wprowadź liczbę końcową: "))
y += 1

for i in range (x,y,1):
    print (i, end = " ")

print ("\n\nTwoja liczba początkowa, końcowa to :", {x,y -1})