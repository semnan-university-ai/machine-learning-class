<div dir="rtl">
  
  ### برای سه عبارت زیر نیز مثل سوال یک کدهای مربوط به آنها را بنویسید.
 </div>
 
 (A AND B) OR (B OR C) XOR (A NAND B):<br/>
 ```
 def example1(A, B, C):
  x = A and B
  y = B or C
  z = not x
  w = x or y
  if z!=w :
     return True
  else:
     return False

print(example1(0, 0, 0))
print(example1(0, 0, 1))
print(example1(0, 1, 0))
print(example1(0, 1, 1))
print(example1(1, 0, 0))
print(example1(1, 0, 1))
print(example1(1, 1, 0))
print(example1(1, 1, 1))
 ```
 
<br/>

 (A AND B OR C) OR (C NAND B):
 ```
 
 def example2(A, B, C):
  x = A and B
  y = x or C
  s = C and B
  z = not s
  w = z or y
  if w==1 :
     return True
  else:
    return False
  

print(example2(0, 0, 0))
print(example2(0, 0, 1))
print(example2(0, 1, 0))
print(example2(0, 1, 1))
print(example2(1, 0, 0))
print(example2(1, 0, 1))
print(example2(1, 1, 0))
print(example2(1, 1, 1))
```

 <br/>
 
 (A XOR B) AND (B OR C) AND (C AND D):
 ```
 def example3(A, B, C, D):
  if A==B:
    x = 0
  else:
    x = 1
  y = C and D
  s = C or B
  z = x and s
  w = z and y
  if w==1 :
     return True
  else:
    return False
  

print(example3(0, 0, 0, 0))
print(example3(0, 0, 0, 1))
print(example3(0, 0, 1, 0))
print(example3(0, 0, 1, 1))
print(example3(0, 1, 0, 0))
print(example3(0, 1, 0, 1))
print(example3(0, 1, 1, 0))
print(example3(0, 1, 1, 1))
print(example3(1, 0, 0, 0))
print(example3(1, 0, 0, 1))
print(example3(1, 0, 1, 0))
print(example3(1, 0, 1, 1))
print(example3(1, 1, 0, 0))
print(example3(1, 1, 0, 1))
print(example3(1, 1, 1, 0))
print(example3(1, 1, 1, 1))
```
 
