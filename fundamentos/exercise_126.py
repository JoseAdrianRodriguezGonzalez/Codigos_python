# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:18:17 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reciba un número entero
positivo y que devuelva si ese número es primo o no 
(True/False)

def primo(n):
	pass

primo(7)
output: True

primo(8)
output: False

- Número primo: solo tiene 2 divisores exactos (1 y sí mismo).
"""
def primo(n):
    si=True
    for i in range(1,n):
        if (i!=n) and (i!=1) and not(n%i):
            si=False
            break
    return si
n=int(input("Dame un numero entero positivo: "))
if n>0:
    print(primo(n))
