.# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:21:57 2020

@author: kevyn_000
"""
def añob(año):
    if año % 4 == 0  and  (año % 100 != 0  or  año % 400 == 0):
        return 'El año %d es bisiesto.' % año
    else:
        return 'El año %d no es bisiesto.' % año
 
try:
    año = int(input('Dame un año: '))
    print (añob(año))
except:
    print ('Failed')


    