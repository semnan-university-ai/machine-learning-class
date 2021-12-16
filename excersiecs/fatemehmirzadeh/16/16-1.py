# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 01:00:59 2021

@author: central
"""
#(A AND B) OR (B OR C) XOR (A NAND B)
def func1(A, B, C):
 x = A and B
 y = B or C
 z = not x  #a nand b
 w = x or y
 if z!=w :
    return 1
 else:
    return 0

print(func1(0, 0, 0))
print(func1(0, 0, 1))
print(func1(0, 1, 0))
print(func1(0, 1, 1))
print(func1(1, 0, 0))
print(func1(1, 0, 1))
print(func1(1, 1, 0))
print(func1(1, 1, 1))