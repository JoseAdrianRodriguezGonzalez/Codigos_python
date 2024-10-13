# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:55:22 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa que pida un nombre (string) al usuario y que
termine cuando el usuario escriba 'Fin'.
Imprime cada nombre que ada el usuario. Al final imprime 'Terminamos
input:
    Dame un nombre Juan
Hola Juan
    Dame un nombre Ana
Hola Ana
    Dame un nombre luis
Hola luis
    Dame un nombre fin
Terminamos'
"""
nombres=""
while(nombres!="Fin"):
    nombres=input("Dame un nombre: ")
    if nombres!= "Fin":
        print(f'¡Hola {nombres}!')
else:
    print("¡Terminamos!")
