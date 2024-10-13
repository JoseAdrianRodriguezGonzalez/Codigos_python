# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:03:39 2024
exercise_49

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Dada una lista con strings y números (creada
por ti directamente en el código), escribe un programa
que pida un string y un número entero n al usuario (valida
que sea positivo y menor que la longitud de la lista),
y que inserte el string en la lista, después de cada n
elementos.

lista = [4, 10, 'a', 'b', 1, 'c', 'd', 4, 5, 7, 'e', 'a']

input:
    Dame un string: 'hola'
    Dame un número (entero positivo): 2

output:
    lista = [4, 10, 'hola', 'a', 'b', 'hola', 1, 'c', 
	'hola', 'd', 4, 'hola', 5, 7, 'hola', 'e',
	'a', 'hola']
"""

lista = [4, 10, 'a', 'b', 1, 'c', 'd', 4, 5, 7, 'e', 'a']
cadena=input("Dame un string")
entero=int(input("Dame un entero"))
i = entero
while i < len(lista):
    lista.insert(i, cadena)
    i += entero + 1
else:
    if i%entero==0 and entero%2!=0:
        lista.insert(i, cadena)   
    elif i%entero!=0 and entero%2==0:
        lista.insert(i, cadena)   
# Mostrar el resultado
print("Lista modificada:", lista) 
