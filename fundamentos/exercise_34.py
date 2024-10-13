# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:04:10 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: DADA UNA LISTA DE NUMEROS FLOTANTES(creada por ti directamente en el código),
escribe un programa que devueva los valores minimo y maximo en la lista
output:
    el minimo es 1.5
    el maximo es 10.3
"""
lista=[4.5,3.2,-0.5,2.3]
mayor=lista[0]
menor=lista[0]
for i in lista:
    if i>mayor:
        mayor=i
    if i<menor:
        menor=i
print(mayor)
print(menor)