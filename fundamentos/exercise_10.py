# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:55:40 2024

@author: USUARIO
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: Escribe u programa que diga si un número entero dado por el usario
es pa, impar o cero.
input:
    Dame un número :3
    Dame un número :8
    Dame un número :0
Output:
    El número es impar
    El número es par
    El número es 0 
"""
n=int(input("Dame un número: "))
if (n!=0):
    if(n%2):
        print("Es un número impar")
    else:
        print("Es un número par")
else:
    print("El número 0")
##Other way
if(n!=0 and n%2):
    print("Es impar")
elif(n!=0 and not(n%2)):
    print("Es par")
else:
    print("Es cero")