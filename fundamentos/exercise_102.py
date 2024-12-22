# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 23:39:52 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dado un diccionario con llaves string y valores
string o numéricos, escribe un programa que devuelva la suma
y el promedio de los valores numéricos.

d = {'a':5.6, 'b':'hola', 'c':7, 'd':8, 'e':'mundo', 'f':'que'}

output:
    suma: 20.6
    promedio: 6.86
"""


d = {'a':5.6, 'b':'hola', 'c':7, 'd':8, 'e':'mundo', 'f':'que'}
suma=0
count=0
for i in d.values():
    if type(i)==float or type(i)==int:
        suma+=i
        count+=1
print(f'suma={suma}')
print(f'promedio={(suma/count):.2f}')

        
