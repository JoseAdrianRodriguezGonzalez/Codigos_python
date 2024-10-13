# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:01:46 2024

exercise_89

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez GOnzález José Adrián
Descripción: Dada una lista llena con strings, escribe un
programa que genere una nueva lista llena de tuplas del tipo
(index, string). El index es la posición del string dentro
de la lista.

lista = ['hola', 'mundo', 'que', 'tal', 'aqui', 'todo', 'bien']

output:
    [(0, 'hola'), (1, 'mundo'), (2, 'que'), (3, 'tal'),
	(4, 'aqui'), (5, 'todo'), (6, 'bien')]
    """

lista = ['hola', 'mundo', 'que', 'tal', 'aqui', 'todo', 'bien']
lista_index=[]
for i in range(len(lista)):
    lista_index.append((i,lista[i]))
print(lista_index)