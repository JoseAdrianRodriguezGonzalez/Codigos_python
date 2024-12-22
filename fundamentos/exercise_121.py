# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:36:25 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripcion:Escribe una funcion que reciba como parámetros dos tuplas con dos números fltoantes cada una, las cuales reperesnta dos puntos en el 
espacio euclideano 2D, y que devuelva la distancia entre esos dos puntos.
def distancia_euc(t1,t2):
    pass
distancia_euc((6,3),(9,4)
              output:
                  distancia"""

def distancia_euc(t1,t2):
    return ((t2[1]-t1[1])**2+(t2[0]-t1[0])**2)**(1/2)
print(distancia_euc((5,0), (8,4)))
print(distancia_euc((6,3),(9,4)))
def distancia_gen(t1,t2):
    s=0
    for i in range(len(t1)):
       s+= (t1[i]-t2[i])**2
    return s**(1/2)
print(distancia_gen(((1,2,3,4)), ((2,3,4,5))))