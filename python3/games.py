from datetime import datetime

from games.fork import fork
from games.guessing import guessing

def select_game():
    now = datetime.now()

    print("*********************************")
    print("*** Hoje é {:02d}/{:02d}/{:4d} **".format(now.day, now.month, now.year))
    print("Escolha o seu jogo!")
    print("*********************************")


    print("(1) Forca\n(2) Adivinhação")
    selected_game = int(input("Deseja iniciar qual jogo? "))

    if selected_game == 1:
        print("Jogando Forca")
        fork()
    elif selected_game == 2:
        print("Jogando Adivinhação")
        guessing()

if __name__ == "__main__":
    select_game()


