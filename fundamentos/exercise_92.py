# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:02:15 2024

exercise_92

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una tupla de tuplas, en donde cada tupla
interna está formada por 2 números enteros, escribe un
programa que genere una lista que contenga aquellos pares de
tuplas que sean simétricas (a,b) (b,a).

tupla = ((1, 2), (8, 2), (9, 5), (2, 1), (2, 8), (5, 4))

output:
    [(1, 2), (2, 1), (8, 2), (2, 8)]
    """

tupla = ((1, 2), (8, 2), (9, 5), (2, 1), (2, 8), (5, 4))
lista=[]
for i in tupla:
    if i[::-1] in tupla:
       lista.append(i) 
print(lista)