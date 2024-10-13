# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:57:42 2024

exercise_68

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Dada un lista llena con números flotantes
y listas de números flotantes, escribe un programa que
genere una lista con la longitud de las listas internas.

lista = [[3, 5, 6], 6.7, 6, [3.4, 2, 5.6], 34, [6.7, 2]]

output:
    new_lista = [3, 3, 2]
    """
lista = [[3, 5, 6], 6.7, 6, [3.4, 2, 5.6], 34, [6.7, 2]]
longitud=[]
for s in lista:
    if type(s)==list:
        longitud.append(len(s))

print(longitud)