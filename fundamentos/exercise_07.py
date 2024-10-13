# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:16:12 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa que calcule el total a pagar por la compra de
3 productos, considerando que los dos priemros tiene un 20 % de descuento cada
 uno y le último un 30 % de descuento, además sumar el  IVa al total.
 Solicitar el precio de cada producto al usuario. 
Desplgear el subtotal sin descuento, el sutotal con desceunto, el IVA  a pagar (16%) y el total a pagar
después de lso descuentos y sumando el IVA
input: 
    Dame el precio del producto 1:
    Dame el precio del producto 2:
    Dame el precio del producto 3:
Output:
    El subtotal sin descuento es
    El subtotal con descuento es
    el IVA a pagar es ...
    el total a pagar es 
    
"""
producto_1=float(input('Dame el precio del producto 1: '))
producto_2=float(input('Dame el precio del producto 2: '))
producto_3=float(input('Dame el precio del producto 3: '))
subtotal=producto_1+producto_2+producto_3
subtotal_descuento=producto_1*0.8+producto_2*0.8+producto_3*0.7
iva=subtotal_descuento*0.16
total=subtotal_descuento*1.16
print(f'El subtotal sin descuento es de: {subtotal:.2f}')
print(f'El subtotal con descuento es de: {subtotal_descuento:.2f}')
print(f'El IVA a pagar es de: {iva:.2f}')
print(f'El total es de: {total:.2f}')

