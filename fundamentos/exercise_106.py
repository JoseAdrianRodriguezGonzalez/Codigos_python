# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 00:34:44 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Dados dos diccionarios, escribe un programa que
devuelva una lista con las llaves que ambos comparten.

d_1 = {'a':'hola', 'b':5, 'c':7}
d_2 = {'d':'mundo', 'a':8, 'b':7}

output:
    ['a', 'b']
"""
d_1 = {'a':'hola', 'b':5, 'c':7}
d_2 = {'d':'mundo', 'a':8, 'b':7}

lista=[]
for key in d_1.keys():
    if key in d_2:
        lista.append(key)
print(lista)