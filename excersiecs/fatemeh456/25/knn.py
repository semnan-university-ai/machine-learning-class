import random
import math
x = []
y = []
sx = 0 #sample - x
sy = 0 #sample - y
i = 1
while i <= 100:
    xp = random.randint(1,50)
    yp = random.randint(1,50)
    x.append(xp)
    y.append(yp)
    if i == 43:
        sx = xp
        sy = yp
    i += 1

#print("x = " , x)
#print("y = " , y)

print ("sample is (",sx,",",sy,")")

mylist = []  
for a in range(len(x)):
    for b in range(len(y)):
        d = (((sx - x[a])**2) + ((sy - y[b])**2))
        d = math.sqrt(d)
        mylist.append(d)
#print(mylist)
mylist.sort()
#print(mylist)
print(mylist[0]," , " , mylist[1]," , " ,mylist[2])

     
