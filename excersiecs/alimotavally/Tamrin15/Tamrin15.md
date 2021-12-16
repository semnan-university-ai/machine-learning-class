<div dir="rtl">
  
  ### همانطور که در تعاریف درخت تصمیم گفته شده الگوریتم درخت تصمیم شامل IF THEN ELSE ها می باشد؛با یک زبان برنامه نویسی (ترجیحا پایتون، جاوا، سی پلاس پلاس) در قالب یک تابع هر درخت تصمیم مربوط به AND و OR و NOT و NAND و NOR و XOR را رسم کنید.
      
  </div>
  
 **AND:**
 ```
 def and(A,B): 
    if A==1 and B==1:
        return 1
    else:
        return 0
    print (and(0,1))
   ```
   
 **OR:**
 ```
   def or(a, b): 
    if a == 1: 
        return 1
    elif b == 1: 
        return 1
    else: 
        return 0
    
    print (or(0,1))
   ```
    
 **NOR:**
 ```
    def nor(A, B): 
    if(A == 0) and (B == 0): 
        return 1
    else: 
        return 0  
   ```


 **NAND:**
 ```
    def nand (A, B): 
    if A == 1 and B == 1: 
        return 0
    else: 
        return 1
   ```
    
 **NOT:**
 ```
      def not(a,b): 
    if a==0: 
        return 1 
   else: 
        return 0 
   ```
       
 **XOR:**
 ```
      def xor (A, B): 
    if A != B: 
        return 1
    else: 
        return 0 
   ```
 
     
