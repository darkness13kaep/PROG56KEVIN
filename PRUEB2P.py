# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:56:45 2020

@author: kevyn_000
"""


print("INGRESE EL VALOR DE LAS TEMPERATURAS :")

n1=int(input())
n2=float(input())
n3=int(input())
n4=float(input())
n5=int(input())
n6=int(input())
n7=int(input())
n8=int(input())
n9=int(input())
n10=int(input())
C=(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
F= (C*(9/5))+32
K=C+273
print("La temperatura en °F de: ",C,"es",F ,"  y en °K es: ",K,".")
