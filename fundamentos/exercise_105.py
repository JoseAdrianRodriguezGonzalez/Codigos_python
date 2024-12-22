# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 00:33:10 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Dado un string (definido por ti), escribe un
programa que genere un diccionario, en donde la llave es la
posición de cada caracter y el valor el caracter:
    
	string = 'hola'

output:
    d = {0:'h', 1:'o', 2:'l', 3:'a'}
"""

string = 'hola'
d={}
for i in range(len(string)):
   d[i]=string[i] 
print(d)