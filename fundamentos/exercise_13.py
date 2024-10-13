# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:50:59 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: Escribe un programa que calcule el precio de un pasaje de avión
Dada la distancia en kilometros entera que va a recorre.
Consdierar el costo por kilometro de la siguiente manera
1 a 1000: $47
>1000: $25
input:
    Dame la distancia 1500
output:
    El total a pagar es $59500
    1000*47
    500*25
    a+b
"""
kilometros=int(input('Dame la distancia'))
precio=0
if(kilometros>1000):
    precio=(1000*47)+((kilometros-1000)*25)
else: 
    precio=kilometros*47
print(f"el precio es: {precio}")