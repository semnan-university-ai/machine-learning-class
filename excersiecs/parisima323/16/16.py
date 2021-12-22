
def Func1(A, B, C):
    return bool((A and B) or (B or C)) != bool(not(A and B))

def Func2(A, B, C):
    return bool((A and B or C) or (not(C and B)))

def Func3(A, B, C, D):
    return bool((bool(A) != bool(B)) and (B or C) and (C and D))



