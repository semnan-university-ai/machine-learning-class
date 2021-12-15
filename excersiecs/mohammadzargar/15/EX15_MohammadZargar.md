<viv dir="rtl">

همانطور که در تعاریف درخت تصمیم گفته شده الگوریتم درخت تصمیم شامل IF THEN ELSE ها می باشد؛ با یک زبان برنامه نویسی (ترجیحا پایتون، جاوا، سی پلاس پلاس) در قالب یک تابع هر درخت تصمیم مربوط به AND و OR و NOT و NAND و NOR و XOR را رسم کنید.

برای نوشتن کد ابتدا باید درخت تصمیم را داشته باشیم و برای رسم درخت ابتدا بایدجدول داده ها را پر کنیم.


|    A    |     B    |    AND    |     OR    |     NAND     |     NOR    |   XOR     |
|---------|----------|-----------|-----------|--------------|------------|-----------|
|     0   |     0    |     0     |     0     |     1        |     1      |    0      |
|     0   |     1    |     0     |     1     |     1        |     0      |    1      |
|     1   |     0    |     0     |     1     |     1        |     0      |    1      |
|     1   |     1    |     1     |     1     |     0        |     0      |    0      |

 برای NOT هم نیاز به جدول نیست. هر درایه را برعکس می کند.
  
  در مرحله بعد درخت همه را رسم می کنیم.
  
  در پایان با پایتون از روی درخت ، کد هر کدام را می نویسیم.
  
   </div>
  
  # AND
  
  ***
def zargarand(a,b): 

    if a==0: 
        return 0 
    if a==1: 
        if b==0: 
            return 0 
    if a==1: 
        if b==1: 
            return 1
print (zargarand(1,0))
***
  
  # OR
  
  def zargaror(a,b): 
  
  
    if a==1: 
        return 1 
    if a==0: 
        if b==0: 
            return 0 
    if a==0: 
        if b==1: 
            return 1
print (zargaror(1,0))

# NAND

def zargarnand(a,b): 


    if a==0: 
        return 1 
    if a==1: 
        if b==0: 
            return 1 
    if a==1: 
        if b==1: 
            return 0
print (zargarnand(1,0))

# NOR

def zargarnor(a,b): 
    if a==1: 
        return 0 
    if a==0: 
        if b==0: 
            return 1 
    if a==0: 
        if b==1: 
            return 0
print (zargarnor(1,0))

# XOR

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

# NOT

def zargarnot(a,b): 


    if a==0: 
        return 1 
    if a==1: 
        return 0 
    



  
  
  
  
  
  
  
  
  
 
