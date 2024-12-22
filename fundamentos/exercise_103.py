# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 23:39:52 2024

exercise_103

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dadas dos listas llenas con strings y números
enteros, escribe un programa que genere un diccionario,
donde las llaves son los objetos de la primera lista, y
los valores los objetos de la segunda. Iterar para la menor
de las listas.

lista_1 = ['a', 1, 'b', 'd', 6]
lista_2 = [67, 'hola', 26]

output:
    {'a':67, 1:'hola', 'b':26}
"""
dic={}

lista_1 = ['a', 1, 'b', 'd', 6]
lista_2 = [67, 'hola', 26]
for i in range(len(lista_2)):
    dic[lista_1[i]]=lista_2[i]
print(dic)