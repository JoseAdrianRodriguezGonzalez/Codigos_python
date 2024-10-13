# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:14:09 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripción: Dadas dos listas con números enteros
(creadas por ti directamente en el código), la primera
más grande que la segunda, escribe un programa que
determine si la segunda lista está contenida dentro de la
primera.
    
lista_1 = [4, 5, 6, 7, 9, 10, 12, 5, 1]
lista_2 = [7, 9, 10]
output:
    True


lista_1 = [4, 5, 6, 7, 9, 10, 12, 5, 1]
lista_2 = [67, 1, 2]
output:
    False
"""


lista_1 = [4, 5, 6, 7, 9, 10, 12, 5, 1]
lista_2 = [67, 1 ,2]
contador=0
for i in lista_1:
    for j in lista_2:
        if i==j:
            contador+=1
        
if contador==len(lista_2):
    print(True)
else:
    print(False)
    