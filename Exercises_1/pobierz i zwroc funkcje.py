# pobierz i zwróć
# Demostruje parametry i wartości zwrotne
# Przykład: jedna funkcja pobiera wartość, następna zwraca pewną wartość, ostatnia pobiera i zwraca

def display(message):
    print(message)

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie"""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

#main

display("To wiadomość dla ciebie.")

number = give_me_five()
print("Oto co otrzymałem z funkcji give_me_five(): ", number)

answer = ask_yes_no("Wprowadź 't' lub 'n': ")
print("Dziękuę za wprowadzenie: ", answer)
