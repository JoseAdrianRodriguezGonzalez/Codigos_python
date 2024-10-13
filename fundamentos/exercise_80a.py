# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:59:42 2024
exercise_80

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una lista de listas llena con números,
escribe un programa que use una comprensión de listas para
generar una nueva lista que 'aplane' la lista original;
es decir, que saque todos los elementos de las listas
internas y los coloque directamente en la nueva lista.

lista = [[7, 3, 4], [1, 9, 10], [6, 3, 4], [5, 2, 1]]

output:
    new_lista = [7, 3, 4, 1, 9, 10, 6, 3, 4, 5, 2, 1]

"""
lista = [[7, 3, 4], [1, 9, 10], [6, 3, 4], [5, 2, 1]]
n=[s for x in lista for s in x ]
print(n)