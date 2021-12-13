import numpy as np
import math
a = int(input('Enter p+: '))
b = int(input('Enter p-: '))
c = int(input('enter instant quantity'))
c =(a+b)/c
e =a+b
a = a/c
b = b/c
entropy=-1*c((a*math.log(a,2))+(b*math.log(b,2)))
entropy= round(entropy,3)
print("entropy is =",entropy)
