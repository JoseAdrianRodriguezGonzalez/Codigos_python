# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 05:18:32 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa que muestre el siguiente
menú en pantalla:
1) sumar
2) restar
3) multiplicar
4) dividir
5) salir
y que solicite al usuario una opción. De acuerdo con la
opción seleccionada, el programa debe pedir 2 números
enteros, realizar la operación indicada y mostrar el
resultado. El programa debe repetir el menú y la selección
de operaciones mientras no se ingrese un 5 en la opción.
En caso de que la opción ingresada sea inválida, indicarlo
en la terminal. Si hay una división por 0, también
indicarlo en la terminal.

input:
	1) sumar
	2) restar
	3) multiplicar
	4) dividir
	5) salir
	Selecciona una operación: 3
	Dame el primer número: 3
	Dame el segundo número: 5

output:	
	El resultado de la operación es: 15
	
"""
print("1) Sumar")
print("2) restar")
print("3) multiplicar")
print("4) dividir")
print("5) salir")
peticion=int(input("Selecciona una operacion: "))
while peticion!=5:
    if peticion==1:
        num1=float(input("Dame el primer numero"))
        num2=float(input("Dame el segundo numero"))
        print(f"El resultado es {(num1+num2):.2f}")
    elif peticion==2:
        num1=float(input("Dame el primer numero"))
        num2=float(input("Dame el segundo numero"))
        print(f"El resultado es {(num1-num2):.2f}")
    elif peticion==3:
        num1=float(input("Dame el primer numero"))
        num2=float(input("Dame el segundo numero"))
        print(f"El resultado es {(num1*num2):.2f}")
    elif peticion==4:
        num1=float(input("Dame el primer numero"))
        num2=float(input("Dame el segundo numero"))
        if num2!=0:
            print(f"El resultado es {(num1/num2):.2f}")
        else:
            print("DIvision por cero")
    else:
        print("Operacion no valida")
    print("1) Sumar")
    print("2) restar")
    print("3) multiplicar")
    print("4) dividir")
    print("5) salir")
    peticion=int(input("Selecciona una operacion: "))