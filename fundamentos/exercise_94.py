# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:58:07 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripición:Dadas dos listas llenas con numeros enteros las cuales son iguales
excepto una tiene un objeto menos que la otra, escribe un programa que devuelva
cual es el objeto que falta.
lista_1=[4,5,6,1]
lista_2=[4,5,6,1,2]
output:
    Falta el dos
"""

lista_1=[4,5,6,1]
lista_2=[4,5,6,1,2]
a=set(lista_1)
b=set(lista_2)
numero=a.symmetric_difference(b)
print(f'falta el {numero} ')
