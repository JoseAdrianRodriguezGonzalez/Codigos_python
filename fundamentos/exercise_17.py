# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:53:06 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: Una compañía de viajes cuenta con tres tipos
de autobuses (A, B y C), cada uno tiene un precio por
kilómetro recorrido por persona, los costos respectivos
son $2.0, $2.5 y $3.0. Escribe un programa que solicite la
distancia total del viaje, el número de personas a viajar
y el tipo de autobús a utilizar, y que emita un 
presupuesto del costo por persona y el costo total de todo
el autobús para el viaje (sumando el costo de todas las
personas). Verifica que el tipo de autobús ingresado sea
válido. Limita la precisión a 2 decimales.
    
input:
    Dame la distancia del viaje (km): 1000
	Dame el número de personas: 50
	Dame el tipo de autobús: B
output:
    El costo por persona es: $2500.00
	El costo total del autobús es: $125000.00
    
"""

distancia=float(input("Dame la distancia del viaje: "))
personas=float(input("Dame el numero de personas: "))
bus=input("Dame el tipo de autobus: ")
pago_persona=0
total=0
if bus=="A":
    pago_persona=distancia*2.0
    total=pago_persona*personas
if bus=="B":
    pago_persona=distancia*2.5
    total=pago_persona*personas
if bus=="C":
    pago_persona=distancia*3.0
    total=pago_persona*personas
else:
    print("Autobus no reconocido")    
print(f'El costo por persona es de {pago_persona}')
print(f'El costo total es de {total}')