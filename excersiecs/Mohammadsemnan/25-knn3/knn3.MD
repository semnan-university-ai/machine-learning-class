```
from numpy import random
import matplotlib.pyplot as plt
import numpy
import math
n = 100
val = [0] * n
for x in range (n):
    val[x] = [random.randint(50)]
    val[x].append(random.randint(50))
print(val)
val1=val
print(val1[43])
val2=numpy.array(val1[43])

val = numpy.array(val)

val3=val2[0]+val2[1]
print(val3)

val5=[]
for i in range(0,100):
  val4=val[i:(i+1),0]+val[i:(i+1),1]
  val5.append(abs(val4-val3))
val5=numpy.array(val5)


def sm(arr,n):
  a1=100
  a2=100
  a3=100
  for i in range(0,n):

    if arr[i]<a1:
      a3=a2
      a2=a1
      a1=arr[i]
      a4=i
    elif arr[i]<a2:
      a3=a2
      a2=arr[i]
      a5=i
    elif arr[i]<a3:
      a3=arr[i]
      a6=i
  
  print("a1",a1)
  print("a2",a2)
  print("a3",a3)
  b1=numpy.array(val1[a4])
  b2=numpy.array(val1[a5])
  print(val1[a5])
  b3=numpy.array(val1[a6])
  plt.style.use('ggplot')
  plt.scatter(val[:,0],val[:,1], c = 'b', s = 50,marker = '*')
  plt.scatter(val2[0],val2[1], c = 'r', s = 50,marker = '+')
  plt.scatter(b1[0],b1[1], c = 'g', s = 50,marker = '*')
  plt.scatter(b2[0],b2[1], c = 'g', s = 50,marker = '*')
  plt.scatter(b3[0],b3[1], c = 'g', s = 50,marker = '*')
  plt.title('Scatter Plot of Data')
  plt.show()


print(val5)
n = len(val5)
sm(val5, n)
```

![asd](https://user-images.githubusercontent.com/94211519/147216580-1561f388-147c-425a-9eba-d04840b546fd.png)
