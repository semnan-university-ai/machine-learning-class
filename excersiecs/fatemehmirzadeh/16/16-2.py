# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 01:19:07 2021

@author: central
"""

#(A AND B OR C) OR (C NAND B)
#2

def func2(A, B, C):
 x = A and B
 y = x or C
 q = C and B
 z = not q #nand of C and B
 p = z or y
 if p==1 :
    return 1
 else:
   return 0
print(func2(0, 0, 0))
print(func2(0, 0, 1))
print(func2(0, 1, 0))
print(func2(0, 1, 1))
print(func2(1, 0, 0))
print(func2(1, 0, 1))
print(func2(1, 1, 0))
print(func2(1, 1, 1))