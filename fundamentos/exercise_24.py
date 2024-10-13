# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:48:37 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: Escribe un programa para generar n elementos de la serie de Fibonacci, n>=3
Seri de Fibonacci:
    0,1,1,2,3,5,8,13,21,24
input:
    Dame un número: 5
output:
    0,1,1,2,3
input :
    Dame un númer 2
Output:s
    ¡Error! el Número debe ser >=3        
"""
num=int(input("Dame un número natural: "))
aur=0
if num>=3:
    serie=0
    serie2=1
    sig=0
    print(serie)
    print(serie2)
    for i in range(2,num):
        sig=serie+serie2
        print(sig)
        serie=serie2
        serie2=sig
        aur=serie2/serie
else:
    print("¡Error! el Número debe ser >=3")
print(aur)