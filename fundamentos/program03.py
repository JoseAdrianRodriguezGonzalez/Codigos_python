# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:22:18 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Basic While loop
"""
# Ciclo no definido se ejecuta el bloque de instrucciones por un numero no
# definido de veces)
#El bloque de contrl while re´pite un bloque de instrucciones
#Mientras la condición se evalúe como verdadera#Estructura general del bloque while
#while(condicion):
#   bloque de instruciones

n=10 #referencia
i=0
suma=0 #acumulador
while i<n:
    i+=1
    suma+=i
print(f'la suma es {suma} ')

"""
n  i   suma     i<n
10 0   0        True
   1   1        True
   2   3        True
   3   6        True
   4   10        True
   5   15        True
   6   21        True
   7   28        True
   8   36        True
   9   45        True
   10  55        False
"""
n=10 
i=0
suma=0
while i<n:
    i+=1
    if i==3:
        break
    suma+=i
print(f'{suma}')
"""
n  i   suma     i<n      i==3
10 0   0        True     ...
   1   1        True     False
   2   3        True    False
   3                     True
  
"""

#Continue
n=10
i=0
suma=0
while i<n:
    i+=1
    if (i==3) or (i==5):
        continue
    suma+=i
print(f'{suma}')


#else

n=10 
i=0
suma=0
while i<n:
    i+=1
    if i==3:
        break
    suma+=i
else:
    print(f'La suma es {suma}')
# Se ejecuta solo cuando se termina el ciclo por completo, es decir cuando no 
#haya un break