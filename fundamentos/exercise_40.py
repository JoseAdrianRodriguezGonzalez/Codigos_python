# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:13:33 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza

Descripción: Dada una lista de listas con números enteros
(creada por ti directamente en el código) escribe un
programa que genere una nueva lista que contenga las
diferencias entre cada par de números consecutivos.
    
        
lista = [5, 6, 1, 2, 5, 6, 7]	

output:
    [-1, 5, -1, -3, -1, -1]
	(5-6), (6-1), (1-2), (2-5), (5-6), (6-7)
"""

lista = [5, 6, 1, 2, 5, 6, 7]	
listadiferencias=[]
for i in range(len(lista)-1):
    dif=lista[i]-lista[i+1]
    
    listadiferencias.append(dif)
print(listadiferencias)

