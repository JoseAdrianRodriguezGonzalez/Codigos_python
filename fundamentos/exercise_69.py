# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:58:06 2024
exercise_69

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Dada una lista de listas llenas con números
enteros, escribe un programa que genere una copia de la
lista original de manera profunda y verificar que
las listas internas efectivamente son diferentes.

lista = [[3, 4, 5], [6, 7, 8], [9, 0, 2]]

output:
    new_lista = [[3, 4, 5], [6, 7, 8], [9, 0, 2]]
    
output:
    new_lista[0] is lista[0] --> False
    new_lista[1] is lista[1] --> False
    new_lista[2] is lista[2] --> False
"""

lista = [[3, 4, 5], [6, 7, 8], [9, 0, 2]]
lista_n=[]
for i in lista:
    temp=[]
    for j in i:
        temp.append(j)
    lista_n.append(temp)
for i in range(len(lista)):
    print(lista_n[i] is lista[i])