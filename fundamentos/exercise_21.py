# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 01:35:11 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción:Escribe un programa que lea una cantidad n
de números flotantes (pide n al usuario) y que calcule:
    a) CuÃ¡nto suman todos los nÃºmeros
    b) CuÃ¡nto suman los nÃºmeros positivos
    c) CuÃ¡nto suman los nÃºmeros negativos
    
input:
    Dame cuÃ¡ntos nÃºmeros son: 4
    
    Dame el nÃºmero 1: -45
    Dame el nÃºmero 2: 19
    Dame el nÃºmero 3: -5
	Dame el nÃºmero 4: 24
output:
    La suma de todos los nÃºmeros es -7
	La suma de los nÃºmeros positivos es 43
	La suma de los nÃºmeros negativos es -50
"""
num=int(input("Dame cuántos números son: "))
sumtotal=0
sumneg=0
sumpos=0
for i in range(num):
    num2=float(input(f'Dame el número {i+1}: '))
    if num2>=0:
        sumpos+=num2
    elif num2<0:
        sumneg+=num2
    sumtotal+=num2
print(f'La usma de todos los números es: {sumtotal}')
print(f'La usma de los números positivos es: {sumpos}')
print(f'La usma de los números negativos es: {sumneg}')
