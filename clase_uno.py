#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:56:18 2021

@author: ivandavid
"""

print('Hello World')

# VARIABLES
a = 3
print(type(a))
a = "Hola"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))

# OPERACIONES
a = 5
b = 2
c = a + b
print(c)

a = 5
b = 2
c = a - b
print(c)

a = 5
b = 2
c = a * b
print(c)

a = 5
b = 2
c = a / b
print(c)

a = 5
b = 2
c = a // b
print(c)

# potencia
a = 5
b = 2
c = a ** b
print(c)

# raiz
a = 9
c = a ** (1/3)
print(c)

"""import math
raiz = math.sqrt(25)
print(raiz)"""

# TIPOS DE DATOS

# string str
a = "Hola Mundo"
a = 'Hola Mundo'
b = "I can't do it"
c = 'Alias "Paez"'

# entero int
a = 5

# decimal float
a = 5.6

# booleano bool
x = True
y = False

# CONVERSIONES ENTRE TIPOS DE DATOS

# convertir de x a entero
a = '3'
y = int(a)
print(y)
print(type(y))

# convertir de x a decimal
a = '3'
y = float(a)
print(y)
print(type(y))

# convertir de x a string
a = '3'
y = str(a)
print(y)
print(type(y))

# CONCATENACIONES
a = 'hola'
b = 'mundo'
c = a + ' ' + b

a = 'hola'
b = a * 5


# CAPTURAR POR PANTALLA
nombre = input('Digite su nombre')
print('Hola', nombre)


# realizar un algoritmo que sume dos numeros e imprima su resultado
a = float(input('Digite el primer numero: '))
b = float(input('Digite el segundo numero: '))
suma = a + b
print("La suma es: ", suma)

# realizar un algoritmo que lea un numero y lo eleve al cuadrado
a = float(input('Digite el numero que desee elevar al cuadrado'))
b = a ** 2
print(f'el resultado del numero {a}  elevado al cuadrado es: {b}')

# realizar un algoritmo que tome el valor de un pproducto, le aplique el 20%
# de descuento, imprima el valor del producto inicial, el valor con descuento
# y el valor ahorrado
a = float(input('Digite el valor del producto $'))
descuento = a * 0.2
final = a - descuento
print(f'el valor del producto es: ${a}')
print(f'el valor final del producto es: ${final}')
print(f'el valor ahorrado es: ${descuento}')
