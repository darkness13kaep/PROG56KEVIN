# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:59:33 2020

@author: kevyn_000
"""


from turtle import *
color("black","green")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
