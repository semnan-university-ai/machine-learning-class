
import numpy as np 
 
p = np.array([0.2,0.3,0.1,0.4]) 
entropy = 0 
for i in range(p.size): 
    entropy = entropy - np.log(p[i]) 
     
print(entropy)