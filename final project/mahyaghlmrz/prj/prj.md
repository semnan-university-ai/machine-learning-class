<div dir="rtl">
  
  با توجه به دیتاست covid که در پوشه ی data موجود است عملیات زیر را روی این دیتاست انجام دهید:
  - نرمالیزه کردن
  - مرتب سازی داده
  - حذف داده های یکسان و تکراری
  - بدست آوردن 5 ویژگی که کمترین اهمیت را دارند
  -  اجرای الگوریتم های find-s و ce و بیز و knn و کلاسترینگ و درخت تصمیم یکبار به صورت تصادفی و یک بار با الگوریتم id3
  - داده های زیر همگی به عنوان true برچسب گذاری خواهند شد و ترکیبات داده ای دیگر به عنوان false تمام ترکیبات داده ای که قابل کشف می باشد را بدست آورید.
  - الگوریتم های اجرا شده را با rappid minner نیست اجرا کنید و نتیجه ی خود را با آن مقایسه کنید
  - دیتاست در سایت kaggle ثبت شده است در صورتی که کد خود را در بخش notebook های kaggle ثبت کنید نمره ی اضافه دریافت خواهید کرد.
  
  
<br />
  لینک kaggle
  : 
  <br />
  https://www.kaggle.com/amirshnll/covid-patient-datasets
  
</div>

<div dir="rtl">

  سایت Kaggle یکی از بهترین سایت ها در زمینه یادگیری ماشین و یادگیری عمیق است. در این سایت دیتاست های زیادی در زمینه های مختلف وجود دارد. همچنین در کنار دیتاست ها کد هایی وجود دارند که منبع بسیار مناسبی برای یادگیری نحوه حل مسائل هستند. 
  در این سایت امکان ایجاد کد هم وجود دارد.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/1.PNG)
  
<br/>
  ابتدا دیتاست مربوطه را به صورت زیر از قسمت add data در note اضافه می کنیم:
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/2.PNG)  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/3.PNG)
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/4.PNG)
  
<br/>
   اولین مرحله در تحلیل داده پیش پردازش یا preprocessing می باشد به این منظور دادگان باید مرتب سازی شوند ابتدا برای کار با داده کتابخانه های pandas و numpy را import می شود. 
   دیتاست کوید شامل 23 ستون ویژگی شامل شماره داده # ،age ، Sleep_problems ، Headache ، Diarrhea ، Abdominal_pain ، body_pain ، Body_discoloration ، Cough
      ، Fever ، Ague ، Sore_throat ، Fatigue ، runny_nose ، Chest_pain ، Decreased_appetite ، Vomit ، Nausea، Sneezing ، Shortness_of_breath ، 
   Loss_of_smell ، Loss_of_tasteو urticarial و 487 نمونه می باشد. تمامی نمونه ها مربوط به بیماران مبتلا به کوید می باشد و رویکرد ما برای دسترسی به اطلاعات بیماران سالم این است که نقیض علائم موجود در بیماران به عنوان افراد سالم جامعه باشند.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/5.PNG)  
  
<br/>
  کنترل missing value ها برای پردازش داده ضروری است بنابراین باید شناسایی شوند.
<br/> 
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/6.PNG)  
  
<br/>
   همانطور که در اطلاعات دیتاست مشخص است ویژگی سن دارای missing value های زیادی است بنابراین این ویژگی مناسب نیست به همراه شماره sample را که غیر ضروری می باشد و به عنوان یک ویژگی محسوب نمی شود از داده ها با استفاده از تابع drop حذف شده است. 
   برای حذف داده های تکراری و مشابه از داده ها با تابع drop_duplicates انجام شد است 189 تا از داده ها تکراری می باشد. 298 داده غیر تکراری باقی می ماند. 
   همچنین ویژگی headache هم یک missing value دارد این دیتا با no جایگزین شده است. 
<br/> 
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/7.PNG)  
  
<br/>
   مقدار ویژگی Abdominal_pain یکی از داده ها برابر با yes می باشد اما به صورت es ثبت شده و این مورد هم در ادامه اصلاح شده است. در این مرحله مقادیر ویژگی های باینری yes و no را به 1 و 0 تبدیل شده است.
   با ساختن یک کپی از دیتا اصلاح شده و تغییر صفر ها به یک و برعکس داده های منفی در واقع داده مربوط به افراد سالم جامعه تولید می شود. این دو دیتاست را با دستور append ادغام و پس از آن با دستور random به صورت رندم ترتیب می شوند.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/8.PNG)  
  
<br/>
   Data شامل 298 دیتا با برچسب 1 به عنوان افراد بیمار و 298 داده با برچسب 0 و سالم می باشد.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/data.PNG)   
  
  ### الگوریتم find-s
  
  در الگوریتم find-s فرض بر این است که همه فضای ویژگی منفی است مگر این که با ورود مثال مثبت این فرضیه تغییر کند. در این روش عملا نمونه های منفی تاثیری در فرضیه نهایی ندارد. در نهایت فرضیه به صورت h=<∅,∅,…,∅>
  که نشان می دهد هیچ یک از ویژگی های انتخابی مناسب نیست و این الگوریتم برای این داده ها جواب نداده است.من در نهایت به این نتیجه رسیدم که چون داده نرمال شده به عنوان ورودی این الگوریتم در نظر گرفته شده است فرضیه مطلوبی حاصل نشده است. 
  تابع enumerate یک تابع از پیش‌ساخته شده و موجود در خود برنامه Built-in در پایتون python است. این تابع برای یک لیست، عناصر و اندیس‌های آن را با هم در نظر می‌گیرد.
  حالت don’t care با -1  نشان داده شده است.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/9.PNG)   
  
  ### Candidate Elimination algorithm
    
  الگوریتم CE با تعیین یک فرضیه اختصاصی و یک فرضیه عمومی ایجاد کرده و با ورود داده با برچسب مثبت و منفی این فرضیه ها را آپدیت می کند در نهایت فرضیه های S و G به سمت یکدیگر همگرا شده و فرضیه های که در این بین باقی می ماند به عنوان پاسخ این الگوریتم در نظر گرفته می شود.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/11.PNG)   
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/10.PNG)   
<br/>
  همانطور که می دانیم این الگوریتم برای داده های زیاد پاسخ خوبی ارایه نمی دهد بنابراین در نهایت فرضیه نهایی عمومی به صورت don’t care برای تمام ویژگی ها و فرضیه اختصاصی نسبت به ویژگی های 2، 5 ، 10، 11، 12 و 17 don’t care می باشد.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/12SG.PNG)

  برای ارزیابی الگوریتم های مبتنی بر نمونه IBL نیاز است تعدادی از داده ها را به عنوان تست در نظر گرفته و بر اساس داده های باقی مانده که به عنوان داده train در نظر گرفته شده classifier خود را train کرده. سپس میزان صحت الگوریتم برای داده تست گزارش می شود.  
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/13splitdata.PNG) 
  
<br/>
  با استفاده ازتابع train_test_split از کتابخانه sklearn.model_selection 30% داده ها به عنوان داده تست و 70% داده ها به عنوان داده train در نظر گرفته شده است.

  ### Naive Bayes Algorithm

  الگوریتم Naïve Bayes را از طریق کتابخانه sklearn اجرا کرده پس از fit شدن بر روی داده train و اعمال بر روی داده تست با دستور predict داده تست را طبقه بندی می شود. با استفاده از کتابخانه confusion_matrix TP، TN، FP، FN و classification_report پارامتر هایی مثل صحت، recall، f1-score را نشان می دهد.
  صحت الگوریتم برابر با 98% می باشد
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/14naivebayes.PNG) 
  
<br/>
  
<br/>
    
  ### K-NN
  
  الگوریتم knn با در نظر گرفتن k همسایگی نزدیک هر یک از داده ها از طریق محاسبه فاصله آن داده برچسبی را تعیین می کند. صحت این الگوریتم برای k=5 برابر با 98% می باشد.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/15KNN.PNG) 
  
<br/>
  
  ### الگوریتم درخت تصمیم
  
  الگوریتم درخت تصمیم بر روی دیتا تست صحتی برابر با 99% دارد.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/16tree.PNG) 
  
<br/>

 
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/plotTree.PNG) 
  
  ### الگوریتم ID3
  
  در این الگوریتم توابعی برای محاسبه آنتروپی و information gain تعیین شده است. الگوریتم ID3 برای این داده ها مناسب نیست به این دلیل که  انتروپی آن برابر 1 می باشد.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/17id3.PNG) 
  
<br/>
  با استفاده از یک حلقه for برای دو الگوریتم decision tree و naïve bayes  ویژگی ها حذف و صحت گزارش شده و میزان صحت به دست آمده پس از حذف هر کدام از ویژگی ها با استفاده از تابع sort ترتیب از زیاد به کم ترتیب شده است. بنابراین 5 صحت اول کم اهمیت ویژگی ها را نشان می دهد.
<br/>
  
  ![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/mahyaghlmrz/prj/img/removeFeature.PNG) 
  
<br/>
  
<br/>
  لینک دسترسی به کد های ضمیمه شده به این دیتاست covid:  

: 
  <br />
https://www.kaggle.com/mahyagh/covid-project-mahyagh

</div>
