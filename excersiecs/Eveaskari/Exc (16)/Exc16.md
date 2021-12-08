<div dir="rtl">
  
  ### برای سه عبارت زیر نیز مثل سوال یک کدهای مربوط به آنها را بنویسید.
 </div>
 
 (A AND B) OR (B OR C) XOR (A NAND B):
 ```
 def my_concept1(A, B, C):
  x = A and B
  y = B or C
  z = not x
  w = x or y
  if z!=w :
     return True
  else:
     return False

print(my_concept1(0, 0, 0))
print(my_concept1(0, 0, 1))
print(my_concept1(0, 1, 0))
print(my_concept1(0, 1, 1))
print(my_concept1(1, 0, 0))
print(my_concept1(1, 0, 1))
print(my_concept1(1, 1, 0))
print(my_concept1(1, 1, 1))
 ```
 
| A | B | C | Con |
|---|---|---|-----|
| 0 | 0 | 0 | 1   |
| 0 | 0 | 1 | 0   |
| 0 | 1 | 0 | 0   |
| 0 | 1 | 1 | 0   |
| 1 | 0 | 0 | 1   |
| 1 | 0 | 1 | 0   |
| 1 | 1 | 0 | 1   |
| 1 | 1 | 1 | 1   |

![concept1](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(16)/concept1.JPG)

<br/>

 (A AND B OR C) OR (C NAND B):
 ```
 
 def my_concept1(A, B, C):
  x = A and B
  y = x or C
  s = C and B
  z = not s
  w = z or y
  if w==1 :
     return True
  else:
    return False
  

print(my_concept1(0, 0, 0))
print(my_concept1(0, 0, 1))
print(my_concept1(0, 1, 0))
print(my_concept1(0, 1, 1))
print(my_concept1(1, 0, 0))
print(my_concept1(1, 0, 1))
print(my_concept1(1, 1, 0))
print(my_concept1(1, 1, 1))
```
   
| A | B | C | Con |
|---|---|---|-----|
| 0 | 0 | 0 | 1   |
| 0 | 0 | 1 | 1   |
| 0 | 1 | 0 | 1   |
| 0 | 1 | 1 | 1   |
| 1 | 0 | 0 | 1   |
| 1 | 0 | 1 | 1   |
| 1 | 1 | 0 | 1   |
| 1 | 1 | 1 | 1   |

 
 ![concept2](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(16)/concept2.JPG)
 
 
 <br/>
 
 (A XOR B) AND (B OR C) AND (C AND D):
 ```
 def my_concept1(A, B, C, D):
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
  

print(my_concept1(0, 0, 0, 0))
print(my_concept1(0, 0, 0, 1))
print(my_concept1(0, 0, 1, 0))
print(my_concept1(0, 0, 1, 1))
print(my_concept1(0, 1, 0, 0))
print(my_concept1(0, 1, 0, 1))
print(my_concept1(0, 1, 1, 0))
print(my_concept1(0, 1, 1, 1))
print(my_concept1(1, 0, 0, 0))
print(my_concept1(1, 0, 0, 1))
print(my_concept1(1, 0, 1, 0))
print(my_concept1(1, 0, 1, 1))
print(my_concept1(1, 1, 0, 0))
print(my_concept1(1, 1, 0, 1))
print(my_concept1(1, 1, 1, 0))
print(my_concept1(1, 1, 1, 1))
```
 
| A | B | C | D | Con |
|---|---|---|---|-----|
| 0 | 0 | 0 | 0 | 0   |
| 0 | 0 | 0 | 1 | 0   |
| 0 | 0 | 1 | 0 | 0   |
| 0 | 0 | 1 | 1 | 0   |
| 0 | 1 | 0 | 0 | 0   |
| 0 | 1 | 0 | 1 | 0   |
| 0 | 1 | 1 | 0 | 0   |
| 0 | 1 | 1 | 1 | 1   |
| 1 | 0 | 0 | 0 | 0   |
| 1 | 0 | 0 | 1 | 0   |
| 1 | 0 | 1 | 0 | 0   |
| 1 | 0 | 1 | 1 | 1   |
| 1 | 1 | 0 | 0 | 0   |
| 1 | 1 | 0 | 1 | 0   |
| 1 | 1 | 1 | 0 | 0   |
| 1 | 1 | 1 | 1 | 0   |

 
 ![concept3](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(16)/concept3.JPG)
 
 
 <br/>
<br/>
