#Nand = not and|
#XOR = bool(a) != bool(b)

def ex1(A, B, C):
 return bool((A and B) or (B or C)) != bool(not(A and B))

def ex2(A, B, C):
 return bool((A and B or C) or (not(C and B)))

def ex3(A, B, C, D):
    return bool((bool(A) != bool(B)) and (B or C) and (C and D))




print(ex1(0,0,0))
print(ex1(1,1,1))
print("----------------")
print(ex2(0,0,0))
print(ex2(1,1,1))
print("----------------")
print(ex3(0,0,0,0))
print(ex3(1,1,1,1))

