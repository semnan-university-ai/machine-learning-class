# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 00:05:19 2021

@author: central
"""


def log2(n):
    """calcukate the value of logaritm(2)"""

    i = 0
    while n > 1:
        n >>= 1
        i += 1
    return i
   
  
  