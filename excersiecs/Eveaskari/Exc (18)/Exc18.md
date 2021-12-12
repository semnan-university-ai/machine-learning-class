<div dir="rtl">
  
  ### فرمول آنتروپی در روش ID3 را بدون استفاده از توابع آماده ی زبان های برنامه نویسی خود برنامه نویسی کنید.
  
  فرمول انتروپی به شرح زیر است:
   Entropy = -(P+logP+ + P-logP-)
  
  </div>
  
  <div dir="ltr">
  
  ```
  import math

def my_entropy( ):
  x = float(input())
  y = float(input())
  la = math.log2(x)
  lb = math.log2(y)
  exp1 = -((x*la) + (y*lb))
  print(exp1)


print(my_entropy())
  ```
  
  </div>
