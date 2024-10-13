# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:56:59 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion : Basic for loop


"""
#for e un bloque de control para ciclos definidos.
# eneralmente e encarga de controlar la ejecución de un bloque
# de instrucciones por un número efinido de vece
# En Python para controlar el ciclo gor se utiliza un iterable
# (objeto o funcion)
# Un itrable es un objeto sobre el que se puede  iterar(recorrer), como una colección de valores
#pero también puede ser una función que genera un valor secuencial cada que se llama (iterator)
#Estructur general del ciclo for:
    #for {variable de control} in (iterable)
    #iteable: objeto a función
#for i in range(11):
#    print(i)
#Variable de control i 
#iterable: funcion range
# Imprimir la seuencia de vlaores enetre 0 y 10
# En cada iteración(ciclo) del bloque for, la función range
#genera un valor secuencial y se lo asigna a la variale de control i
# La función range es una función iterable que genera un vlalor en cada iterción demanera secuencial

#La función range fenera los alores detntro de un rango definido
#(val_ini, val_end-1,step)
#Si el valor inicial se omite, inica en 0
#Sie l paso(step se omite, el valro por default es 1)
for i in range(1,11,1):
    if i==3:
        break
    print(i)
print("end")
####Use of cotniue
for i in range(1,11,1): #genera valors entre 0 y 10
    if i==3 or i==5: #Evalua si la variable de control i==3 o i==5
        continue #Se salta esta iteración omite las instrucciones posteriores y continua con el siguientevalor en la iteracion
    print(i)
print("end")
for i in range(11): #Genera valores entre o y 10
    if i==11: #Evaluea si la variable de control i==3
        break
    print(i)#imprimie los alores de i
else:
    print("noooo")
#El bloque else en el for se ejucta solo cuando el cilco logro terminar complematne. Es decir, cuando n se ejecuta un break



###Use of nested fos
for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print(f'{i}*{j}={k}')