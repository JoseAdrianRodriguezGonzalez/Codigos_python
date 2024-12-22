# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:33:58 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reciba un número entero
positivo que representa un año y que devuelva si el año es
bisiesto o no (True/False).

Un año es bisiesto si es divisible entre 4, excepto si
también es divisible entre 100, en se caso debe ser
divisible entre 400


"""

def bisiesto(n):
    boo=False
    if not(n%4):
        boo=True
        if not(n%100):
            boo=False
            if not(n%400):
                boo=True
    return boo
print(bisiesto(1800))