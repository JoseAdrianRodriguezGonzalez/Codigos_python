# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:24:23 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reciba un número entero
positivo y que multiplique sus dígitos de forma recurrente
hasta que solo quede 1 dígito. Utiliza la función del
ejercicio previo como complemento.
"""

def multiplicaion_recurrente(n):
    while n>=10:
        producto=1
        while n>0:
            producto*=n%10
            n//=10
            if n==0:
                break
        return producto
    return n
print(multiplicaion_recurrente(589))