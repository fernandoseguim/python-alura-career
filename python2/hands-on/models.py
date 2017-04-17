# -*- coding: utf-8 -*-
from __future__ import print_function

from math import pow


class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        if(len(nome) < 3):
            raise InvalidArgumentError("nome deve ter pelo menos 3 caracteres")

        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def to_string(self):
        print('Nome: %s, Telefone: %s, Empresa: %s, Total de curtidas: %d' % (self.nome, self.telefone, self.empresa, self.get_like()))

    def set_like(self):
        self.__curtidas += 1

    def get_like(self):
        return self.__curtidas

    @classmethod
    def create_profile_from_csv(classe, path_file):

        file = open(path_file, 'r')
        profiles = []

        for line in file:
            values = line.split(',')
            if(len(values) is not 3):
                raise ValueError('Uma linha no arquivo %s deve conter 3 valores' % path_file)
            profiles.append(Perfil(*values))

        file.close()

        return profiles

class Perfil_VIP(Perfil):

    def __init__(self, nome, telefone, empresa,apelido=''):
        self.super_class = super(Perfil_VIP, self)
        self.super_class.__init__(nome, telefone, empresa)
        self.apelido = apelido

    def get_creditos(self):
        return self.super_class.get_like() * 10.0

    def to_string(self):

        print('Nome: %s, Telefone: %s, Empresa: %s, Total de curtidas: %d, Apelido: %s' % (self.nome,
                                                                                           self.telefone,
                                                                                           self.empresa,
                                                                                           self.super_class.get_like(),
                                                                                           self.apelido))

class InvalidArgumentError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)

class Data(object):

    def __init__(self, dia, mes, ano):
        self.dia, self.mes, self.ano = dia, mes, ano

    def format_data(self, separador):
        print('%d%s%d%s%d' % (self.dia, separador, self.mes, separador, self.ano))


class Pessoa(object):

    def __init__(self, nome, peso, altura):
        self.nome, self.peso, self.altura = nome, peso, altura

    def calc_imc(self):
        imc = self.peso / pow(self.altura,2)
        print('IMC do %s é %.2f' % (self.nome, imc))


