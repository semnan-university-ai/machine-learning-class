
<div dir="rtl">
  
  ### 17) الگوریتم find-s را برای داده های زیر استفاده کنید.
  </div>
  
|     Example    |     Size     |     Color    |     Shape       |     Class/Label    |
|----------------|--------------|--------------|-----------------|--------------------|
|     1          |     big      |     red      |     circle      |     No             |
|     2          |     small    |     red      |     triangle    |     No             |
|     3          |     small    |     red      |     circle      |     Yes            |
|     4          |     big      |     blue     |     circle      |     No             |
|     5          |     small    |     blue     |     circle      |     Yes            |
  
   
 <div dir="rtl">
  حل :
   </div>
  <br/>
 h0= <0 , 0 ,0 > : خاص ترین فرضیه  <br/> <br/>
  
  x1= <Big, Red, Circle>  - <br/>
  h1= <0, 0, 0 > = h0    <br/> <br/>
  
  x2= <Small, Red, Triangle>  - <br/>
  h2= <0, 0, 0 > = h1   <br/> <br/>
  
  x3= <Small, Red, Circle>  +  <br/>
  h3= <Small, Red, Circle>   <br/> <br/>
  
  x4= <Big, Blue, Circle>  -  <br/>
  h4= <Small, Red, Circle>  = h3    <br/> <br/>
  
  x5= <Small, Blue, Circle >  + <br/>
  h5= <Small, ?, Circle> <br/> <br/>
  
  h= <Small, ?, Circle> : فرضیه نهایی 
  
  </div>
  
