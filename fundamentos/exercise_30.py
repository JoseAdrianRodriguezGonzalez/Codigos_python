# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 04:59:56 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa que solicite 2 números
enteros positivos al usuario <= 100 (valida que sean <=100)
y que imprima todos los números pares que hay entre estos
dos números (incluyendo ambos números), usando un ciclo
while. Considerar que pueden darte el número mayor primero y el número menor después.
    
input:
    Dame el número 1: 50
    Dame el número 2: 40
output:
    40
	42
	44
	46
	48
	50
"""
mayor=int(input("Dame el numero 1: "))
menor=int(input("Dame el numero 2: "))
contador=0
if mayor<=100 and mayor>=0 and menor<=100 and menor >=0 :
    if menor>mayor:
        menor+=mayor
        mayor=menor-mayor
        menor-=mayor
    contador=menor
    while contador<=mayor:
        if contador%2==0:
            print(contador)
        contador+=1
else:
    print("están fuera del rango")