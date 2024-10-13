# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:37:40 2024
Descripcion: Dado un string (definelo en tu codigo),escribe un programa que genere 
otro string originial(define n tu en el cdigo). COmprobar que el string original tenga más de n caracteres en caso contrario
Imprimir 'La cadena es muy corta!'
s='Que tal, cómo etán. Qué han hecho'
n=10
output:
    'Qué tal cmo están. Qué han hecho'
    
"""
s='Que tal, cómo etán. Qué han hecho'
n=40
if len(s)>=n:
    word=s[:n]+s[n+1:]
    print(word)
else: 
    print('La cadena es muy corta')
