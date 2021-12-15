#AND
def AND(A,B):
    if A == "T" and B == "T" :
        print("AND is True")
    else:
        print("AND is False")
       

A = input ("Please enter T or F :")
B = input ("Please enter T or F :")
AND(A,B)



#OR
def OR(A,B):
    if A == "F" and B == "F" :
        print("OR is False")
    else:
        print("OR is True")
              
A = input ("Please enter T or F :")
B = input ("Please enter T or F :")
OR(A,B)


#NOT
def NOT(A):
    if A == "F":
        print("NOT is True")
    else:
        print("Not is False")
       

A = input ("Please enter T or F :")
NOT(A)


#NAND
def NAND(A,B):
    if A == "T" and B == "T" :
        print("NAND is False")
    else:
        print("NAND is True")
              
A = input ("Please enter T or F :")
B = input ("Please enter T or F :")
NAND(A,B)


#NOR
def NOR(A,B):
    if A == "F" and B == "F" :
        print("NOR is True")
    else:
        print("NOR is False")
              
A = input ("Please enter T or F :")
B = input ("Please enter T or F :")
NOR(A,B)


#XOR
def XOR(A,B):
    if (A == "F" and B == "F") or ( A == "T" and B == "T") :
        print("XOR is False")
    else:
        print("XOR is True")
              
A = input ("Please enter T or F :")
B = input ("Please enter T or F :")
XOR(A,B)
