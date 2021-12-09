<div dir="rtl">
سوال: همانطور که در تعاریف درخت تصمیم گفته شده الگوریتم درخت تصمیم شامل IF THEN ELSE ها می باشد؛ با یک زبان برنامه نویسی (ترجیحا پایتون، جاوا، سی پلاس پلاس) در قالب یک تابع هر درخت تصمیم مربوط به AND و OR و NOT و NAND و NOR و XOR را رسم کنید.  
<div/>
<br/>

<div dir="rtl">
برای AND
</div>  

def AND (a, b): 
  
    if a == 1 and b == 1: 
        return True
    else: 
        return False  


if __name__=='__main__': 
  <br/>
    print(AND(1, 1)) 
  
    print("+---------------+----------------+") 
    print(" | AND Truth Table | Result |") 
    print(" A = False, B = False | A AND B =",AND(False,False)," | ") 
    print(" A = False, B = True | A AND B =",AND(False,True)," | ") 
    print(" A = True, B = False | A AND B =",AND(True,False)," | ") 
    print(" A = True, B = True | A AND B =",AND(True,True)," | ")   
 
<br>

<div dir="rtl">
برای OR
</div>   

def OR(a, b): 
    if a == 1: 
        return True
    elif b == 1: 
        return True
    else: 
        return False
 <br/>
 if __name__=='__main__': 
    print(OR(0, 0)) 
  
    print("+---------------+----------------+") 
    print(" | OR Truth Table | Result |") 
    print(" A = False, B = False | A OR B =",OR(False,False)," | ") 
    print(" A = False, B = True | A OR B =",OR(False,True)," | ") 
    print(" A = True, B = False | A OR B =",OR(True,False)," | ") 
    print(" A = True, B = True | A OR B =",OR(True,True)," | ") 
  <br/>
  
<div dir="rtl">
برای NOT
</div>  
<br/>

def NOT(a): 
    if(a == 0): 
        return 1
    elif(a == 1): 
        return 0
 
if __name__=='__main__': 
    print(NOT(0)) 
<br/>
print("+---------------+----------------+") 
    print(" | NOT Truth Table | Result |") 
    print(" A = False | A NOT =",NOT(False)," | ") 
    print(" A = True, | A NOT =",NOT(True)," | ") 
  
  
