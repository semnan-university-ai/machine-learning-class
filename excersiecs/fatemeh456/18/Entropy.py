def log(a):
    tol = 1e-13
    ans = 0.0
     
    while a<1:
        ans -= 1
        a *= 2
    while a>= 2:
        ans += 1
        a /= 2
         
    fp = 1.0
    while fp>=tol:
        fp /= 2
        a *= a
        if a >= 2:
            a /= 2
            ans += fp
             
    return ans

print(log(3))

def Entropy(ppos , pneg):
    ppos = float(ppos)
    pneg = float(pneg)
    Logpos = log(ppos)
    Logneg = log(pneg)
    ans = ((ppos * Logpos) + (pneg * Logneg))
    print(-ans)


pos = input ("Enter p positive : ")
neg = input ("Enter p negative : ")
if (float(pos) + float(neg))>1:
    print ("out of range")
else:
    Entropy (pos , neg)
