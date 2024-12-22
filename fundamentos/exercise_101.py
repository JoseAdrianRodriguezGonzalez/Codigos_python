# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 23:39:51 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe un programa que genere un dictionarioen donde las llaves
 son las secuencias desde 1 hasta n y los
valores son las llaves al cuadrado. n es un número entero
positivo definido por ti, valida que n sea positivo.

n = 5:
    
output:
    {1:1, 2:4, 3:9, 4:16, 5:25}

"""

n=int(input('n= '))
diccionario={}
if n>0:
    for i in range(1,n+1):
        diccionario[i]=i**2