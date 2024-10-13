# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:15:03 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: Escribe un programa que solictie 3 número flotante al usuario y 
determina cuál de ellos es el mayor:
input: 
    Dame el númer 1:5.62
    Dame el númer 2:8.95
    Dame el númer 3:1.58
output:
    El número mayor es 8.95
"""
num_1=float(input('Dame el número 1: '))
num_2=float(input('Dame el número 2: '))
num_3=float(input('Dame el número 3: '))
if ((num_1>num_2) and(num_1>num_3)):
    print(f'El mayor es:  {num_1}')
elif((num_2>num_3) and(num_2>num_1)):
    print(f'El mayor es: {num_2}')
else:
    print(f'El mayor es: {num_3}')
#other way
mayor=num_1
if num_2>mayor:
    mayor=num_2
if num_3 > mayor:
    mayor=num_3
print(f'El numero mayor es {mayor}')