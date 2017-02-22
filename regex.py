# -*- coding: utf-8 -*-
from re import match, findall

resultado = match('Py', 'Python')
print resultado.group()

# quando a função match não encontra um valor ele retorna um objeto do tipo NoneType
resultado = match('py', 'Python')
print type(resultado)

#Expressões regulares são uma alternativa para contornar o resultado anterior, isto é,
# possibilitanto uma busca idependente das letras serem maiúsculas ou minúsculas
resultado = match('[pP]y', 'Python')
print resultado.group()

resultado = findall('[A-Za-z]y', 'Python ou Jython')
print resultado

resultado = findall('[A-Za-z]y[A-Za-z]+', 'Python ou Jython ou Pypy')
print resultado

resultado = findall('(\wy\w+)', 'Python ou Jython ou Pypy')
print resultado

resultado = findall('(\wy\w+\d)', 'Python3 ou Jython2 ou Pypy')
print resultado

resultado = findall('[A-Za-z]+\d?', 'Python3 ou Jython ou Pypy3')
print resultado

resultado = findall('(\wy\w+\d*)', 'Python3 ou Jython2 ou Pypy3')
print resultado

resultado = findall(r'[A-Za-z]y[A-Za-z]+', 'Python3 ou Jython ou Pypy3')
print resultado

resultado = match(r'^#', '#comentarios começam com hashtag')
print resultado is None

lista = ['http://alura.com.br', 'http://www.alura.com.br', 'http://alura.com']

resultados = []
for item in lista:
    resultado = findall(r'.*br$', item)
    if (resultado != []):
        resultados.append(resultado[0])
print resultados

padrao = raw_input("Padrão: ")
resultados = findall(r'^'+padrao+r'\w+', 'Fernando Gabriela Silvia Dora Flavio')


print resultados

