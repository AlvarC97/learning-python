'''
Script description
Cree una función que genere el lanzamiento de dados (1-6)
y que muestre por pantalla el mensaje ganador cuando 
genere un par de SEIS, de lo contrario el 
mensaje dirá: SIGUE INTENTANDO
'''
#Importo biblioteca para generar números aleatorios enteros
from random import randint

#Lanzar y generar los valores de los dos dados 
def dices():
    dice1 = randint(1, 6) #(dado 1)
    dice2 = randint(1, 6) #(dado 2)

    return dice1, dice2
d = dices()
d1 = d[0]
d2 = d[1]
print("Dices: ", d)
print("Dice1: ", d1)
print("Dice2: ", d2)
if d1 == 6 and d2 ==6:
    print("GANADOR")
else: print("SIGUE INTENTANDO")


