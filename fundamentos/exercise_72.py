# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:29:17 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripición: Dado un string escribe un programa usando comprehension lists, para generar 
o crear una nuvea lista que contenga solos caracteres del
string que sean digitos
s= 'Hola,1,2,3,probando,1,2,3,...,probando,5,6,7'
"""
s= 'Hola,1,2,3,probando,1,2,3,...,probando,5,6,7'
lista=[x for x in s if x.isdigit()]
print(lista)