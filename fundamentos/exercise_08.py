# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:34:08 2024

@author: USUARIO

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: Escribe un programa que reciba un número entrro N de dias
 y que devuelva a cuantos años, meses, semanas y días corresponde. Considerar 
 un año con 365 días y un mes con 30 días
input:
    Dame el número de dáis :373
output:
    El total de años es 1
    el total de meses de 0
    el total de smeana es 1 
    el totla de días es 1
"""

##Utilizar los meses y semanas pasadas basandonos en el año
dias=int(input('Dame el numero de días:  '))
anio=dias//365
meses=(dias%365)//30
semanas=(dias%365)//7
dia=(dias%365)%7
print(f'el total de años es {anio}')
print(f'el total de meses es {meses}')
print(f'el total de semanas es {semanas}')
print(f'el total de dia es {dia}')
##Residuo basandonos en el mes o en la semana
anio=dias//365
resto=dias%365
meses=(resto)//30
resto%=30
semanas=(resto)//7
resto%=7
dia=(resto)%7