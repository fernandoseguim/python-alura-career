# -*- coding: utf-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def to_string(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)


class Data(object):

    def __init__(self, dia, mes, ano):
        self.dia, self.mes, self.ano = dia, mes, ano

    def format_data(self, separador):
        print '%d%s%d%s%d' % (self.dia, separador, self.mes, separador, self.ano)
