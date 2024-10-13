# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 01:48:08 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa para calcular el factorial
de un número entero positivo ingresado por el usuario. Valida que el nÃºmero sea positivo.

El factorial se define como:
	n! = 1 * 2 * 3 * 4 * ... * n
    
input:
    Dame un nÃºmero entero positivo: 5
output:
    El factorial de 5 es 120

input:
    Dame un nÃºmero entero positivo: -5
output:
    Â¡Error! El nÃºmero debe ser positivo.
"""
num=int(input('Dame un entero positivo'))
factorial=1
if num<0 :
    print("El numero debe ser positivo")
else:
    if num==0:
        num=1
    for i in range(num):
        factorial*=(i+1)
        print(factorial)
    print(f'el factorial de {num} es {factorial}')