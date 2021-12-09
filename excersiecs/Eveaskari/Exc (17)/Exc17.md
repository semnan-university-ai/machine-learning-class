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
  
  <div dir="ltr">
  
  <br/>
  h0= <0 , 0 ,0 >  <br/>
  x1= < C, R, B>  ->  h1= <0, 0, 0 > = h0    <br/>
  x2= < T, R, S>  ->  h2= <0, 0, 0 > = h1   <br/>
  x3= < C, R, S>  ->  h3= < C, R, S> -> yes    <br/>
  x4= < C, B, B>  ->  h4= < C, R, S> = h3    <br/>
  x5= < C, B, S>  ->  h5= < C, ?, S>    <br/>
  فرضیه نهایی h5
  
  </div>
