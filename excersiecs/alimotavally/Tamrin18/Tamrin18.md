<div dir="rtl">
  
  ### فرمول آنتروپی در روش ID3 را بدون استفاده از توابع آماده ی زبان های برنامه نویسی خود برنامه نویسی کنید.
  
  فرمول انتروپی به شرح زیر است:
   Entropy = - ( P(+) logP(+) + P(-) logP(-) )
  
  </div>
  
  <div dir="ltr">
  
  
  ```
  import math

def id3_entropy( ):
a = float(input('please enter  number : '))
b = float(input('please enter  number : '))
  lx = math.log2(x)
  ly = math.log2(y)
  ent = -((x*lx) + (y*ly))
  print(ent)


print(id3_entropy())
  ```
  
  </div>
