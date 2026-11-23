"""
Write a python program to find the highest and lowest number form a given string of space separated integers
original string: 1 5 77 9 0
"""

string_1="1 4 5 77 9 0"
lista=list(map(int,string_1.split(" ")))
maximo=max(lista)
minimo=min(lista)
print(minimo)
print(maximo)
