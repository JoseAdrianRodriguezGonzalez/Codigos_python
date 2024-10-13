# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:30:18 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion:Escribe un programa que lea una cantidad n
de números enteros (pide n al usuario) y que determine 
cuál fue el mayor número ingresado y cuantas veces se ingreso 
    
input:
    Dame cuÃ¡ntos nÃºmeros son: 5
    
    Dame el nÃºmero 1: 5
    Dame el nÃºmero 2: 3
    Dame el nÃºmero 3: 5
	Dame el nÃºmero 4: 2
    Dame el nÃºmero 5: 1
    
output:
    El mayor nÃºmero ingresado fue 5 y  fue ingresado dos veces
"""

num=int(input("Dame cuantos numeros son:"))
mayor=0
cuenta=0
anterior=0
for i in range(num):
    num_pedido=int(input(f"dame el numero {i+1}: "))
    if i==0 or num_pedido>mayor:
        mayor=num_pedido
        cuenta=1
    elif mayor==num_pedido:
        anterior=mayor
        cuenta+=1
    
print(f"El numero mayor fue {mayor} y se repitio {cuenta}")