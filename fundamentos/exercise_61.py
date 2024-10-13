# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:23:39 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dada una lista con strings (creada por
ti directamente en el código) que contengan números y
letras, escribe un programa que genere dos listas, una que
contenga los strings que son solo números y otra que
contenga los strings que son solo letras. Los strings con
letras y números no se agregan a ninguna.

lista = ['abc', 'ab12', '456', '12vb', 'tye', '567', 'ad34']

output:
    numeros: ['456', '567']
    letras: ['abc', 'tye']
	
"""

lista = ['abc', 'ab12', '456', '12vb', 'tye', '567', 'ad34']
alfa=[]
num=[]
for i in lista:
    if i.isalpha():
        alfa.append(i)
    elif i.isnumeric():
        num.append(i)
print(alfa)
print(num)