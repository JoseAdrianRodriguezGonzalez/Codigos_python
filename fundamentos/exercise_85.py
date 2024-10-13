# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:00:39 2024

exercise_85

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una lista de tuplas, escribe un programa
que genere una nueva lista sin las tuplas vacías de la lista
original

lista = [('a', 3, 4), (), (4, 5, 'd', 'e'), (), (), (7, 'a', 'b', 8)]

output:
    [('a', 3, 4), (4, 5, 'd', 'e'), (7, 'a', 'b', 8)]
"""

lista = [('a', 3, 4), (), (4, 5, 'd', 'e'), (), (), (7, 'a', 'b', 8)]
nueva=[x for x in lista if len(x)>0]
print(nueva)