# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:03:04 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripcion:
    Escribe una funcion que reciba como parametro
    un numero entero positivo n, y que devuelva el factorial de ese numero 
    def factorial(n):
        pass
    facotrial(5):
        
   """
def factorial(n):
    """
    Devuelva el facotrial de forma recursiva

    Parameters
    ----------
    n : entero positivo
        DESCRIPTION.

    Returns
    -------
    el numero en factorial
        DESCRIPTION.

    """
    if n==0:
        return 1
    else:
        return factorial(n-1)*n
print(factorial(5))
##Sin recurisvidad
def factorial2(n):
    factorial=1
    if n==0:
        return 1
    for i in range(1,n):
        factorial*=i
print(factorial(6))