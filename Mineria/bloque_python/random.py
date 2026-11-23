"""
Description: generar númeos aleatorios  y manejo de archivos generales
"""

import random as rnd
rnd.seed()
# EStablecer una seilla permite reproducibilidad
#del código
print(rnd.random())

#Archivos

# Modos con open
#r -> read o lectur#w -> write escritur
#a -> append

w_d="/data/"
o_f=w_d+"nota.txt"

with open(o_f,'r',encoding='utf-8')as f:
    print(f)
