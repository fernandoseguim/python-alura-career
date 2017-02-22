# -*- coding: utf-8 -*-

from re import *

def create(names):
    name = raw_input("\nInforme o name do usuário a ser cadastrado: ")
    names.append(name)


def delete(names):
    name = raw_input("\nInforme o name do usuário a ser removido: ")
    names.remove(name)


def update (names):
    name = raw_input('Informe o nome a ser atualizado: ')
    new_name = raw_input('Informe o novo nome: ')
    i = names.index(name)
    names[i] = new_name


def read_all(names):
    print ''
    for nome in names:
        print nome


def find(names):
    padrao = raw_input('Informe o nome que deseja procurar: ')

    list_names = []
    for name in names:
        item_name = findall(r'^'+padrao+r'\w+', name)
        if (item_name != []):
            list_names.append(item_name[0])
    print list_names


def main():

    names = []
    switch = ''

    while(switch != '0'):
        switch = raw_input("\nDigite:"
                           "\n1 para cadastrar"
                           "\n2 para listar todos"
                           "\n3 para atualizar"
                           "\n4 para remover"
                           "\n5 para procurar"
                           "\n0 para sair\n")

        if switch == '1':
            create(names)
        elif switch == '2':
            read_all(names)
        elif switch == '3':
            update(names)
        elif switch == '4':
            delete(names)
        elif switch == '5':
            find(names)

main()
