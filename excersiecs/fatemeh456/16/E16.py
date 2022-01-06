#1
def my_func1(A,B,C):
    if (A == "F" and B == "F" and B == "F") or (A == "T" and B == "F" and B == "F") or (A == "T" and B == "T") :
        print("True")
    else:
        print("False")
              
A = input ("Please enter T or F :")
B = input ("Please enter T or F :")
C = input ("Please enter T or F :")

my_func1(A,B,C)


#2
def my_func2(A,B,C):
        print("True")
    
A = input ("Please enter T or F :")
B = input ("Please enter T or F :")
C = input ("Please enter T or F :")

my_func2(A,B,C)


#3
def my_func3(A,B,C,D):
    if C == "F" or D == "F" :
        print("False")
    else:
        if (A == "T" and B == "T") or (A == "F" and B == "F"):
            print("False")
        else:
            print("True")
              
A = input ("Please enter T or F :")
B = input ("Please enter T or F :")
C = input ("Please enter T or F :")
D = input ("Please enter T or F :")

my_func3(A,B,C,D)
