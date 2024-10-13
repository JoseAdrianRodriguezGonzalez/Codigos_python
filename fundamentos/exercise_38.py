# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:12:08 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripción: Escribe un programa que solicite un número
entero positivo n al usuario (valida que sea positivo),
y que que genere una lista que contenga n sublistas
internas, y que cada lista interna contenga n ceros.
    
input:
    Dame el número (entero positivo): 3
output:
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

input:
    Dame el número (entero positivo): 2
output:
    [[0, 0], [0, 0]]
"""
n=int(input("Dame el número (entero positivo): "))
lista=[]
lista2=[]
if n>0:
    cont=0
    while cont<n:
        lista.append(0)
        cont+=1
    for i in range(n):
        lista2.append(lista)
else:
    print("No es entero positivo")
print(lista2)