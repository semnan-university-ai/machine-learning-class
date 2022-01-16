
## rapidminer
<div dir="rtl">
  ابتدا دیتاست را درقسمت repository 
  اضافه می کنیم چون  می خواهیم چند الگوریتم را روی آن بررسی کنیم
  می بینیم 17 ستون که یکی از آن ها لیبل است و 454 مثال دارد  که همان ديتاست نهايي است که لیبل های منفی را خودمان ساختيم
</div>
<br/>



![20.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/20.jpeg)


### KMEANS:
<div dir="rtl">
  برای kmeans ،از قسمت operator ، clustring را انتخاب می کنیم و اتصالات را وصل می کنیم
 اگر run کنیم  خطایی داریم مبنی بر اینکه یک ویژگی داریم که عددی نیست و yes , no است باید به rapidminer بفهمانیم که این ستون لیبل است 
   پس از یک ماژول به نام set rule   بین دیتا و کلاسترینگ استفاده می کنیم
   از قسمت attribute name ما class را انتخاب می کنیم
  target rule هم lable قرار می دهیم یعنی ویژگی کلاس، لیبل است.
  
  حال run می گیریم و مدل kmeans ساخته می شود
  

![08.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/08.jpeg)


<div dir="rtl">
  نتایج KMEANS:<br/>
  کلاس صفر تعداد187 آیتم و کلاس یک تعداد 267 آیتم دارد
  در ماژول کلاسترینگ  پارامترهای قابل تنظیمی وجود دارد مانند k  که تعداد خوشه هاست که ما آن را دو در نظر گرفتیم و تعداد ران ها که ما 10 لحاظ کردیم.
  و هرچه بیشتر باشد تعداد آپدیت ها بیشتر می شود.
   بعد از ساخت مدل می خواهیم performance آن را بسنجیم 
  در خوشه بندی برای بررسی عملکرد از cluster distance performance استفاده میکنیم  
  امابرای کلاسیفیکیشن باید از ماژول  performance (classification ) استفاده کنیم
  
  خروجی های clustring را به صورت زیگزاگی به performance وصل می کنیم
  و خروجی های performance را به result 
  و حال ران بگیریم به ما اطلاعات performance میانگین فاصله از مرکز ، میانگین فاصله از خوشه 0 ، میانگین فاصله از خوشه یک  و Davies Bouldin    که معیاری برای ارزیابی k means است 
  را می دهد 
  </div>
  
  

![09.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/09.jpeg)

![010.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/010.jpeg)


### DT:
  
<div dir="rtl">
  تقریبا شبیه به kmeans است اما باید داده ها راتقسیم بندی کنیم
  پس از اپراتور split validation استفاده می کنیم
  پارامتری دارد به نام split ratio 
  که ما آن را 0.7
گرفتیم یعنی 70 درصد داده ها برای آموزش باشند
 این ماژول دو قسمت training و testing دارد
   در این قسمت ماژول های مورد نظر از جمله Decision Tree - Apply Model - performance را drop  می کنیم و اتصالات را لحاظ کرده  و ران می گیریم 
 </div>
  



  
  
![03.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/03.jpeg)
![21.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/21.jpeg)
  
  <div dir="rtl">
  نتایج DT:<br/>
  می بینیم کلاس no دارای دقت 81.82 درصد و کلاس yes دارای دقت 77.97 درصد است
  که برای دیتاست ما که اکثر دیتاها دیتای فیک بودند درصد قابل قبولی است
  درخت هم رسم شده که درخت بسیار بزرگی است
  </div>

![02.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/02.jpeg)



  
  

![04.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/04.png)

![05.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/05.png)

![06.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/06.png)

![07.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/07.png)
 



### KNN
<div dir="rtl">
  مدل knn را می سازیم  و ساخت مدل مثل مدل های قبل است
  </div>


![011.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/011.jpeg)



<div dir="rtl">
  نتایج KNN:<br/>
  مقدار k را برابر 3 گرفتم و 
  می بینیم کلاس no دارای دقت 88.31 درصد و کلاس yes دارای دقت 84.75 درصد است
که برای دیتاست ما دقت قابل قبولی است
  </div>


![99.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/99.jpeg)

![013.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/013.jpeg)




### NB
<div dir="rtl">
  مدل naive bayes را می سازیم  و ساخت مدل مثل مدل های قبل است
  </div>
  
  

![014.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/014.jpeg)


<div dir="rtl">
  نتایج NB:<br/>
  می بینیم کلاس no دارای دقت 85.71 درصد و کلاس yes دارای دقت 76.27 درصد است
 </div>
  
  

![015.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/015.jpeg)

![016.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/016.jpeg)


