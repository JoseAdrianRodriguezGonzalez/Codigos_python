# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:22:02 2024

Descripcion dado un string escribe un programa que genere otro string compuestro 
por las dos primera su a las ods ultimas letras del string original. 
Si la longitud del stringes menor que 4 que imrpima la leyenda 'Empty string'
s='Hello world!'
output:
    
"""
s='Hello world!'
if len(s)<4:
    print('Empty string')
else:
    s=s[:2]+s[-2:]
    print(s)