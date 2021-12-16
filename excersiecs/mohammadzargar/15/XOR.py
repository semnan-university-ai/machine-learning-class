#XOR
def zargarxor(a,b): 
    if a==0:
     if b==0:  
        return 0 
    if a==0: 
        if b==1: 
           return 1
 
    if a==1: 
        if b==1: 
            return 0
    if a==1: 
        if b==0: 
            return 1
print (zargarxor(1,0))
