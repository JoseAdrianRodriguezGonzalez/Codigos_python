# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:45:48 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: El dueño de un estacionamiento requiere de un
programa para determinar cuánto debe cobrar por el uso del
estacionamiento a sus clientes. Las tarifas que se tienen
son las siguientes: 
	• Las dos primeras horas a $5.00 c/u.
	• Las siguientes tres a $4.00 c/u.
	• Las cinco siguientes a $3.00 c/u.
	• Después de diez horas el costo por cada una es de
        $2.00 c/u.
Escribe un programa que calcule el total a pagar,
dado un número entero de horas. Limita la precisión a 2 
decimales.
    
input:
    Dame el total de horas: 5
output:
    El total a pagar es: $22.00

input:	
	Dame el total de horas: 15
output:
    El total a pagar es: $47.00
"""

horas=int(input('Dame el total de horas: '))
pago=0
if horas<=2:
    pago=horas*5
elif horas>=3 and horas <6:
    pago=(2*5)+(horas-2)*4
elif horas>=6 and horas <11:
    pago=(2*5)+(3*4)+(horas-5)*3
elif horas >=11 :
    pago=(2*5)+(3*4)+(5*3)+(horas-10)*2
    
print(f'El pago total es {(pago):.2f}')