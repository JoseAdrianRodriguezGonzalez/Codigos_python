# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:13:17 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripción: Dada una lista de listas con números enteros
(creada por ti directamente en el código) escribe un
programa que imprima la sublista cuya suma de elementos es
la mayor.
    
lista = [[1, 2, 3], [3, 4, 5], [1, 1, 2]]	

output:
    La lista con la suma mayor es: [3, 4, 5], cuya suma es 12
-----------------------------------------------------------
"""
lista = [[1, 2, 3], [3, 4, 5], [1, 1, 2]]	
mayor=lista[0]
suma=0
suma_anterior=0
for i in lista[0]:
    suma_anterior+=i
for i in lista:
    for j in i:
        suma+=j
    if suma>suma_anterior:
        mayor=i
        suma_anterior=suma
    suma=0
print(f'la lista con la mayor suma es : {mayor} cuya suma es {suma_anterior}')