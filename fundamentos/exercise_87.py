# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:01:01 2024
exercise_87

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una tupla llena con objetos de diferentes
tipos (string, números enteros, números flotantes, listas y
tuplas), escribe un programa que cuente cuántos objectos hay
de cada tipo.

tupla = (1, 3, 4.5, 'hola', [1, 2], [3, 4], (t,) (y, t), (4, 5))

output:
    Hay 1 string
    Hay 2 enteros
    Hay 1 flotantes
    Hay 2 listas
    Hay 3 tuplas
"""
tupla = (1, 3, 4.5, 'hola', [1, 2], [3, 4], ('t',) ,('y', 't'), (4, 5))
lista=[0,0,0,0,0]
nombres=['strings','enteros','flotantes','listas','tuplas']
for i in tupla:
    if type(i)==str:
        lista[0]+=1
    elif type(i)==int:
        lista[1]+=1
    elif type(i)==float:
        lista[2]+=1
    elif type(i)==list:
        lista[3]+=1
    elif type(i)==tuple:
        lista[4]+=1
        
for i in range(len(nombres)):
    print(f'Hay {lista[i]} {nombres[i]}')