
# While

"""
i = 1
while i < 10:
	print(i)
	i+=

i = 0
while i <= 21:
	if i == 5:
		i += 1
		#continue
		break
	else:
		if i % 2 == 0: # mod
			print(str(i) + " is even")
		else:
			print(str(i) + " is odd")

	i += 1	

"""
# ...s

#print(range(10))
"""
for x in range(5, 100, 5):
	print(x)

"""

mylist = [ "amir", "ali", "reza", "zahra" ]
"""
for x in mylist:
	print(x)
"""

#print(len(mylist))
"""
for x in range(1, len(mylist) -1):

	print(mylist[x])

"""
"""
def mySum(number1, number2 = 0, printstate = False):
	if printstate == False:
		return int(number1) + int(number2)
	else:
		print(int(number1) + int(number2))



#num1 = input("Enter Number 1 : ")
#num2 = input("Enter Number :D ")

print("23")

"""

"""
def mySum(x, y):
	global z
	z = 10
	#print(x + y)


x = 10
mySum(2, 5)
print(z + 2)

"""

"""
def myMin(a):
	m = a[0]
	for x in a:
		if m > x:
			m = x

	return m

a = [ 1, 2, 6, -2, 98, 23]

print(myMin(a)) #min
print(max(a))
print(abs(-2))
print(pow(2,3))

"""

import math as m1
#print(math)

#for x in math:
	#print(x)

print(m1.sqrt(64))
print(m1.floor(2.3))
print(m1.floor(2.8))

print(m1.ceil(2.2))

print(m1.pi)

# import pandas as ps
# import numpy as np

#print( help(m1))

from persian_tools import digits

print(digits.convert_to_fa(123))