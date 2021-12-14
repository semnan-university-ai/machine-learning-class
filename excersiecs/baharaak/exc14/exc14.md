## با کمک سه روش درخت تصمیم، حذف کاندید و id3 داده ها را حل کنید:


  
| Example | Size  | Color | Shape    | Class/Label |
|---------|-------|-------|----------|-------------|
| 1       | big   | red   | circle   | No          |
| 2       | big   | red   | triangle | Yes         |
| 3       | small | red   | circle   | No          |
| 4       | big   | red   | triangle | No          |
| 5       | small | blue  | circle   | No          |



#### روش حذف کاندید:

s0=<0,0,0>

G0=<؟,؟,؟>


X1=<big, red, circle>-

s1=<0,0,0>

G1=<small,؟> <؟,؟,blue, ؟,؟> <؟, triangle>


X2=<big, red, triangle>+

s2=<big, red, triangle>

G2=<؟,؟, triangle>


X3=<small, red, circle>-

s3=<big, red, triangle>

G3=<؟,؟, ؟>


X4=<big, red, triangle>-

s4=<big, red, triangle>

G4=<؟,؟, ؟>


X5=<small, blue, circle>-

s5=<big, red, triangle>

G5=<؟,؟, ؟>


### درخت تصمیم



### روش id3





