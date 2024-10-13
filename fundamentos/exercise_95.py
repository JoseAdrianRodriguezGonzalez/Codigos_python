# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:10:06 2024



División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripición:Dadas tres listas llenas con numeros enteros escribe un programa que devuelva
todos los objetos unicos que comparten las tres listas.
lista_1=[1,2,3,4,5,6]
lista_2=[3,4,5,6,7,8]
lista_3=[1,3,4,6,8,9,10]
output:
    Comparten {3,4,6}
  """
lista_1=[1,2,3,4,5,6]
lista_2=[3,4,5,6,7,8]
lista_3=[1,3,4,6,8,9,10]
a=set(lista_1)
b=set(lista_2)
c=set(lista_3)
intersection_abc=a.intersection(b).intersection(c)
print(intersection_abc)