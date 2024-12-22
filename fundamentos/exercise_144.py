# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:25:30 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: José Adrián Rodríguez González
Descripcion: Escribe un programa ue lea las nlineas y las concatene en una variable separandolas por un espacio
hola mundo
que tal
¿cómo estás?
hello wolrd
output: 
    hola mundo que tal como estás
"""
f_path="C:/Users/USUARIO/Documents/Universidad/terer/fundamentos/code/data/"
f_name='info_students'
f_extension='.csv'
f_file=f_path+f_name+f_extension
n=int(input("Dime la cantidad de lineas que quieras leer: "))
c=0
string=[]
with open(f_file,'r',encoding='utf-8') as reader:
    while c<n:
        data=reader.readline().strip()
        string.append(data)
        c+=1
s=' '.join(string)
print(s)
        