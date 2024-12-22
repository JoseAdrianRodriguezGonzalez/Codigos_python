# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:45:23 2024
Carrera:Licenciatura en Ingeniería de Datos e Inteligencia ARTIFICIAL
cURSO: Fundamentos del Análisis de Datos
Semestre: 2024 Agosto-Diciembre
Examen práctico 2
Fecha: 29-10-2024
Profesor: Dr. Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Juego de pig
"""
import random as rn
opcion=""
error=True
while error:
    opcion=input("Entra j pra jugar o q para salir del juego:").lower()
    error=False
    if opcion=='j':
        puntos_usuario=0
        valores_usuario=[]
        puntos_compu=0
        valores_compu=[]
        volver_jugar='s'
        gano=False
        while volver_jugar=='s':#Si quiere volver a jugar
            
            a=(rn.randint(1, 6)) 
            b=(rn.randint(1, 6)) 
            ###usuario
            if (a==1) or (b==1):
                print(f'Número para la computadora {a} y {b}')
                print(f'Total de nueros para la computadora {puntos_usuario}')
                print("**************")
            elif (a==1) and (b==1):
                puntos_usuario=0
                valores_usuario=[]
            else:
                puntos_usuario+=(a+b)
                valores_usuario.append(a)
                valores_usuario.append(b)
                print("**************")
                print(f'Número para el usario: {a} y {b}')
                print(f'Total de nueros para el usuario{puntos_usuario}')
                print("**************")
            if puntos_usuario>50:
                print("**************")
                print("*¡Felicdades, has ganado la partida!!")
                print("**************")
                print(valores_usuario)
                volver_jugar=""
                gano=True
                error_ca=True
                while error_ca:
                    volver_jugar=input("Quieres volver a jguar (s/n)").lower()
                    if volver_jugar=='n':
                        error_ca=False
                        print("*********")
                        print("*¡¡Gracias por jugar!*")
                        print("*********")
                    elif volver_jugar=='s' and gano:
                        puntos_usuario=0
                        valores_usuario=[]
                        puntos_compu=0
                        valores_compu=[]
                        gano=False
                        break
                    
                    else:
                        print("Opcion no valida, da otra entrada")
            else:                
            #computadora
                
                a=(rn.randint(1, 6)) 
                b=(rn.randint(1, 6)) 
                            
                if (a==1) or (b==1):
                    print(f'Número para la computadora {a} y {b}')
                    print(f'Total de nueros para la computadora {puntos_compu}')
                    print("**************")
                elif (a==1) and (b==1):
                    print(f'Número para la computadora {a} y {b}')
                    puntos_compu=0
                else:
                    puntos_compu+=(a+b)
                    print(f'Número para la computadora {a} y {b}')
                    print(f'Total de nueros para la computadora {puntos_compu}')
                    print("**************")
                if puntos_compu>50:
                    print("***********")
                    print(":( Perdite¡Mejor suerte para la próxima!")
                    print("***********")
                    print(f'Secuencia perdedora {valores_usuario}')
                    puntos_usuario=0
                    valores_usuario=[]
                    puntos_compu=0
                    valores_compu=[]
                    volver_jugar=""
                error_ca=True
                while error_ca:
                    volver_jugar=input("Quieres volver a jguar (s/n)").lower()
                    if volver_jugar=='n':
                        error_ca=False
                        print("*********")
                        print("*¡¡Gracias por jugar!*")
                        print("*********")
                    elif volver_jugar=='s':
                        break
                    else:
                        print("Opcion no valida, da otra entrada")
    elif opcion=='q':
        print("*************")
        print("* ¡¡Gracias por jugar!*")
        print("*************")
        
    else:
        print("¡Opción no válida! Da otra entrada")
        error=True