import numpy as np
<br/>
import math
<br/>
a = int(input('p+: '))
<br/>
b = int(input('p-: '))
<br/>
c = int(input('enter iq'))
<br/>
c =(a+b)/c
<br/>
e =a+b
<br/>
a = a/c
<br/>
b = b/c
<br/>
Ent=float(-1*c((a * math.log(a,2))+(b * math.log(b,2))))
<br/>
Ent= round(Ent,4)
<br/>
print('entropy  =',Ent)
<br/>

