# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:43:01 2024

Given five positive integers, find the minimum and maximum values that can be 
calculated by summing exactly four of the five integers. Then print the 
respective minimum and maximum values as a single line of two space-separated 
long integers.
input:
    1 2 3 4 5
output:
    10 14
"""

valor=[1,2,3,4,5]
valor.sort()
sumamax=0
sumamin=0
for i in valor[1:]:
    sumamax+=i
for i in valor[:len(valor)-1]:
    sumamin+=i
print(f'{sumamax} {sumamin}')