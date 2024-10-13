# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:24:11 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dada una lista llena con strings (creada por
ti directamente en el código), escribe un programa
que solicite un string al usuario, lo busque en la lista,
lo quite de su posición y lo envíe al final de la lista.
Si el string no se encuentra en la lista, que imprima
'¡La palabra no existe!'

lista = ['a', 'e', 'z', 'b', 'x', 't', 'hola', 'que']

input:
	Dame una palabra: 't'
output: 
	['a', 'e', 'z', 'b', 'x', 'hola', 'que', 't']
    
input: 
	Dame una palabra: 'mundo'

output:
	'¡La palabra no existe!'
"""

lista = ['a', 'e', 'z', 'b', 'x', 't', 'hola', 'que']
string_pedir=input("Dame un string")
if string_pedir in lista:
    p=lista.pop(lista.index(string_pedir))
    lista.append(p)
    print(lista)
else:
    print("¡La palabra no existe!")