# -*- coding: utf-8 -*-

from __future__ import print_function

file = open('perfis.csv', 'r')

for line in file:
    print(line)

file.close()


# new_file = open('perfis_novos.csv', 'w+')
# new_file.write('Joana Maria Darque, 11955556454, Taverna \n')
# new_file.write('Tom Renques, 11977776454, Roliúdi \n')
#
# for line in new_file:
#      print(line)
#
# new_file.close()