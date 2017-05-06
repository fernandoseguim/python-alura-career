from datetime import datetime
from random import randrange

def print_header_or_footer(position):

    if position == "header":
        now = datetime.now()
        print("*********************************")
        print("Bem vindo ao jogo de Forca!")
        print("*** Hoje é {:02d}/{:02d}/{:4d} **".format(now.day, now.month, now.year))
        print("*********************************")
    elif position == "footer":
        print("*********************************")
        print("Fim de Jogo!")
        print("*********************************")
    else:
        print("Parametro inválido!")


def load_secret_word():
    file = open("palavras.txt", "r")
    fruits_list = file.read().split("\n")
    fruits_list.pop()
    secret_word = fruits_list[randrange(0, len(fruits_list))].upper()
    return secret_word


def get_shot():
    shot = input("Qual a letra deseja tentar? ").upper().strip()
    return shot


def check_shot(shot, secret_word, list_letters):
    index = 0
    for letter in secret_word:
        if letter == shot:
            list_letters[index] = shot
        index += 1


def print_result(hit):

    if hit:
        print("Parabéns! Você acertou todas as letras da palavra!")
    else:
        print("Você perdeu! Errou todas as suas tentativas!!")


def fork():

    print_header_or_footer("header")
    secret_word = load_secret_word()
    letters_sucessful = ["_" for letter in secret_word]

    forked = False
    hit = False
    errors = 0

    while not hit and not forked:

        print("Palavra {}".format(letters_sucessful))

        shot = get_shot()

        if shot in secret_word:
            check_shot(shot, secret_word, letters_sucessful)

        else:
            errors += 1
            print("Ops, você errou a letra! Faltam {} tentativas!".format(6-errors))

        forked = errors == 6
        hit = "_" not in letters_sucessful

    print_result(hit)

    print_header_or_footer("footer")

if __name__ == "__main__":
    fork()
