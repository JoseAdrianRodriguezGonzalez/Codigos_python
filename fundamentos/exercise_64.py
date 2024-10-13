# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:33:42 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dada una lista llena con strings (creada por
ti directamente en el código), escribe un programa que
genere un string formado por la concatenación de los
strings de la lista, separados entre sí por un '+', pero
solo aquellos cuya longitud es mayor que 3.

l_s = ['anita', 'lava', 'la', 'tina', 'con', 'mucho', 'esfuerzo']

output:
    anita+lava+tina+mucho+esfuerzo

"""

l_s = ['anita', 'lava', 'la', 'tina', 'con', 'mucho', 'esfuerzo']
n=[]
s=''
for i in l_s:
    if len(i)>3:
        n.append(i)
s='+'.join(n)
print(s)