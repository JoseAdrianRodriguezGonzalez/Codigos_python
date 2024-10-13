# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:54:22 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: Un productor de leche entrega su producto en litros,
 pero le pagan en galones. Escribe un programa que solicite la porducción
 en litro y el precio por galón, y que calcule cuánto le pagarán al producto. 
Limita la precisión a 2 decimales

(1 galon= 3.785 litros)
input :
        Dame la producción en litros: 80
        Dame el precio por galón:50.25
    output:
        el pago total es ...
"""

litros=float(input("Dame la producción en litros= "))
precio=float(input("Dame el precio por galón= "))
pago=litros/3.785*precio
print(f"el pago total es: ${pago}")