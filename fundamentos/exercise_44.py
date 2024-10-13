# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:27:00 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripcion: Dada una lista con números flotantes y un numero entero n (definidos por ti en el cósigo que),
Escribe un programa que devuelva los n números más pequeños de la lista
lista=[6.7,8.9,1.3,2.5,10.1]
n=3
output=[1.3,2.5,6.7]
"""
lista=[6.7,8.9,1.3,2.5,10.1]
n= int(input("Dame el numero: "))
if n<len(lista):
    lista.sort()
    peques=lista[:n]
else:
    print("Se sobrepasa de la longitud del arreglo")
print(peques)