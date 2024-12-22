# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:36:30 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripcion:  lo mismo que el anterior, pero que el string
generado contenga dígitos y las letras a-z (minúsculas)

input:
	6

output: 
    12bf4y
"""


import random as rn
n =int(input("Dame un numero entero menor a 20: "))
if n <20:
    string=""
    itr="abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(n):
        d=rn.choice(itr)
        string=string+d
    print(string)
else:
    print("Muy grande")