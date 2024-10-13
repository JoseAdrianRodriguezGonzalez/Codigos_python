# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:42:48 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dada una lista llena con strings (creada por
ti directamente en el código), escribe un programa
que devuelva cuál es el string más largo de la lista.

lista = ['merequetengue', 'hola', 'que', 'tal', 'mundo']

output:
    'merequetengue'

"""

lista = ['sa','merequetengue', 'hola', 'que', 'tal', 'mundo']
maximo=len(lista[0])
string_maximo=lista[0]
for i in lista:
    if len(i)>maximo:
        maximo=len(i)
        string_maximo=i
print(string_maximo)