#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:22:46 2021

@author: jesus
"""
# Taller #1 IA - Jesús Hernández

# 1.
y = (((5+2-5)**2)*((5+8)/(2-30)))/((2*5)-3)
print(f'El resultado es {y}')

# 2.
z = 5
n = 3
m = z-n
y = (((((z+2-n)**2)*((m+8)/(2-30)))/((2*5)-3))**5)+(15*3)-(9/3)
print(f'El resultado es {y}')

# 3.
z = 5
n = (((8+2-4)**2)*((5+8+7)/2)-(30*5))/(2*5-3)
m = (z**2)*(3+n)
y = (((((((z+2-n)**2)*(m+8)/(2-30))/(2*5-3))**5)+(15*3)-(9/3))**2)-5/4
print(f'El resultado es {y}')

# 4.
presión = float(input('Ingrese el valor de la presión: '))
volúmen = float(input('Ingrese el valor del volúmen: '))
temperatura = float(input('Ingrese el valor del temperatura: '))
masa = (presión*volúmen)/(0.37*(temperatura+460))
print(f'El valor de la masa es {masa}')

# 5.
edad = int(input('Ingrese su edad: '))
pulsaciones = (200-edad)/10
print(f'El numero de pulsaciones que debe tener cada 10s es {pulsaciones}')

# 6.
cPersona1 = float(input('Ingrese la cantidad de $ de la personas #1: '))
cPersona2 = float(input('Ingrese la cantidad de $ de la personas #2: '))
cPersona3 = float(input('Ingrese la cantidad de $ de la personas #3: '))
total = cPersona1 + cPersona2 + cPersona3
pPersona1 = (cPersona1*100)/total
pPersona2 = (cPersona2*100)/total
pPersona3 = 100-(pPersona1 + pPersona2)
print(f'El porcentaje correspondiente para la persona #1 es {pPersona1}%')
print(f'El porcentaje correspondiente para la persona #2 es {pPersona2}%')
print(f'El porcentaje correspondiente para la persona #3 es {pPersona3}%')

# 7.
saldoInicial = float(input('Ingrese su saldo: '))
interes = (1.5)/100
saldoFinal = (saldoInicial*interes) + saldoInicial
print(f'Su saldo final con interes es ${saldoFinal:,}')

# 8.
sueldo = float(input('Ingrese su sueldo neto: '))
totalDescuento = 0
descuentos = {'Politica Publica': 0.01,
              'Seguro Social': 0.04,
              'Seguro Forzoso': 0.005,
              'Caja de Ahorro': 0.05
              }
for tipoDescuento, valorDescuento in descuentos.items():
    iDescuento = valorDescuento*sueldo
    print(f'El descuento en {tipoDescuento} es {iDescuento}')
    totalDescuento = totalDescuento + iDescuento
print(f'Su sueldo final es ${sueldo - totalDescuento:,}')

# 9.
palabras = int(input('Ingrese el numero de palabras: '))
centimetros = float(input('Ingrese los cm a utilizar: '))
colores = int(input('Ingrese la cantidad de colores a utilizar: '))

