# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:53:44 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dado un string (defínelo tú en el código),
escribe un programa que devuelva el número de vocales que
contiene.

s = 'Hola mundo que tal'

output:
    'Hola mundo que tal' Tiene 7 vocales
"""

s = 'Hola mundo que tal'
cont=0
for i in s:
    if i=='o'or i=='a' or i=='u' or i=='e' or i=='i':
      cont+=1
print(f'{s} tiene {cont} vocales')