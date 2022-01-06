#(A XOR B) AND (B OR C) AND (C AND D)
#3
def func3(A, B, C, D):
 if A==B:
   x = 0
 else:
   x = 1
 y = C and D
 q = B or C
 z = x and q
 p = z and y
 if p==1 :
    return 1
 else:
   return 0
print(func3(0, 0, 0, 0))
print(func3(0, 0, 0, 1))
print(func3(0, 0, 1, 0))
print(func3(0, 0, 1, 1))
print(func3(0, 1, 0, 0))
print(func3(0, 1, 0, 1))
print(func3(0, 1, 1, 0))
print(func3(0, 1, 1, 1))
print(func3(1, 0, 0, 0))
print(func3(1, 0, 0, 1))
print(func3(1, 0, 1, 0))
print(func3(1, 0, 1, 1))
print(func3(1, 1, 0, 0))
print(func3(1, 1, 0, 1))
print(func3(1, 1, 1, 0))
print(func3(1, 1, 1, 1))