def mf1(a, b, c): 
    if a==0: 
        if b==1: 
            return 0 
        elif b==0: 
            if c==0: 
                return 1 
            elif c==1: 
                return 0 
    elif a==1: 
        if b==1: 
            return 1 
        elif b==0: 
            if c==0: 
                return 1 
            elif c==1: 
                return 0 
 
print(mf1(0,1,0))