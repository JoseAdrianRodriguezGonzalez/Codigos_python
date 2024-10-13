# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 01:29:58 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion:Escribe un programa que lea una cantidad n
de números flotantes (pide n al usuario) y que determine 
cuál fue el mayor número ingresado.
    
input:
    Dame cuÃ¡ntos nÃºmeros son: 4
    
    Dame el nÃºmero 1: -45.7
    Dame el nÃºmero 2: 19.4
    Dame el nÃºmero 3: -5.2
	Dame el nÃºmero 4: 24.4
output:
    El mayor nÃºmero ingresado fue 19.4
"""
num=int(input('Dame cuantos numeros son: '))
mayor=0
neg=0
for i in range(num):
    num2=float(input(f'Dame el numero {i+1}: '))
    if (i==0) or(num2>mayor):
        mayor=num2
print(f'El numero más grande es: {mayor}')