# -*- coding: utf-8 -*-


from datetime import datetime


def cadastrar():
    usuario = {}
    nome = raw_input("Informe o seu nome: ")
    ano_nascimento = int(raw_input('Informe o ano do seu nascimento: '))

    usuario['nome'] = nome
    usuario['idade'] = datetime.now().year - ano_nascimento

    return usuario


def incluir_na_lista(usuarios, usuario):
    usuarios.append(usuario)
    return usuarios


def remover_da_lista(usuarios, usuario):
    usuarios.remove(usuario)

    return usuarios

def main():

    usuarios = []

    controle = 1
    while (controle != 0):
        usuario = cadastrar()
        usuarios = incluir_na_lista(usuarios, usuario)

        controle = int(raw_input('Digite 1 para continuar ou 0 pra sair: '))


    print usuarios

    p = int(raw_input("Informe a posição do usuário que deve ser removido: "))

    remover_da_lista(usuarios, usuarios[p])
    print usuarios

main()
