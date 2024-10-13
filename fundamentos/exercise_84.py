# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:00:10 2024
exercise_84

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una lista de tuplas, donde cada tupla
está llena con objetos de diferente tipo, y dado un
número entero positivo; escribe un programa que reemplace el
último elemento de cada tupla por el número entero.

lista = [('a', 3, 4), ('b', 'c'), (4, 5, 'd', 'e'), (7, 'a', 'b', 8)]
n = 14

output:
    [('a', 3, 14), ('b', 14), (4, 5, 'd', 14), (7, 'a', 'b', 14)]

"""

lista = [('a', 3, 4), ('b', 'c'), (4, 5, 'd', 'e'), (7, 'a', 'b', 8)]
n=14
c=0
for i in lista:
    lista_temp=list(i)
    lista_temp.pop()
    lista_temp.append(n)
    i=tuple(lista_temp)
    lista[c]=i
    c+=1
print(lista)
    