# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock


u1 = input("Podaj - rock, scissors, paper: ")
u2 = input("Podaj - rock, scissors, paper: ")

if u1 == u2:
    print("Remis!")

elif u1 == 'rock':
    if u2 == 'paper':
        print("Paper wins!")
    else:
        print("Rock wins!")

elif u1 == 'scissors':
    if u2 == 'rock':
        print("Rock wins!")
    else:
        print("Scissors wins!")

elif u1 == 'paper':
    if u1 == 'scissors':
        print("Scissors wins!")
    else:
        print("Paper wins!")

