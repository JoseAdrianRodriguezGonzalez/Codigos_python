# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:59:23 2024

exercise_79

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dado un string, escribe un programa para
separarlo por espacios y usando dos comprensiones de listas
genere dos nuevas listas, una que contenga los substrings
que sean solo letras, y otra que contenga aquellos que sean
solo números. Los substrings que sean combinaciones de 
letras y números, se ignoran.

s = 'Hola Mundo34 123 q56ue t12al 678 mucho gusto 456'

output:
    lista_s = ['Hola', 'mucho', 'gusto']
    lista_n = ['123', '678', '456']
"""
s = 'Hola Mundo34 123 q56ue t12al 678 mucho gusto 456'
lista_s=[i for i in s.split() if i.isalpha()]
lista_n=[i for i in s.split() if i.isnumeric()]
print(lista_s)
print(lista_n)

