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
import math

f = open("G:/TTT/myfile.txt", "w")
x=random.randint(50, size=(100,1))
for i in range (41,44):
    if i==43:
        print("x point 43")
        print(x[43])

y=random.randint(50, size=(100,1))
for i in range (41,44):
    if i==43:
        print("y point 43")
        print( y[43])
    
print("x,y point 43 = ")
print(x[43],y[43])
f.write("{} {}\n".format(x,y))

plt.scatter(x, y, color = 'hotpink')
plt.show()
f.close(x)

```
