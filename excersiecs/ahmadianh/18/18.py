
def Entropy(P1,P2):
	"""P1 Ehtemal vogho Positive , P2 Ehtemal vogho negative"""
	L1= math.log2(P1)
	L2=math.log2(P2)
	L3= P1*L1
	L4=P2*L2
	Entropy1= abs(L3+L4 )
	return Entropy1

import math 
print("Enter the probability of occurrence of positive  P+")
x=float (input ())
while x>1 or x<0:
	print("please enter 0<nember<1 ")
	x=float (input ())
else:
	P1=x
print("Enter the probability of occurrence of Negetive P- ")
y=float(input())

while y>1 or y<0:
	print("please enter 0<nember<1 ")
	y=float (input ())
else:
 P2=y

if (P1 ==1 and P2 ==0) or (P1==0 and P2==1):
  print ("Entropy = 1")
  
else: print(Entropy(P1,P2))


