<div dir="rtl">
  
  ### الگوریتم find-s را برای داده های زیر استفاده کنید.
  
|     Example    |     Size     |     Color    |     Shape       |     Class/Label    |
|----------------|--------------|--------------|-----------------|--------------------|
|     1          |     big      |     red      |     circle      |     No             |
|     2          |     small    |     red      |     triangle    |     No             |
|     3          |     small    |     red      |     circle      |     Yes            |
|     4          |     big      |     blue     |     circle      |     No             |
|     5          |     small    |     blue     |     circle      |     Yes            |
  
  </div>
  
  
<div dir="rtl">  
خاص ترین فرضیه   
<div/>

h0= <0 , 0 ,0 >   
   
x1= < Circle, Red, Big> -> h1= <0, 0, 0 > = h0

x2= < triangle, Red, Small> -> h2= <0, 0, 0 > = h1

x3= < Circle, Red, Small> -> h3= < Circle, Red, Small> -> yes

x4= < Circle, Big, Big> -> h4= < Circle, Red, Small> = h3

x5= < Circle, Big, Small> -> h5= < Circle, ?, Small>
  
 
فرضیه نهایی h5   
 
