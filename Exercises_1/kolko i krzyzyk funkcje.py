# Kółko i krzyżyk z wykożystaniem funkcji
# komputer przeciwko człowiekowi

# Stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instructions():
    """Ta funkcja wyświetla instrukcję gry"""
    print("""
    To jest instrukcja gry.....
    Pola gry wyglądają tak
    0 | 1 | 2
    3 | 4 | 5
    6 | 8 | 9 
    """)

def ask_yes_no(question):
    """Zadaje pytanie na które można odp. tak lub nie"""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
        return response

def ask_number(question, low, high):
    """Poproś o podanie liczby z odpowiedniego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
        return response

def pieces():
    """Ustala do kogo należy pierwszy ruch"""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t\\n): ")
    if go_first == 't':
        print("Wykonujesz pierwszy ruch.")
        human = X
        computer = O
    else:
        print("Pierwszy ruch wykonuje komputer.")
        computer = X
        human = O
    return computer, human

def new_board():
    """Utworzy nową planszę gry"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board():
    """Wyświetla plansze gry na ekranie"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "-----------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "-----------")
    print("\n\t", board[6], "|", board[7], "|", board[8])

def legal_moves():
    """Utworzy listę prawidłowych ruchów"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
        return moves

def winner():
    """Ustala zwycięzcę gry"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    """Odczytaj ruch człowieka"""
    legal = legal_move(borad)
    move = None
    while move not in legal:
        move = ask_number("Jaki będzie Twój ruch (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest już zajęte. Wybierz inne.")
        print("Znakomicie...")
        return move

def computer_move(board, computer, human):
    """Spowoduje wykonanie ruchu przez komputer"""
    # utwórz kopię roboczą, ponieważ funkcja będzie zmieniać liste
    board = board[:]
    # najlepsze pola do zajęcia wg kolejności
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Wybieram pole numer:", end = " ")
    # jeżeli komputer może wygrać, wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY
        # jeżeli komputer może wygrać, wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY
    # ponieważ nikt nie może wygrać w następnym ruchu, wybierz najlepsze wolne pole
        for move in legal_moves(board):
            print(move)
            return move

def next_turn():
    """Zmień wykonawcę ruchu"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Pogratuluj zwycięzcy"""
    if the_winner != TIE:
        print(the_winner, " jest zwycięzcą!")
    else:
        print("Remis")

    if the_winner == computer:
        print("Wygrał komputer!")
    if the_winner == human:
        print("Wygrał człowiek!")
    if the_winner == TIE:
        print("Remis!")

def main():
    display_instructions()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# rozpocznij program
main()
input("\nNaciśnij klawisz enter aby zakończyć grę.")
