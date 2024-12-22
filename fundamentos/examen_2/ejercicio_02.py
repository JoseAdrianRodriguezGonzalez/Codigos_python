# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:55:43 2024

Carrera:Licenciatura en Ingeniería de Datos e Inteligencia ARTIFICIAL
cURSO: Fundamentos del Análisis de Datos
Semestre: 2024 Agosto-Diciembre
Examen práctico 2
Fecha: 29-10-2024
Profesor: Dr. Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Adivinanzas
"""
import random as rn
palabras = {
    'Casa': 'Edificio para habitar',
    'músico': 'Persona que conoce el arte de la música o lo ejerce',
    'peine': 'Utensilio de madera, marfil, concha u otra materia, provisto de dientes muy juntos, con el cual se desenreda y compone el pelo.',
    'puente': 'Estructura que permite salvar un obstáculo natural, como un río o un barranco',
    'silla': 'Mueble con respaldo y, por lo general, con patas, utilizado para sentarse',
    }
conteo=0
palabra=rn.choice(list(palabras.keys()))
palabra_list=rn.sample(palabra, len(palabra))
opcion="s"
gano=False

while(opcion=='s'):
    print("divina la siguiente palabra")
    print(' '.join(palabra_list))
    print(palabras[palabra])
    respuesta=input("Escribe tu respuesta: ").lower()
    
    
    
    if respuesta==palabra.lower():
        print("*********************+")
        print("¡Felicidades, has adiviniado la palabra!!")
        print("*********************+")
        gano=True
    else:
        conteo+=1
        print(f"¡Respuesta incorrecta! Te quedan {3-conteo} oportunidades")
        gano=False
        if conteo==3:
            print("*********************+")
            print("*:( Perdiste: ¡intentalo de nuevo!")
            conteo=0
            palabra=rn.choice(list(palabras.keys()))
            palabra_list=rn.sample(palabra, len(palabra))    
    opcion=""
    error=True
    while error:
        opcion=input("Quieres volver a jugar? s/n: ").lower()
        if opcion=='s' and gano:
            error=False
            conteo=0
            palabra=rn.choice(list(palabras.keys()))
            palabra_list=rn.sample(palabra, len(palabra))
            continue
        elif opcion=='s':
            error=False
            continue
        if opcion=='n':
            error=False
            print("*********")
            print("*¡¡Gracias por jugar!*")
            print("*********")
        else:
            print("Opcion no valdia!!!!!!!Da otra entrada")