# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 00:36:27 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Dado un diccionario con llaves string y 
valores string o números, escribe un programa que solicite
un valor al usuario (string) y devuelva una lista con las
llaves que tengan ese valor asociado.

d = {'a':5.6, 'b':'hola', 'c':7, 'd':8, 'e':'mundo', 
	'f':'que', 'g':'hola'}

input:
	Dame una palabra: hola
output:
    'hola' aparece en las llaves: [b, g]
"""


d = {'a':5.6, 'b':'hola', 'c':7, 'd':8, 'e':'mundo', 
	'f':'que', 'g':'hola'}
lista=[]
n=input("dame un string: ")
for k in d.keys():
    if d[k]==n:
        lista.append(k)
print(lista)