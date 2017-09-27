print ("Twój bohater jest otoczony przez armię troli.\
        Bohater wyjmuje miecz, gotów do stoczenia swej ostatniej bitwy.\n")

health = 10
damage = 3
trolls = 0

while health > 0:
    trolls += 1
    health -= damage
    print ("Bohater pokonuje złego trola i odnosi obrażenia ", damage, " punkty zdrowia")

print ("\nTwój bohater walczył dzielnie i pokonał ", trolls, " troli.")


input ("\n\nNaciśnij klawisz Enter aby zakończyć program.")
    
