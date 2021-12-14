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

خطا را برای سه ویژگی به دست می اوریم، هر ویژگی که خطای کمتری داشته باشد به عنوان گره درخت انتخاب میشود:

![1](1.png)

پس shape با خطای کمتر انتخاب میشود، در قسمت circle به جواب قطعی no میرسیم ولی در قسمت triangle تناقض داریم بنابراین نمیتوانیم به طور قطعی گره بعدی را انتخاب کنیم.



### روش id3





