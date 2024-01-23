import os  #Para limpiar pantalla
from random import randint, uniform
'''
randint => Genera número aleatorios enteros entre un rango especificado 
uniform => Genera números aleatorios flotantes o decimales en un rango especificado 
'''

os.system('clear')

n1 = randint(1, 100)
n2 = uniform(1, 100)

print(n1)
print(n2)