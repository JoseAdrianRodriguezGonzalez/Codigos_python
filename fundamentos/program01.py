# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:32:35 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Basic conditionals
"""

#Pyython utiliza la tabulación para indicar que un bloque 
#de instrucciones pertenece a un bloque de control.
#pytho no utiliza {} para agrupar bloqeus de control
#Estructura:if[condición]:
#           else:
#El condicional siempre evalua un valor de verdad (boolean)
# Que pueed ser el resltado de diversos operadores lógicos
#o de comparación
"""
num =10
if (num>=10):
    print('Positive or zero')
    print('Hello')
else:
    print('Negative')
print('finish')
"""

###Nested if
"""
n=float(input('Dame un número: '))
if (n>=0):
    if(n>0):
        print('Positive number')
    else:
        print('Zero')
else:
    print('Negative number')
"""
###Use of elif
n=float(input('Dame un número: '))
if(n>0):
    print('Positive number')
elif(n<0):#Si la primera condcion no se cumple, evalua la segunda
    print('Negative number')
else:
        print('Zero')