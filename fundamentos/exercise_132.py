# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:51:39 2024

@author: USUARIO
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reciba una lista de números enteros yt devuelva el promedio, el minimo
y el maximo de la lsita
lsita=[90,34,1,134,56]
output: 
    promedio:2342
    min:1
    max:134
"""
def calculos(lista):
    """
    Parameters
    ----------
    lista : list
    Lista de numeros enteros.

    Returns
    -------
    TYPE
        Es una tupla del promedio, minimo, maximo

    """
    return sum(lista)/len(lista),min(lista),max(lista)
    
lista=[90,34,1,134,56]

mean,mini,maxi=calculos(lista)
print(f'promedio:{mean}\nminimo:{mini}\nmaximo:{maxi}')