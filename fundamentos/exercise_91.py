# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:02:05 2024
exercise_91

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dadas dos listas de tuplas, donde cada tupla
interna contiene objetos de diferentes tipos, escribe un
programa que genere una lista con los elementos comunes de
las dos listas. Los elementos de la nueva lista deben
ser único (no hay repetición)

lista_1 = [(1, 'a'), ('b', 4.5), (1, 6.7), ('n', 6, 7.8), (1, 6.7)]
lista_2 = [(1, 6.7), ('h', 5, 6), (1, 6.7), ('b', 4.5), ('l', 1, 6.7)]

out:
    [(1, 6.7), ('b', 4.5)]
"""
lista_1 = [(1, 'a'), ('b', 4.5), (1, 6.7), ('n', 6, 7.8), (1, 6.7)]
lista_2 = [(1, 6.7), ('h', 5, 6), (1, 6.7), ('b', 4.5), ('l', 1, 6.7)]
lista_nueva=[]
for i in lista_1:
    if i in lista_2 and (i not in lista_nueva):
        lista_nueva.append(i)
print(lista_nueva)