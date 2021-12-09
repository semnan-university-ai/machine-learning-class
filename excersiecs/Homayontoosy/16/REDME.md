<div dir="rtl">
برای سه عبارت زیر نیز مثل سوال یک کدهای مربوط به آنها را بنویسید.
<div/>

<br/>
(A AND B) OR (B OR C) XOR (A NAND B)
</br>  
(A AND B OR C) OR (C NAND B)
<br/>
(A XOR B) AND (B OR C) AND (C AND D)

<br/>
<div dir="rtl">
# Python3 program to illustrate 
# working of javab3 gate   

if(a == 0) and (b == 1) and (c == 1) and (d == 1):
        return 1
    elif(a == 1) and (b == 0) and (c == 1) and (d == 1):
        return 1
    else: 
        return 0
  
# Driver code  
if __name__=='__main__': 
    print(javab3(0, 0, 0, 0)) 
  
    print("+---------------+----------------+") 
    print(" | javab3 Truth Table | Result |") 
    print(" A = False, B = False, C = false, D = false | javab3(False,False,False,false)," | ") 
    print(" A = False, B = False, C = false, D = true | javab3(False,False,False,true)," | ")
    print(" A = False, B = False, C = true, D = false | javab3(False,False,true,false)," | ")
    print(" A = False, B = False, C = true, D = true | javab3(False,False,true,true)," | ")
    print(" A = False, B = true, C = false, D = false | javab3(False, true,False,false)," | ")
    print(" A = False, B = true, C = false, D = true | javab3(False,true,False,true)," | ")
    print(" A = False, B = true, C = true, D = false | javab3(False,true,true,false)," | ")
    print(" A = False, B = true, C = true, D = true | javab3(False,true,true,true)," | ")
    print(" A = true, B = False, C = false, D = false | javab3(true,False,False,false)," | ")
    print(" A = true, B = False, C = false, D = true | javab3(true,False,False,true)," | ")
    print(" A = true, B = False, C = true, D = false | javab3(true,False, true,false)," | ")
    print(" A = true, B = False, C = true, D = true | javab3(true,False,true,true)," | ")
    print(" A = true, B = true, C = false, D = false | javab3(true,true,False,false)," | ")
    print(" A = true, B = true, C = false, D = true | javab3(true,true,False,true)," | ")
    print(" A = true, B = true, C = true, D = false | javab3(true,true,true,false)," | ")
    print(" A = true, B = true, C = true, D = true | javab3(true,true,true,true)," | ") 

<div/>
