# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:34:35 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos

Descripcion dada una lsita de strins, escribe un programa que imprima un sitrng
 de esa lista al azar.
lista=['hola',' mundo','que','tal']
output :
    que
"""
import random as rn
lista=['hola',' mundo','que','tal']
print(lista[rn.randint(0,len(lista)-1)])
