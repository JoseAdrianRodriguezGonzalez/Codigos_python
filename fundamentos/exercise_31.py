# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 05:12:33 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
5@author: Rodríguez González José Adrián
Descripción: Escribe un programa que pida un número entero
positivo al usuario (valida la entrada) y que lo transforme
a binario, imprimiendo cada dígito de forma  inversa e independiente.
 Utiliza el ciclo while.

input:
	Dame un número (entero positivo): 4

output:
	0
	0
	1

input:
	Dame un número (entero positivo): 5

output:
	1
	0
	1
"""
num=int(input("Dame un entero positivo"))
residuo=0
while num>0:
    residuo=num%2
    num//=2
    print(residuo)
