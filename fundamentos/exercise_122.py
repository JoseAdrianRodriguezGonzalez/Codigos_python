# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:34:56 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reciba un número entero
positivo n, y que devuelva una lista de listas que 
represente una matriz de nxn llena de ceros.

def matriz(n):
	pass

matriz(3)

output:
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
"""

def matriz(n):
    return [[0 for j in range(n)]for i in range(n)]
lista=matriz(3)
print(lista)