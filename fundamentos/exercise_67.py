# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:57:35 2024
exercise_67

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una lista llena con números y strings,
escribe un programa que separe la lista original en dos
listas, una llena con los números y otra llena con los
strings

lista = ['e', 5.6, 'a', 'b', 7.8, 'd', 10.5]

output:
    lista_numeros = [5.6, 7.8, 10.5]
    list_strings = ['e', 'a', 'b', 'd']
"""

lista = ['e', 5.6, 'a', 'b', 7.8, 'd', 10.5]
lista_numeros=[]
lista_strings=[]
for s in lista:
    if type(s)==float or type(s)==int:
        lista_numeros.append(s)
    elif type(s)==str :
        lista_strings.append(s)
print(f'lista_numeros={lista_numeros}')
print(f'lista_string={lista_strings}')