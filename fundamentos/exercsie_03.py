# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:50:08 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa que calcule el valor de la hipotenusa en un triángulo rectángulo :
   c^2=a^2+b^2
   dados vlaores flotantes de los catetos por el usario.
input:
    Dame el cateto a: 8.7
    Dame el cateto b: 1.5
Ouput:
    El área de la hipotenusa  es ...
"""
a,b=float(input("Dame el cateto a: ")),float(input("Dame el cateto b: "))
c=((a)**2+(b)**2)**(1/2)
print(f' El valor de la hipotenusa es {c:.2f}')

