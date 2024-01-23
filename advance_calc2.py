
'''Calculadora que reciba 2 números y realice la operación aritmética
que el usuario desee. Puede escoger entre sumar, restar, multiplicar y dividir'''

import os
os.system('clear')

def calculator(x, y, z): #x, y, z corresponden a n1, n2, o, osea los valores con los que se trabaja
    if z == 1: 
        return x + y
    elif z == 2:
        return x - y
    elif z == 3:
        return x * y
    elif z == 4:
        if y == 0: print(div0)
        else: return x / y 
    elif z == 5:
        if y == 0: return f"\nSUMA = {x + y} \nRESTA = {x - y} \nMULTIPLICACIÓN = {x * y} \nDIVISIÓN = {div0}"
        else: return f"\nSUMA = {x + y} \nRESTA = {x - y} \nMULTIPLICACIÓN = {x * y} \nDIVISIÓN = {x / y}"
    else: return "::FAIL, invalid option::"
n1 = float(input("Ingrese el primer valor: "))
n2 = float(input("Ingrese el segundo valor: "))

print("::::MENÚ CALCULADORA::::")
div0 = "No es posible dividir en cero"
print("[1] para SUMAR")
print("[2] para RESTAR")
print("[3] para MULTIPLICAR")
print("[4] para DIVIDIR")
print("[5] TODAS LAS OPERACIONES")

o = int(input("Digite una opcion:"))

ans = calculator(n1, n2, o)
print("Resultado = ", ans)