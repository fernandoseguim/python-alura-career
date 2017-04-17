# -*- coding: utf-8 -*-

def insere_na_lista(lista, item):
    lista.append(item)

    return lista


def remove_da_lista(lista, item):
    if lista.__contains__(item):
        lista.remove(item)
    else:
        print "item não removido pois não está na lista"

    return lista


def main():

    lista = []
    controle = 1

    while (controle != 0):
        item = raw_input("Informe um valor para inserir na lista: ")
        insere_na_lista(lista, item)
        controle = int(raw_input("Digite 1 para continuar ou 0 para sair: "))

    print lista

    item = raw_input("Informe qual item deve ser removido da lista: ")
    remove_da_lista(lista, item)

    print lista

main()