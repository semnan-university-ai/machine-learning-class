<div dir="rtl">
سوال : با توجه به دیتاست covid که در پوشه ی data موجود است عملیات زیر را روی این دیتاست انجام دهید:
</div>  
<br/>

<div dir="rtl">
  
نرمالیزه کردن

مرتب سازی داده
  
حذف داده های یکسان و تکراری
  
بدست آوردن 5 ویژگی که کمترین اهمیت را دارند
  
اجرای الگوریتم های find-s و ce و بیز و knn و کلاسترینگ و درخت تصمیم یکبار به صورت تصادفی و یک بار با الگوریتم id3
  
داده های زیر همگی به عنوان true برچسب گذاری خواهند شد و ترکیبات داده ای دیگر به عنوان false تمام ترکیبات داده ای که قابل کشف می باشد را بدست آورید.
  
الگوریتم های اجرا شده را با rappid minner نیست اجرا کنید و نتیجه ی خود را با آن مقایسه کنید
  
دیتاست در سایت kaggle ثبت شده است در صورتی که کد خود را در بخش notebook های kaggle ثبت کنید نمره ی اضافه دریافت خواهید کرد.
  
</div> 

<br/>

<div dir="rtl">
شروع
</div>
<br/>
<div dir="rtl">
ابتدا فایل json را از کاگل دانلود و سپس در گوگل درایو بارگذاری میکنیم 
</div>  
<br/>

<div dir="rtl">
  
کتابخانه های مربوطه را فراخوانی میکنیم

کتابخانه پانداس  

import pandas as pd

کتابخانه نام پای

import numpy as np

پیش پردازش دیتاها

from sklearn import preprocessing

فراخوانی فایل json بارگذاری شده در گوگل درایو

data=pd.read_json("/content/drive/MyDrive/data/covid.json")

چاپ داده ها

print(data)
  
</div>

<br/>
***********************************************************************************************
<div dir="rtl">
  
استانداردسازی و نرمال‌سازی
  
با توجه به قابلیت انجام محاسبات برداری در کتابخانه Numpy در پایتون می‌توان محاسبات و تبدیلات مربوط به استانداردسازی و نرمال‌سازی را انجام داد ولی راه ساده‌تر استفاده از کتابخانه scikit-learn و توابع درون آن است
<div/>
<br/>
  
<div dir="rtl">
پیش‌پردازش داده‌ها(Preprocessing the Data)
<div/>

<div dir="rtl">
در زندگی روزمره ما با داده‌های زیادی سروکار داریم اما این داده‌ها به صورت خام هستند. برای آماده‌سازی داده به عنوان ورودی الگوریتم‌های یادگیری ماشین، باید آن را به یک داده معنی دار تبدیل کنیم. اینجاست که پیش‌پردازش داده‌ها به تصویر کشیده می‌شود. به عبارت دیگر، می‌توان گفت قبل از ارائه داده‌ها به الگوریتم‌های یادگیری ماشین، ما نیاز به پیش‌پردازش داده‌ها داریم.
<div/>

<div dir="rtl">
اگر از پایتون استفاده می کنیم، پیش‌پردازش اطلاعات اولین قدم برای تبدیل داده‌ها به یک قالب خاص، یعنی پردازش اولیه خواهد بود و می‌تواند به شرح زیر انجام شود:
<div/>
  
import numpy as np
  
import sklearn.preprocessing

<div dir="rtl">
NumPy – اساساً NumPy یک بسته پردازش آرایه با هدف کلی است که برای دستکاری موثر آرایه های بزرگ چند بعدی از پرونده های دلخواه ساخته شده است بدون اینکه سرعت زیادی را برای آرایه های چند بعدی کوچک قربانی کند.
<div/>
  
  
<div dir="rtl">  
Sklearn.preprocessing – این بسته بسیاری از توابع ابزار مشترک و کلاس‌های تبدیل کننده را برای تغییر بردارهای ویژگی خام به به نمایشی فراهم می کند که برای الگوریتم‌های یادگیری ماشین مناسب‌تر است.    
<div/>
<br/>
  
<div dir="rtl">  
نمایش داده
</div>
  
![show data](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/1.jpg)

<div dir="rtl">  
دریافت اطلاعات دیتاست
</div>  
  
![get info data](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/2.jpg)  
  
<div dir="rtl">  
مرتب سازی بر اساس نام
</div>   

![get info](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/4.jpg)  

<div dir="rtl">  
نرمال سازی
</div>    
  
![normalize](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/5.jpg)  
  
<div dir="rtl"> 
حذف داده های تکراری  
</div>
  
![duplicate](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/6.jpg)  

  
![duplicate](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/7.jpg)    
  
<div dir="rtl"> 
اهمیت مرحله انتخاب ویژگی در طراحی مدل‌های یادگیری
تحقیقات انجام شده در زمینه تاثیر انتخاب ویژگی‌های مناسب در عملکرد روش‌های یادگیری ماشین، نشان داده است که انتخاب مجموعه مناسب از ویژگی‌ها در هنگام طراحی مدل‌های یادگیری ماشین، عملکرد، دقت و کارایی روش‌های یادگیری «نظارت شده» (Supervised) و «نظارت نشده» (Unsupervised) را بهبود می‌بخشد. همچنین، وقتی که ابعاد فضای ویژگی داده‌ها بسیار زیاد است و با معضل «نفرین ابعاد بالا» (Curse of Dimensionality) مواجه هستیم، استفاده از مجموعه ویژگی‌های مناسب، «هزینه‌های محاسباتی» (نظیر زمان آموزش و یا منابع) لازم برای آموزش بهینه سیستم را به شدت کاهش می‌دهد. محاسبه درجه اهمیت ویژگی‌ها و استفاده از آن‌ها در مرحله انتخاب ویژگی، گام مهمی در جهت «تفسیرپذیری» (Interpretability) مدل‌های یادگیری ماشین خواهد بود. 
</div>

<div dir="rtl"> 
پنج ویژگی کم اهمیت
</div>

clf=RandomForestClassifier(n_estimators=100)
  
clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


<br/>

<div dir="rtl">
اجرای الگوریتم های find-s
<dir/>
  
<br/>

![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/8finds.jpg)
  
![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/9finds.jpg)
  
![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/10finds.jpg)  
  
<div dir="rtl">
knn الگوریتم
</div>
<br/>  
<div dir="rtl">  
الگوریتم K نزدیک ترین همسایه (KNN)  
</div> 

<div dir="rtl">
الگوریتم Knn در حقیقت به معنی الگوریتم یافتن نزدیکترین همسایه است. Knn مخفف K nearest neighbor بوده و بیشترین استفاده از این الگوریتم در یادگیری ماشین ( machine learning ) و همچنین داده کاوی می باشد. این الگوریتم یک الگوریتم ناپارامتری بوده که همین امر سبب می شود به نسبت الگوریتم های دیگر سادگی بیشتری داشته و استفاده بیشتری نیز داشته باشد.
</div>  

  
![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/1knn.jpg)

<div dir="rtl">
ce الگوریتم
<dir/> 
    
![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/ce.jpg)  

<div dir="rtl">
الگوریتم ID3
</div>  
  
![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/1id3.jpg)
  
![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Homayontoosy/pic/2id3.jpg)  
  
