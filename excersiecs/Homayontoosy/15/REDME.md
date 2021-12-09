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
    print(AND(1, 1)) 
  
    print("+---------------+----------------+") 
    print(" | AND Truth Table | Result |") 
    print(" A = False, B = False | A AND B =",AND(False,False)," | ") 
    print(" A = False, B = True | A AND B =",AND(False,True)," | ") 
    print(" A = True, B = False | A AND B =",AND(True,False)," | ") 
    print(" A = True, B = True | A AND B =",AND(True,True)," | ")   
 
