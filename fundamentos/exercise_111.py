# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:46:42 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adria´n
Descripción:Escribe un programa que genere una lista llena con 100 numeros 
enteros aleatorios entre 100 y 1000
"""
import random as rn
lista=[rn.randint(100,1000) for i in range(100)]
print(lista)