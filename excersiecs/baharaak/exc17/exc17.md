# الگوریتم find-s برای داده های زیر 

در این جدول ما پنج نمونه اموزشی با سه ویژگی 
<size, color, shape > داریم

برای نوشتن الگوریتم find-s  در مرحله اول h0 را خاص ترین فرضیه درنظر میگیریم :

h0<0,0,0>

نمونه اموزشی اول را وارد الگوریتم میکنیم چون این نمونه منفی است و پیش فرض ما تمامی نمونه ها منفی هستند بنابراین تغییری در h0 ایجاد نمیشود

x1<big, red, circle>-

h1=h0<0,0,0>

نمونه اموزشی دوم هم منفی میباشد بنابراین تغییری تا اینجا برای فرضیه ایجاد نمیشود و فرضیه خاص ترین حالت ممکن خود را دارد:

x2<small, red, triangle>-

h2=h1=h0<0,0,0>

زمانی که نمونه اموزشی سوم را وارد الگوریتم میکنیم چون نمونه ها مثبت هستند فرضیه را تغییر میدهدو با مقادیر کلی تری جایگزین میشوند:

x3=<small, red, circle>+

h3=<small, red, circle>

نمونه اموزشی چهارم هم منفی میباشد و فرضیه را تغییر نمیدهد:

x4=<big, blue, circle>-

h4=h3=<small, red, circle>

نمونه اموزشی پنجم مثبت میباشد وفرضیه h5 را کلی تر میکند و در نمونه دوم چون الگوریتم هر دوحالت باینری را دیده است از علامت ؟ استفاده میکنیم:

x4=<small, blue, circle>+

h4=h3=<small, ?, circle>

فرضیه با تمامی نمونه های اموزشی سازگار است
