import math

a = float(input('enter first number : '))
b = float(input('enter second number : '))

entropy = -(a * math.log2(a) + b * math.log2(b))
 
print ('entropy =', entropy)