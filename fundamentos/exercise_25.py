# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:06:58 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Un restaurante ofrece hamburguesas de tres tipos: Sencillas(s), dobles(d)
y triples(t), las cuales tienen un costo de $20,$25 y $30 respectivamente. La empres acepta tarjetas de créidto con
un cargo de 5% sobre el total de la compra. Suoniendo que un cliente adquiere n hamburguesas (n dad por el usuario9),
Cada una puede ser de diferente tipo, escribe un programa que caclule cuánto 
debe pagar el client, dependiendo si decide pagar con tarjeta de crédito o no.
input:
    Dame cuántas hamburguesas son: 3
    tipos hamburguesa 1(s/d/t):s
    tipos hamburguesa 2(s/d/t):s
    tipos hamburguesa 3(s/d/t):t

Pago cn tarjeta (s/n): s
output:
    Totala a pagar es $70
    total a pagar con tarjeta e s $73.5 5%
"""
hamburgesas=int(input("Dame cuántas hamubrguesas son: "))
suma=0
for i in range(hamburgesas):
    tipo=input(f'tipos hamburguesa {i+1}(s/d/t): ')
    if tipo=='s':
        suma+=20
    elif tipo=='d':
        suma+=25
    elif tipo=='t':
        suma+=30
    else:
        print('Tipo de hamburguesa no valido')
tarj=input('Pago con tarjeta (s/n)')
total=0
if tarj=='s':
    total=suma*1.05
    print(f'Total a pagar es $ {suma}')
    print(f'Total a pagar con tarjeta es $ {total}')
elif tarj=='n':
    total=suma
    print(f'Total a pagar es $ {suma}')
else:
    print('No se reconoce valor')