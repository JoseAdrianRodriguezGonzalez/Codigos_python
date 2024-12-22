# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 00:40:12 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Dada una lista llena con strings, escribe un
programa para crear un diccionario en donde las llaves son
cada uno de los strings de la lista y el valor es el número
de veces que ese string aparece en la lista.

lista = ['a', 'b', 'c', 'd', 'a', 'a', 'b', 'd', 'e']

output:
    {'a':3, 'b':2, 'c':1, 'd':2, 'e':1}
"""

lista = ['a', 'b', 'c', 'd', 'a', 'a', 'b', 'd', 'e']
d={}
for i in lista:
    d[i]=lista.count(i)
print(d)