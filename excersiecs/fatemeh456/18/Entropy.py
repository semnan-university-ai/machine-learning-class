
def log (a):
    counter = 0
    value = 0
    while value < a:
        value = 2**counter
        if (value == a):
            break
        counter += 1
    print(counter)


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

