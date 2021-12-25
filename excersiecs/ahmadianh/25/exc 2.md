<div dir='rtl'>

## سوال 25

با کمک توابع رندوم در یک زبان برنامه نویسی روی یک صفحه ی مختصات دوبعدی  100نقطه با  xو yهای
رندوم در بازه ی  1تا  50بدست آورید و برنامه ای بنویسید که  k=3را نسبت به  43یا چهل و سومین نقطه
ی تولید شده ی شما دارد

</div>
<div dir='rtl'>
با این قطعه کد اعداد رندوم در بازه 1 تا 50 تولید می شود 

</div>

```
import matplotlib.pyplot as plt
from numpy import random
from sklearn import neighbors
import numpy as np
import math
import pandas as pd
from math import sqrt
import math
import operator

def distance (x0,y0,x,y):
 distance=[]
 L= []
 
 for i in range (len(x)):

      distance[i]=((x[i]-x0)*(x[i]-x0)) + ((y[i]-y0)*(y[i]-y0))
      L[i]=sqrt(distance[i])
 print(L[i])

 for i in range (len(x)):
    if L[i]>L[i+1]:
        t=L[i]
        L[i]=L[i+1]
        L[i+1]=t
 print (L[i],L[i+1],L[i+2])

      






x=random.randint(50, size=(100,1))
for i in range (41,44):
    if i==43:
        x0=x[i]
        print("x point 43")
        print(x[43])

y=random.randint(50, size=(100,1))
for i in range (41,44):
    if i==43:
        y0=y[i]
        print("y point 43")
        print( y[43])
    
#Print("x,y point 43 = ")
print("x,y point 43 = ")
print(x[43],y[43])

plt.scatter(x, y, color = 'hotpink')
plt.show()
distance(x0,y0,x,y)
  
```
