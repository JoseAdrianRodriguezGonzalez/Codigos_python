# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:14:59 2024

@author: USUARIO
@author: USUARIO
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reciba dos tuplas de numeros flotantes del
 mismo tamaño y que calcule su producot punto
t1=(1.5,2.4,6.7,8.9)
t2=(3.2,9.3,1.8,4.5)
"""
t1=(1.5,2.4,6.7,8.9)
t2=(3.2,9.3,1.8,4.5)
def producto_punto(t1,t2):
    return sum(i*j for i,j in zip(t1,t2))
print("Producto punto: ",producto_punto(t1, t2))