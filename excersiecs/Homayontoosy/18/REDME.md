<div dir="rtl">
سوال :فرمول آنتروپی در روش ID3 را بدون استفاده از توابع آماده ی زبان های برنامه نویسی خود برنامه نویسی کنید.
</div>
<br/>

Import numpy as np
Import math
Print(" enter p+ ")
a=int(input())
Print(" enter p- ")
b=int(input())
Print(" enter instant quantity ")
D=int(input())
d =(a+b)/d
c =a+b
a = a/c
b = b/c
entropy=-1*d((a*math.log(a,2))+(b*math.log(b,2)))
entropy= round(entropy,3)
print("entropy is =",entropy)
