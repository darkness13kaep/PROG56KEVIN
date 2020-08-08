# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:45:54 2020

@author: kevyn_000
"""


import calendar
print("escriba el mes y año a calcular:   ")

año=int(input("Escriba el año :"))
mes=int(input("Escriba el mes :"))
print(calendar.month(año,mes))
