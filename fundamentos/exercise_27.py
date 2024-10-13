# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:42:59 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción:
    Escribe un programa que permite leer una cantidad variable de número 
    flotantes hasta que s eingresen 3 números negativos consecutivos.
    Al final, imprimir la suma de todos los números.
    input: 
        Dame el número 1: 2.5
        Dame el número 2: 3.3
        Dame el número 3: 7.8
        Dame el número 4: -1
        Dame el número 5: -5.6
        Dame el número 6: 7.8
        Dame el número 7: 2.5
        Dame el número 8: 2.5
        Dame el número 9: 2.5
    
    
"""
i =0
suma=0
while i<3:
    n=float( input("Dame el numero: "))
    if n<0:
        i+=1
    else:
        i=0
    suma+=n
print(f'la suma es {suma:.2f}')


