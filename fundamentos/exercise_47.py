# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:54:42 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripción:  Dada una lista de listas (creada por ti
directamente en el código), donde cada lista interna
contiene números flotantes, escribe un programa que genere
una nueva lista en donde las listas internas de la lista
original estén ordenadas de forma descendente.

lista = [[1.4, 3.5, 5.6], [2.5, 1.3, 7.8], [5.6, 3.4, 8.7, 10.3]]

output:
    [[5.6, 3.5, 1.4], [7.8, 2.5, 1.3], [10.3, 8.7, 5.6, 3.4]]
"""
lista = [[1.4, 3.5, 5.6], [2.5, 1.3, 7.8], [5.6, 3.4, 8.7, 10.3]]

for i in lista:
    i.sort(reverse=True)
print(lista)
            
        