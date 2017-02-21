# -*- coding: utf-8 -*-

print 'Lista ou array - são dinamicamente expansiveis'

membros_familia = ['Fulano de Tal', 'Ciclano de Tal', 'Dealtrano de Tal']
print membros_familia

membros_familia.append('Beltrano de Tal')
print membros_familia

print '\ntuplas - não são dinamicamente expansiveis'

membros_familia = ('Fulano de Tal', 'Ciclano de Tal', 'Dealtrano de Tal')
print membros_familia

#membros_familia.append('Beltrano de Tal')
#print membros_familia

print 'dicionários - são listas com a característica chave-valor'
membros_familia = {'pai': 'Fulano de Tal', 'mae':'Dona Maria', 'filho': 'Joaquim José'}
print membros_familia

print membros_familia.keys()
print membros_familia.values()

print membros_familia['pai']
print membros_familia['mae']
print membros_familia['filho']

pais = ('Fulano de Tal', 'Dona Maria')
filhos = ('Joaquim José', 'Maria Joaquina')

membros_familia = pais + filhos

print membros_familia
print type(membros_familia)

pais = ['Fulano de Tal', 'Dona Maria']
membros_familia = pais
filhos = ['Joaquim José', 'Maria Joaquina']

for filho in filhos:
    membros_familia.append(filho)

print membros_familia
print type(membros_familia)

estados = ('RJ','SP') + tuple(['MG','ES'])
print estados
print type(estados)

print max((10,2,7,9))
print min((10,2,7,9))

nomes = ('Leonardo', 'Flávio', 'Rômulo')
nomes_ordenados = sorted(nomes)
print nomes_ordenados