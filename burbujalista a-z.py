# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:52:14 2020

@author: kevyn_000
"""
    
from random import randint
from time import sleep
auxiliar=int()
vector=[int() for ind0 in range (100)]
print("INGRESE EL TAMAÑO DEL VECTOR:")
tamañovec=int(input())
for i in range (1,tamañovec + 1):
    vector[i-1]=randint(0,99)
    print("INGRESE EL NOMBREDEL ESTUDIANTE  ",i)
    nombre=input()
    vector[i-1]=nombre
    print("EL VALOR EN LA POSICION   ",i,"  ES  "  ,vector[i-1])
for j in range (1,tamañovec+1):
    for l in range (1,tamañovec) :
        if vector[l-1]>vector[l]:
           auxiliar=vector[l-1]
           vector[l-1]=vector[l]
           vector[l]=auxiliar
for k in range (1,tamañovec+1):
    print("EL VECTOR ORDENADO EN LA POSICION   ",k,"  ES  ", vector[k-1])
print("\n"*2)
print("GRACIAS :3 ")
    sleep(1)
    

