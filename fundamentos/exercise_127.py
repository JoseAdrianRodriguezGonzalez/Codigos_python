# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:18:59 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reciba un número entero
positivo y que devuelva el producto de sus dígitos 
individuales

def producto_digitos(n):
	pass

producto_digitos(589)
output: 
	5*8*9 = 360

producto_digitos(1578)
output: 
	1*5*7*8 = 280

"""

def producto_digitos(n):
    numeros=[s for s in str(n)]
    multiplicacion=1
    for i in numeros:
        multiplicacion*=int(i)
    return multiplicacion
print(producto_digitos(589))
print(producto_digitos(360))