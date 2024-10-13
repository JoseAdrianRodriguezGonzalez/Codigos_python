# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:21:44 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripición:Dad una tuple llena con objetos y un número entero n,escribe un 
program para eliminar el objeto en la posición n.
Vlaida que n sea menor a la longitud de la tupla

t=('a','b',1,2,3,'c','e',[1,2])
n=4
output:
    ('a','b',1,3,'e',[1,2])
"""

t=('a','b',1,3,'c','e','c',[1,2])
n=4
if n<len(t):
   lista=list(t)
   lista.pop(n)
   t=tuple(lista)
print(t)
"""
t=t[:n]+t[n+1:]
"""
