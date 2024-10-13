# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 04:52:31 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
descripción: Escribe un programa para obtener la estatura 
promedio de un grupo de personas cuyo número de miembros se desconoce. 
El ciclo debe pedir la estatura de cada
persona mientras se tenga una estatura registrada
> 0. Omite en el promedio las estaturas < 1.50m. Imprime
el promedio con un límite de 2 decimales.
    
input:
    Dame la estatura 1: 1.56
    Dame la estatura 2: 1.80
    Dame la estatura 3: 1.65
	Dame la estatura 4: 1.76
	Dame la estatura 5: 1.48
	Dame la estatura 6: 0
output:
    El promedio de la estatura es ...

promedio = (1.56+1.80+1.65+1.176)/4
"""
estaturas =1
suma=0
contador=0
while(estaturas>0):
    estaturas=float(input("Dame la estatura "))
    if estaturas>=1.50:
        suma+=estaturas
        contador+=1
if contador !=0:
    print(f'La estatura promedio es de : {(suma/contador):.2f}')
else:
    print("No se ingresaron datos")
