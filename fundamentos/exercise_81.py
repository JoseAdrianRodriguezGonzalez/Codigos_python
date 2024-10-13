# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:34:43 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripición: Dada una utple llena de objetos, escribe un programa para encontrar
los elementos repetidos y que genere una lista con ellos.
En la nueva lsita, no debe de haber elementos repetidos 

t=('a','b',1,2,3,'c','e',[1,2],1,3,3)
output:
    ['a','c',1,3]
"""

t=('a','b',1,2,3,'c','e',[1,2],1,3,3)
lista=[]
for i in t:
    if t.count(i)>1 and not(i in lista):
        lista.append(i)
print(lista)
