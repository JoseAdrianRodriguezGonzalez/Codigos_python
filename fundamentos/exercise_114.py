# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:39:21 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripcion: Escribe un programa que solicite un string al
usuario y que imprima una vocal del string al azar. Si no contiene
vocales, imprimr 'No hay vocales'
input:
    'Hola mundo'
output:
    UNa vocal al azar del string es 'o'
"""
import random as rn
string=input("Dame un string:  ")
vocales='AEIOUaeiou'
s_v=list({c for c in string if c in vocales})
if len(s_v)>0:
    vocal=rn.choice(s_v)
    print(vocal)
else:
    print("No hay vocales")        