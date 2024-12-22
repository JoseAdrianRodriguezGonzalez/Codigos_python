# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:52:52 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adria´n
Descripción:Lo mismo que el anterior ejercicio , pero solo puedden agregarse
a la lista aquellos números aletorio que sean divisbles entre 2 y 7. Tiene que
a
haber 100 elementos numeros en la lista
"""

import random as rn
lista=[]
while len(lista)<100:
    n=rn.randint(100,1000)
    if n%2==0 and n%7==0:
        lista.append(n)
print(lista)