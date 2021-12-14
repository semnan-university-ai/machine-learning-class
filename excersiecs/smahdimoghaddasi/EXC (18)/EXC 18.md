 
 
 <div dir="rtl">
  
  ### 18) فرمول آنتروپی در روش ID3 را بدون استفاده از توابع آماده ی زبان های برنامه نویسی خود برنامه نویسی کنید.
 <br/>
 <br/>
  برای مثال آنتروپی دیتاست سوال 8 را بدست می آوریم.
 </div> 
   آنتروپی کل: Entropy(S) = -(P+logP+ + P-logP-)= -3/12 log(3/12)-9/12log (9/12)=.811
   
 <br/>
 <br/>
 <br/>
 
| day | outlook  | temperature | humidity | windy | play |
|-----|----------|-------------|----------|-------|------|
| 1   | overcast | hot         | high     | false | yes  |
| 2   | rainy    | mild        | high     | false | yes  |
| 3   | rainy    | cool        | normal   | false | no   |
| 4   | sunny    | mild        | high     | false | no   |
| 5   | overcast | mild        | high     | false | yes  |
| 6   | sunny    | cool        | normal   | true  | no   |
| 7   | sunny    | hot         | normal   | true  | yes  |
| 8   | rainy    | cool        | high     | false | yes  |
| 9   | sunny    | cool        | high     | false | yes  |
| 10  | overcast | cool        | normal   | true  | yes  |
| 11  | sunny    | hot         | high     | true  | yes  |
| 12  | rainy    | hot         | high     | true  | yes  |



```
def entropy(labels):
#def log(x):
#n=1000.0
#return n*((x**(1/n))-1)
    
    def log(x):
     tol=1e-13
     res=0.0
     
     #integer part
     while x<1:
         res -= 1
         x *= 2
     while x>= 2:
         res += 1
         x /= 2
         
     #fractional part
     fp=1.0
     while fp>=tol:
         fp /= 2
         x *= x
         if x >= 2:
             x /= 2
             res += fp
             
     return res
  
    n_labels = len(labels)

    di = dict();
    
    for i in set(labels):
        di[i]=0
    
    for la in labels:
        di[la]+=1
            
    counts = []
    for k,v in di.items():
        counts.append(v)
        
    prob = [0]*len(counts)
    
    for i in range(len(counts)):
        prob[i]=counts[i]/n_labels
        
    
    ent = 0.0
    for i in prob:
      ent -= i * log(i)
    
    return ent

#READ DATASET
    
with open("Data.txt","r") as f:
    txt = f.read()   
txt = txt.split("\n")

heads = txt[0].split('|')

heads = [w.strip() for w in heads]
del heads[0]
heads.pop()

data = []

for line in range(2,len(txt)):
    line = txt[line].split('|')
    line = [w.strip() for w in line]
    del line[0]
    line.pop()
    data.append(line)
    
#trasposing
data = [list(x) for x in zip(*data)]

e = entropy(data[-1])
print("Entropy for {:15} = {:10.5f}".format(heads[-1],e))
    

#labels = ["yes", "yes", "no", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes"]
#print(entro(labels))
```
<br/> 
خروجی:

Entropy for play            =    0.81128 

همانطور که انتظار داشتیم در خروجی برنامه هم به عدد 0.811 رسیدیم.
