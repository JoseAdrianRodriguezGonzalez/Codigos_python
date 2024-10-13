# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:59:57 2024
exercise_81

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dado un string, escribe un programa usando una
comprensión de listas para crear una nueva lista que contenga
las palabras 'consonante', 'vocal' u 'otro' para cada 
caracter del string.

s = 'hola12'

output:
    lista= ['consonante', 'vocal', 'consonante', 'vocal', 'otro', 'otro']
"""

s = 'hola12'
vocales='AEIOUaeiou'
lista=['vocal' if i in vocales else 'consonante' if i.isalpha()  else 'otro' for i in s]
print(lista)