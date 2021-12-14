### الگوریتم find-s را برای داده های زیر استفاده کنید.
<div align="center">

|     Example    |     Size     |     Color    |     Shape       |     Class/Label    |
|----------------|--------------|--------------|-----------------|--------------------|
|     1          |     big      |     red      |     circle      |     No             |
|     2          |     small    |     red      |     triangle    |     No             |
|     3          |     small    |     red      |     circle      |     Yes            |
|     4          |     big      |     blue     |     circle      |     No             |
|     5          |     small    |     blue     |     circle      |     Yes            |

</div>

```
h0= <0 , 0 ,0 >
```
```
x1= < big, red, circle> -> no
h1= <0, 0, 0 > = h0
```
```
x2= <small, red, triangle> -> no
h2= <0, 0, 0 > = h1
```
```
x3= <small, red, circle> -> yes
h3= <small, red, circle>
```
```
x4= <big, blue, circle> -> no
h4= <small, red, circle> = h3
```
```
x5= <small, blue, circle> -> yes
h5= < small, ?, circle>
```
<div dir="rtl">
فرضیه نهایی : < small, ?, circle>
  </div>
