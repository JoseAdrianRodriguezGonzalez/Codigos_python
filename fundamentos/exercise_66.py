# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:42:28 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripición: Dada una lista llena con números flotantes
y strings,,escribe un programa que devuelva el mínimo, el máximo 
y el promedio de los números de la lista
lista=[5.6,'a','b',7.8,'d',10.5,1.3]
output: 
    minimo: 1.3
    máxmio:10.5
    promedio:6.3
"""

lista=['z',5.6,'a','b',-7.8,'d',10.5,1.3]
sub=[]
prom=0
for i in lista:
    if type(i) ==float:
        sub.append(i)
        prom+=i
sub.sort()
mini=sub[0]
maxi=sub[-1]
print(f'minimo: {mini}')
print(f'maximo: {maxi}')
print(f'promedio: {prom/len(sub):.2f}')