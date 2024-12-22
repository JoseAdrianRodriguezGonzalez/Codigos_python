# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:32:43 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripcion:  Escribe un programa que solicite al usuario un
número entero n (n<20) y que genere un string con n dígitos
(0-9) al azar. Validar que n sea < 20.

input:
	5

output:
    18496
"""
import random as rn
n =int(input("Dame un numero entero menor a 20: "))
if n <20:
    string=""
    for i in range(n):
        d=rn.randint(0, 9)
        string=string+str(d)
    print(string)
else:
    print("Muy grande")