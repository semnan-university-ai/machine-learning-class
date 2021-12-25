import random
import math

x_array = []
y_array = []
x_point = 0
y_point = 0
i = 1

while i <= 100:
    x = random.randint(1,50)
    y = random.randint(1,50)
    x_array.append(x)
    y_array.append(y)
    if i == 43:
        x_point = x
        y_point = y
    i += 1


print ("sample is (",x_point,",",y_point,")")

distance_array = []  
for a in range(len(x_array)):
    for b in range(len(y_array)):
        distance = (((x_point - x_array[a])**2) + ((y_point - y_array[b])**2))
        distance = math.sqrt(distance)
        distance_array.append(distance)

distance_array.sort()

print(distance_array[0]," , " , distance_array[1]," , " ,distance_array[2])