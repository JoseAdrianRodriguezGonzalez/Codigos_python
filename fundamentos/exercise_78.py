# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:59:09 2024
exercise_78

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián 
Descripción: Dado un string, escribe un programa para
separarlo por espacios y usando una comprensión de listas
que genere una nueva lista con cada substring convertido a
minúsculas.

s = 'Hola Mundo que tal mucho gusto'

output:
    lista = ['hola', 'mundo', 'que', 'tal', 'mucho', 'gusto']
"""

s = 'Hola Mundo que tal mucho gusto'
lista=[i.lower() for i in s.split()]
print(lista)