# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:00:46 2024
exercise_86

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una lista de tuplas, donde cada tupla
interna contiene números flotantes, escribe un programa que
devuelva una nueva lista con las tuplas internas ordenadas
de forma descendente.

lista = [(1.4, 6.7, 3.7), (2.5, 10.7), (11.8, 1.7, 9.5), (9.4, 1.3, 10.5)]

output:
    [(6.7, 3.7, 1.4), (10.7, 2.5), (11.8, 9.5, 1.7),
	(10.5, 9.4, 1.3)]
"""

lista = [(1.4, 6.7, 3.7), (2.5, 10.7), (11.8, 1.7, 9.5), (9.4, 1.3, 10.5)]
nueva=[]
for i in lista:
    lista_t=list(i)
    lista_t.sort(reverse=True)
    nueva.append(tuple(lista_t))
print(nueva)