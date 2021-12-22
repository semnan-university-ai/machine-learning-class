#And Function

def And(A, B):
  if A == False or B==False:
    return False 
  else:
    return True
print("A", "B", "AND")      
print("0", "0",And(0,0))
print("0", "1",And(0,1))
print("1", "0",And(1,0))
print("1", "1",And(1,1))

#Or Function
def Or(A, B):
  if A == True or B==True:
    return True 
  else:
    return False
print("A", "B", "Or")      
print("0", "0",Or(0,0))
print("0", "1",Or(0,1))
print("1", "0",Or(1,0))
print("1", "1",Or(1,1))

#Not Function
def Not(A):
  if A == True:
    return False 
  else:
    return True
print("A", "AND")      
print("0",Not(0))
print("1",Not(1))

#Nand Function
def Nand(A, B):
  if A == True and B==True:
    return False 
  else:
    return True
print("A", "B", "AND")      
print("0", "0",Nand(0,0))
print("0", "1",Nand(0,1))
print("1", "0",Nand(1,0))
print("1", "1",Nand(1,1))

#Nor Function
def NOr(A, B):
  if A == False and B==False:
    return True 
  else:
    return False
print("A", "B", "Or")      
print("0", "0",NOr(0,0))
print("0", "1",NOr(0,1))
print("1", "0",NOr(1,0))
print("1", "1",NOr(1,1))


#Xor function
def Xor(A, B):
  if A == B :
    return False 
  else:
    return True
print("A", "B", "Or")      
print("0", "0",Xor(0,0))
print("0", "1",Xor(0,1))
print("1", "0",Xor(1,0))
print("1", "1",Xor(1,1))



