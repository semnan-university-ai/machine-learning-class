import numpy as np
<br/>
import math
<br/>
a = int(input('Enter p+: '))
<br/>
b = int(input('Enter p-: '))
<br/>
c = int(input('enter instant quantity'))
<br/>
c =(a+b)/c
<br/>
e =a+b
<br/>
a = a/c
<br/>
b = b/c
<br/>
Ent=-1*c((a *math.log(a,2))+(b*math.log(b,2)))
<br/>
Ent= round(Ent,3)
<br/>
print("entropy  =",Ent)
<br/>

