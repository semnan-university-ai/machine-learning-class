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
  
<br/>
: 
  <br />
https://www.kaggle.com/mahyagh/covid-project

</div>
