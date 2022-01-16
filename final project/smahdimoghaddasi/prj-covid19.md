 
 <div dir="rtl">
  
  با توجه به دیتاست covid که در پوشه ی data موجود است عملیات زیر را روی این دیتاست انجام دهید:
  - نرمالیزه کردن
  - مرتب سازی داده
  - حذف داده های یکسان و تکراری
  - بدست آوردن 5 ویژگی که کمترین اهمیت را دارند
  -  اجرای الگوریتم های find-s و ce و بیز و knn و کلاسترینگ و درخت تصمیم یکبار به صورت تصادفی و یک بار با الگوریتم id3
  - داده های زیر همگی به عنوان true برچسب گذاری خواهند شد و ترکیبات داده ای دیگر به عنوان false تمام ترکیبات داده ای که قابل کشف می باشد را بدست آورید.
  - الگوریتم های اجرا شده را با rapidminer نیست اجرا کنید و نتیجه ی خود را با آن مقایسه کنید
  - دیتاست در سایت kaggle ثبت شده است در صورتی که کد خود را در بخش notebook های kaggle ثبت کنید نمره ی اضافه دریافت خواهید کرد.
  
  
<br />
  لینک kaggle
  : 
  <br />
  </div>
  https://www.kaggle.com/amirshnll/covid-patient-datasets
<div dir="rtl">

حل:
ابتدا باید کتابخانه های لازم را فراخوانی کنیم:
<br />
  کتابخانه pandas :
    این کتابخانه می‌تواند داده‌ها را با بهره‌گیری از ساختارهای Series و DataFrame که ارائه می‌کند، به قالبی که برای تحلیل داده‌ها مناسب هستند، مبدل سازد.
    بسته پانداس حاوی چندین متد برای پالایش مناسب داده‌ها است.
    پانداس دارای ابزارهای گوناگونی برای انجام عملیات ورودی/خروجی است و می‌تواند داده‌ها را از فرمت‌های گوناگونی شامل MS Excel ،TSV ،CSV و دیگر موارد بخواند.

کتابخانه numpy:
با استفاده از این کتابخانه امکان استفاده از آرایه‌ها و ماتریس‌های بزرگ چند بعدی فراهم می‌شود. هم‌چنین می‌توان از تابع‌های ریاضیاتی سطح بالا بر روی این آرایه‌ها استفاده کرد

از کتابخانه یsklearn model_selection ما train_test_split را فراخوانی کردیم برای تقسیم بندی داده ها به train و test
  
کتابخانه ی matplotlib.pyplot  برای رسم نمودار ها فراخوانی شد و کتابخانه ی seaborn برای کانفیوژن ماتریس مورد استفاده قرار گرفت
  
</div>

```  
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
```
<div dir="rtl">
در این قسمت دیتاست کوید را خواندیم  که شامل ویژگی هایی است ( 23 ویژگی و 487 نمونه دارد)

</div>

```
covid = pd.read_excel('covid.xlsx');
covid

```

</div>

![1.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/1.jpeg)

</div>

<div dir="rtl">
در این مرحله باید دیتاست را پاکسازی کنیم و سطرهای اضافه را هم حذف کنیم تا به دقت بالاتری دست یابیم. همانطور که در دیتاست می بینیم  ستون # اضافه است که فقط  ستون را نشان می دهد و برای ویژگی
  age  بیشتر مقادیر missvalue هستند  اگر تعداد داده های فراموش شده کم باشد می توان با روش هایی از جمله میانگین گیری آن ها را بدست آورد اما در اینجا من تصمیم به حذف این ویژگی گرفتم  چون وجودش باعث از دست رفتن دقت در نتایج می شود پس در اینجا# و سن را حذف کردم  
و تعداد ویژگی های ما 21  می شود
</div>

```
covid=covid.drop(['#'], axis=1);
covid

covid=covid.drop(['age'], axis=1);
covid
```


![2.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/2.jpeg)

</div>

<div dir="rtl">
با دستور describe یک توصیف کلی از دیتا خواهیم داشت که از دستوری از کتابخانه ی pandas است 
اطلاعاتی همچون count را به ما میدهد . همانطور که می بینیم بیشتر count ها 487 هستند  اما Headache  486 است و این نشان دهنده ی یک مقدار فراموش شده در این ویژگی است

قسمت بعد unique را نشان میدهد چون دیتاست ما yes no است تعداد unique را  باید دو نشان دهد اما برای  Diarrhea میبینیم این عدد 4 و برای Headache عدد 3 را نشان می دهد پس این دو ویژگی را باید بررسی کنیم 


</div>

```
covid.describe()
```

![3.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/3.jpeg)

</div>
<div dir="rtl">
 برای ویژگی Diarrhea دیدیم unique را 4 نشان داد در این مرحله میخواهیم  مشکل را پیدا کنیم با دستور unique  می بینیم که علت در نحوه ی نوشتن yes و no است که گاهی با حروف کوچک
  (yes و no) و گاهی با حروف بزرگ ( YES و NO ) در دیتاست وجود دارد
  
</div>
 
```
covid.Diarrhea.unique()
  
```  
array(['yes', 'no', 'Yes', 'No'], dtype=object)

</div>
<div dir="rtl">
 برای رفع مشکل بالا yes را به YES  و  no را به NO .تبدیل می کنیم 
</div>


```
covid=covid.replace({'yes':'Yes', 'no':'No'});
```


</div>
<div dir="rtl">
  مجدد describe می زنیم و برای Abdominal.pain میبینیم 3 است  مجدد  unique اش را میبینیم که متوجه می شویم متغیری به اسم "es" است  که همان YES است
</div>


```
covid.describe()
```


![4.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/4.jpeg)

</div>



```
covid.Abdominal_pain.unique()
```

array(['Yes', 'No', 'es'], dtype=object)


</div>
<div dir="rtl">
در این مرحله این متغیر را اصلاح می کنیم به YES و Replace می کنیم به YES و unique می گیریم و می بینیم فقط   YES و NO داریم
  
</div> 
 
 
 
```
covid=covid.replace({'es':'Yes'});
covid.Abdominal_pain.unique()
```

array(['Yes', 'No'], dtype=object)

</div>
<div dir="rtl">
 
  حال باید ببینیم کجاهای جدول null هستند. دیدیم در Headache، 486 تا بود پس مینویسیم:
  یعنی ایندکس null ها را پیدا کنیم و میبینیم در آرایه 396 ستون 2 null است
  </div>
  
  
  ```
  np.where(pd.isnull(covid))
  ```
 
(array([396]), array([1]))
  
  
</div>
<div dir="rtl">
در سطر 397 یه دونه خالی هست و باید حذف شود
 سپس اگر null بزنیم آرایه ی خالی به ما بر می گرداند
</div>


```
covid=covid.drop(covid.index[396])
np.where(pd.isnull(covid))
```

(array([], dtype=int64), array([], dtype=int64))

</div>
<div dir="rtl">
  برای ادامه یکار باید دیتاها را عددی کنیم و به صفر و یک (باینری) تبدیل کنیم
</div>


```
covid=covid.replace({'Yes':1, 'No':0});
covid
```

![5.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/5.jpeg)
    
    
    
</div>
<div dir="rtl">
   از دستور drop_duplicates   .استفاده می کنیم  و  داده های شبیه به هم را حذف می کنیم 487 سطر بود و الان  248 سطر شد تقریبا نصف داده ها مشابه  بودند   

</div>

  
```
covid=covid.drop_duplicates(keep=False)
covid.shape
```

(248, 22)

</div>
<div dir="rtl">
  بعد از تبدیل داده ها به داده های عددی describe میزنیم تا اطلاعات بیشتری از دیتاست را بدست آوریم
  این دستور دستوری بسیار مفید برای بدست آوردن اطلاعاتی کامل از دیتاست است
  count تعدادشان 248 است و داده یnull  نداریم در هیچ کدام.
   میانگین کل، انحراف معیار ، مینیمم، 25 درصد ازداده های ما په مقداری دارند و.....را به ما می دهد 
برای مثال در
    
</div>  



```
covid.describe()  
```
  
![6.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/6.jpeg)


</div>
<div dir="rtl">
 هیستوگرام‌ها شکلی از نمایش داده هستند که داده‌ها را بر اساس توزیع عددی آن‌ها ارائه می‌دهند. 
  در واقع نوعی نمودار میله‌ایست که محور X نشان دهنده دامنه توزیع داده و محور Y نمایانگر فراوانی داده در یک بازه معین می‌باشد.
  برای ایجاد یک هیستوگرام در کتابخانه Matplotlib لازم است ابتدا داده‌های خود را در یک آرایه لیست کنیم 
از این نمودار می توان داده های کم اهمیت هم شناسایی کرد
  هیستوگرام برای داده های باینری مناسب است  برای هر ویژگی یک هیستوگرام بدست می آوریم
  مثلا  urticaria حدودا 200 نفر از بیماران کهیر نداشتند پس کهیر ویژگی مناسبی برای تشخیص کرونا نخواهد بود
  علاوه بر این از تعداد تکرارهایی که با دستور describe  مراحل  قبل بدست آوردیم هم می توان ویژگی های  کم اهمیت را تشخیص داد چون تمام لیبل ها مثبت هستند و تمام نمونه ها کوید دارند آن ویژگی ای که تعداد تکرار کمتری دارد ویژگی مناسبی برا تشخیص کرونا نخواد بود
</div>
  
  
  
  
```
  covid.hist(bins=15,figsize=(20,20))
```

![7.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/7.jpeg)
![8.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/8.jpeg)

</div>
<div dir="rtl">


