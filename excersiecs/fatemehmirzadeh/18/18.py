# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 23:31:29 2021

@author: central
"""
import math

def Entropy(a,b):
#calculate entropy formula
    entropy = -(a * math.log2(a) + b * math.log2(b))
    print(entropy)
 
a = float(input('num1 is: '))
b = float(input('num2 is: '))

Entropy(a,b)

