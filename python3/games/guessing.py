from datetime import datetime
from random import randrange


def guessing():
    now = datetime.now()
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*** Hoje é {:02d}/{:02d}/{:4d} **".format(now.day, now.month, now.year))
    print("*********************************")

    secret_number = randrange(1, 101)
    hit = False
    list_numbers = []
    count = 1
    score = 100

    while not hit:

        user_number = int(input("Digite um novo número entre 1 e 100: "))
        print("Você digitou ", user_number)
        list_numbers.append(user_number)

        if user_number < 1 or user_number > 100:
            print("Você errou, você deve digitar um número entre 1 e 100!")
            continue

        hit = secret_number == user_number
        smaller = user_number < secret_number
        larger = user_number > secret_number

        if hit:
            print("Parabéns, você acertou após {} tentativas!".format(count))
            print("Pontuação na partida: {} ".format(score))
            break
        else:
            if smaller:
                print("Você errou! Tente um numero maior!")
            elif larger:
                print("Você errou! Tente um numero menor!")

            score -= abs(secret_number - user_number)
            print(list_numbers)

        count += 1

    print("*********************************")
    print("Fim de Jogo!")
    print("*********************************")


if __name__ == "__main__":
    guessing()
