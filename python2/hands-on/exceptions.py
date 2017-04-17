# -*- coding: utf-8 -*-
from __future__ import print_function

from models import *

arquivo = None
try:
    arquivo = open('files/perfis.csv', 'r')
    valores = arquivo.readline().split(',')

    perfil = Perfil(*valores)

    print('arquivo foi aberto')

    print(perfil.nome)

except (IOError) as error:
    print('Ocorreu um erro do tipo IOError na execução do programa: %s' % error)

except (TypeError) as error:
    print('Ocorreu um erro do TypeError na execução do programa: %s' % error)

except (Exception) as error:
    print('Ocorreu um erro não esperado na execução do programa: %s' % error)

finally:
    arquivo.close()
    print('arquivo foi fechado')
