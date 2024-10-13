# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:30:39 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dado un string (defínelo tú en el código),
escribe un programa que lo separe por espacios en una
lista de strings, y que genere una nueva lista que
contenga la longitug de cada substring generado.

s = 'anita lava la tina'
l_s = ['anita', 'lava', 'la', 'tina']

output:
    [5, 4, 2, 4]

"""

s = 'anita lava la tina'
l_s=s.split()
tam=[]
for i in l_s:
    tam.append(len(i))
print(tam)