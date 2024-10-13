# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:01:21 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Dada una lista de listas (creada por ti
directamente en el código), donde cada lista interna
contiene números flotantes y strings, escribe un programa
que modifique la lista original, para eliminar la primera
lista interna que contenga menos de 3 elementos.

lista = [[1.4, 'a', 'b'], ['c', 2.5], [5.6, 3.4], [8.7, 'e', 'f']]

output:
    [[1.4, 'a', 'b'], [5.6, 3.4], [8.7, 'e', 'f']]
"""


lista = [[1.4, 'a', 'b'], ['c', 2.5], [5.6, 3.4], [8.7, 'e', 'f']]
for i in lista:
    if len(i)<3:
        lista.remove(i)
print(lista)