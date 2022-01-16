 
 <div dir="rtl">
  
  با توجه به دیتاست covid که در پوشه ی data موجود است عملیات زیر را روی این دیتاست انجام دهید:
  - نرمالیزه کردن
  - مرتب سازی داده
  - حذف داده های یکسان و تکراری
  - بدست آوردن 5 ویژگی که کمترین اهمیت را دارند
  -  اجرای الگوریتم های find-s و ce و بیز و knn و کلاسترینگ و درخت تصمیم یکبار به صورت تصادفی و یک بار با الگوریتم id3
  - داده های زیر همگی به عنوان true برچسب گذاری خواهند شد و ترکیبات داده ای دیگر به عنوان false تمام ترکیبات داده ای که قابل کشف می باشد را بدست آورید.
  - الگوریتم های اجرا شده را با rapidminer نیز اجرا کنید و نتیجه ی خود را با آن مقایسه کنید
  - دیتاست در سایت kaggle ثبت شده است در صورتی که کد خود را در بخش notebook های kaggle ثبت کنید نمره ی اضافه دریافت خواهید کرد.
  
  
<br />
  لینک kaggle
  : 
  <br />
  </div>
  https://www.kaggle.com/amirshnll/covid-patient-datasets
<div dir="rtl">

حل:<br />
### لازم به ذکر است کدهای مربوطه در kaggle نیز ثبت شده است 
ابتدا باید کتابخانه های لازم را فراخوانی کنیم:
<br />
  کتابخانه pandas :
    این کتابخانه می‌تواند داده‌ها را با بهره‌گیری از ساختارهای Series و DataFrame که ارائه می‌کند، به قالبی که برای تحلیل داده‌ها مناسب هستند، مبدل سازد.
    بسته پانداس حاوی چندین متد برای پالایش مناسب داده‌ها است.
    پانداس دارای ابزارهای گوناگونی برای انجام عملیات ورودی/خروجی است و می‌تواند داده‌ها را از فرمت‌های گوناگونی شامل MS Excel ،TSV ،CSV و دیگر موارد بخواند.

کتابخانه numpy:
با استفاده از این کتابخانه امکان استفاده از آرایه‌ها و ماتریس‌های بزرگ چند بعدی فراهم می‌شود. هم‌چنین می‌توان از تابع‌های ریاضیاتی سطح بالا بر روی این آرایه‌ها استفاده کرد

از کتابخانه یsklearn model_selection ما train_test_split را فراخوانی کردیم برای تقسیم بندی داده ها به train و test
  
کتابخانه ی matplotlib.pyplot  و seaborn برای رسم نمودار ها فراخوانی شد.    
  
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
   از دستور drop_duplicates   .استفاده می کنیم  و  داده های شبیه به هم را حذف می کنیم 487 سطر بود و الان  205 سطر شد تقریبا نصف داده ها مشابه  بودند   

</div>

  
```
covid=covid.drop_duplicates(keep=False)
covid.shape
```

(205, 21)

</div>
<div dir="rtl">
  بعد از تبدیل داده ها به داده های عددی describe میزنیم تا اطلاعات بیشتری از دیتاست را بدست آوریم
  این دستور دستوری بسیار مفید برای بدست آوردن اطلاعاتی کامل از دیتاست است
  count تعدادشان 205 است و داده یnull  نداریم در هیچ کدام.
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

![77.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/77.png)


</div>
<div dir="rtl">

برای فیچر سلکشن راه حل مناسب دیگر رسم نمودار کرولیشن بین ویژگی هاست که دستور cor = covid.corr() را از کتابخانه ی seaborn استفاده می کنیم 
این نمودار ارتباط بین ستون ها را بایکدیگر نشان می دهد و می بینیم کرولیشن هر ویژگی با خودش یک است و بقیه اعدادی بین 1 و-1 هستند. عدد نزدیک به صفر  ( چه منفی و چه مثبت)  نشان دهنده ی این است که ارزش آن متغبر کم است  و هرچه به مثبت یک نزدیک تر باشد یعنی یعنی رابطه یمستقیم بیشتر و هرچه به منفی یک نزدیک تر یعنی رابطه ی عکس بیشتر  یه متغیر کم شود، متغیر دیگر زیاد می شود. پس با این نمودار می توان تاثیر ویژگی ها بر یکدیگر را بدست آورد
 در جدول کرولیشن lose of taste با lose of small هم رابطه است یعنی اگر بیماری یکی از این ها را داشته باشد دومی هم دارد.
</div>
 
 
 
 ```
 plt.figure(figsize=(20,20))
cor = covid.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()
```

![9.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/9.png)

</div>
<div dir="rtl">
 
 قبل از اینکه داده ها را به هر الگوریتمی بدهیم یک قدم اصلی و مهم دستیابی به ویژگی های با اهمیت بیشتر و فیچر سلکشن است که من از نمودار هیستوگرام و  کرولیشن بین ویژگی ها و همینطور میانگین استفاده کرده و ویژگی های کم اهمیت را حذف می کنم
</div>
 
 ```
 covid =covid.drop(['urticaria','Vomit','Body_discoloration' ,'Abdominal_pain','Sneezing'],axis=1)
covid
```

![10.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/10.jpeg)


</div>
<div dir="rtl">
در این مرحله می خواهیم نمونه ی منفی تولید کنیم در اینجا حالت هایی که در دیتاست وجود ندارند را اگر تولید کنیم  یعنی 2 به توان 21 حدود 2 میلیون دیتا میشود و حتی   
 تعداد کل حالت هایی که با  16 ستون می توان ایجاد کرد برابر 65536
است.
 و اگر دادهای مثبت را از این تعداد کم کنیم  باز هم حدود 65 هزار داده ی منفی  خواهیم داشت و این ها موجب عدم بالانس در دیتاست نهایی ما می شود
 من ستون های جدول را در یک حلقه ی for  قرار دادم و مقادیرش را صفر و یک گذاشتم
 </div>

 
```
columns={}
for col in covid.columns:
    columns[col]=[1,0];
columns
```

 
 {'Ague': [1, 0],<br />
 'Chest_pain': [1, 0],<br />
 'Cough': [1, 0],<br />
 'Decreased_appetite': [1, 0],<br />
 'Diarrhea': [1, 0],<br />
 'Fatigue': [1, 0],<br />
 'Fever': [1, 0],<br />
 'Headache': [1, 0],<br />
 'Loss_of_smell': [1, 0],<br />
 'Loss_of_taste': [1, 0],<br />
 'Nausea': [1, 0],<br />
 'Shortness_of_breath': [1, 0],<br />
 'Sleep_problems': [1, 0],<br />
 'Sore_throat': [1, 0],<br />
 'body_pain': [1, 0],<br />
 'runny_nose': [1, 0]}<br />
 
 
 
 
</div>
<div dir="rtl">
 در این دیکشنری تمام احتمالاتی را که برای این جدول می شود درست کرد را بدست آوردم
 65536 تعداد حالت هایی است که در دیتاست وجود ندارد 
 و در برابر دیتاست اصلی خیلی عدد بزرگی است 
 </div>
 
 ```
 from itertools import product
All_V=pd.DataFrame([row for row in product(*columns.values())],columns=columns.keys())

All_V
 ```
 
![11.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/11.jpeg)



</div>
<div dir="rtl">
 در این مرحله دیتاست اصلی و دیتای تولید شده را با هم یکی می کنیم که یک سری از دیتاها تکراری بوده اند و باید حذف شوند  پس از دستور drop_duplicates استفاده می کنیم و تعداد 65338 خواهد شد  پس این تعداد کوید ندارند  
</div>
 
 

```
df4 = pd.concat([covid,All_V])
no_covid=df4.drop_duplicates(keep=False)
no_covid
```

![12.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/12.jpeg)



</div>
<div dir="rtl">
اگر از این دیتاست استفاده کنیم دقت مناسبی به دست نخواهیم آورد و اصلا کوید مثبت هارا به خوبی نمی تواند تشخیص دهد و بایاس به سمت کوید منفی پیدا می کند 
 باید داده های فیک و بهینه بسازیم 
در اینجا اگر نمونه ای داشته باشیم که تمام ویژگی هایش مثبت باشد  را (چون در دیتاست اولیه ی کویدمثبت ها نبود)را به نوان نمونه ی کوید منفی تشخیص می دهد و این به شدت دقت  را خراب خواهد کرد.
  بنابراین شرط هایی را در نظر گرفتیم  در دیتاست کوید منفی  تعداد یک ها کمتر از 8 یعنی داده های کوید منفی حداکثر8 ویژگی را داشته باشند و از 8 بیشتر نداشته باشند  چون از 8 بیشتر احتمال اینکه  کرونا داشته و در جدول نبوده وجود دارد  

 برای اینکه حجم دیتاست کمتر شود یک شرط دیگر را همزمان با این شرط اعمال می کنیم (می توان این شرط هم لحاظ نکرد)
 اینکه حداقل سه تا از این علائم را داشته باشد تا به عنوان بیماری کوید مثبت شناسایی شود.
 پس به اینصورت نوشتیم ولی باز هم به نسبت دیتای کوید مثبت، تعدداد کوید منفی زیاد است  
</div>
 
 
 
```
no_covid=no_covid[(no_covid.sum(axis=1)<8)  & (no_covid.sum(axis=1)>3)];
no_covid
```
 
 
![13.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/13.jpeg)
 
 
</div>
<div dir="rtl">
 پس در این مرحله سمپل گیری انجام دادم به صورت رندوم و به تعدادی که می خواهیم  می توان سمپل گیری انجام داد
  250 تاست که 250 گرفتم که یعنی تعداد داده هایی که ساختیم و کوید منفی است
</div> 



```
no_covid=no_covid.sample(n=250)
no_covid
```


![14.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/14.jpeg)



</div>
<div dir="rtl">
حال باید دیتاها را لیبل گذاری کنیم
 کلاس صفر کوید منفی و کلاس یک کوید مثبت و یک سطر لیبل به داده ها اضافه می شود
</div>
 
 
 
 
```
no_covid['class']=0;
covid['class']=1;
no_covid
```



![15.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/15.jpeg)

</div>
<div dir="rtl">
 داده هایمان را که لیبل زدیم با هم concat می کنیم 
 و آن را به عنوان یک دیتاست نهایی داریم 
</div>
 
 
 
 ```
 dataset =pd.concat([no_covid,covid],ignore_index=True)
dataset
 ```
 
 
 ![16.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/16.jpeg)
 
 
</div>
<div dir="rtl">
 کل داده ها را می گیریم به جز ستون آخر و لیبل هار ا می گیریم یعنی همان ستون آخر
 </div>
 

 
 
```
X=dataset.iloc[:,:-1]
y =dataset.iloc[:,-1]
y
```



</div>
<div dir="rtl">
 داده هایمان را تقسیم بندی  می کنیم  به ترین و تست 
و test_size = 0.30 می گیریم و 70 درصد برای ترین استفاده می شود 
</div>
 
 
 ```
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 4)
 ```
 
</div>
<div dir="rtl">
 در بعضی از کلاسیفایر ها داده ها باید اسمی باشند و با داده ی عددی امکان پذیر نیست پس replace می کنیم به yes و no 
 </div>
 
 
```
dataset_nominal=dataset.replace({1:'Yes', 0:'No'});
dataset_nominal
```



</div>
<div dir="rtl">
 اجرای Find-S  
<br />
 لیبل و دیتا را جدا کردم
</div>
 
 
 
 
 ```
 h = ['0', '0', '0', '0', '0', '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0','0','0','0']

for index, row in dataset.iterrows():
    if row[-1] == 'Yes':
        j = 0
        
        for col in row:
            if col != 'Yes':
                if col != h[j] and h[j] == '0':
                    h[j] = col
                elif col != h[j] and h[j] != '0':
                    h[j] = '?'
                    
            j = j + 1
 
    
print('Maximally Specific Hypothesis: ', h)

```

Maximally Specific Hypothesis:  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

</div>
<div dir="rtl">
 اجرای CE:
<br />
ابتدا لیبل و دیتا را جدا کردم   
</div>





```
import numpy as np
import pandas as pd

def learn(concepts, target):
    
    specific_h = concepts[0].copy()
    
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    
    # The learning iterations
    for i, h in enumerate(concepts):
        
        # Checking if the hypothesis has a positive target
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                
                # Change values in S & G only if values change
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
                    
        # Checking if the hypothesis has a positive target
        if target[i] == "No":
            for x in range(len(specific_h)):
                
                # For negative hyposthesis change values only  in G
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
    
    # find indices where we have empty rows, meaning those that are unchanged
    indices = [i for i,val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        # remove those rows from general_h
        general_h.remove(['?', '?', '?', '?', '?', '?'])
        
    # Return final values
    return specific_h, general_h
sample=dataset.sample(n=30);
concepts =np.array(sample.iloc[:,:-1]);
target=np.array(sample.iloc[:,-1]);
s_final, g_final = learn(concepts, target)
print("Final S:", s_final, sep="\n")
print("Final G:", g_final, sep="\n")
```

</div>
<div dir="rtl">
 Naive Bayes:<br />
 دقت:0.7299270072992701
</div>


```
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
y_pred
gnb.score(X_test, y_test)
```


</div>
<div dir="rtl">
 KNN
</div>



```
from sklearn.neighbors import KNeighborsClassifier
error_rate = []
for i in range(1,50):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))
plt.figure(figsize=(15,8))
plt.plot(range(1,50),error_rate,color='green', linestyle='dashed', marker='o',
 markerfacecolor='red', markersize=12)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
```

![17.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/17.png)



</div>
<div dir="rtl">
5NN :<br />
 دقت:0.7372262773722628
</div>


```
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(X_train, y_train)

y_pred=neigh.predict(X_test)
y_pred
neigh.score(X_test, y_test)
```


</div>
<div dir="rtl">
Decision Tree - ID3<br />
 دقت:0.7757009345794392
</div>


```
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=0,criterion='entropy')
clf.fit(X_train, y_train)

y_pred=clf.predict(X_test)
y_pred
clf.score(X_test, y_test)
```


</div>
<div dir="rtl">
Decision Tree - random<br />
 دقت:0.7850467289719626
</div>



```
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=0,splitter='random')
clf.fit(X_train, y_train)

y_pred=clf.predict(X_test)
y_pred
clf.score(X_test, y_test)
```


</div>
<div dir="rtl">
 برای پیدا کردن مقدار k مناسب نمودار elbow را رسم می کنیم تا k مناسب را بدست آوریم 
می بینیم در k=2 شیب نمودار مقداری  تغییر کرده  پس k lkhsf 2 می باشد 
 Kmeans:<br />
 0.5098591549295775 :دقت 
</div>

```
from sklearn.cluster import KMeans

wcss = []
for i in range(1, 16):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
#Plotting the results onto a line graph, allowing us to observe 'The elbow'
plt.plot(range(1, 16), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') #within cluster sum of squares
plt.show()
```





![18.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/smahdimoghaddasi/18.png)




```
from sklearn.metrics import accuracy_score
kmeans = KMeans(n_clusters=2, random_state=1).fit(X)
kmeans.labels_
print(accuracy_score(y,kmeans.labels_))
```


</div>
<div dir="rtl">
در نهایت چندین مدل دیگر را بر روی این دیتاست اعمال می کنیم و می بینیم mlp  و svm با کرنل RBF هم دارای دقتی نزدیک به mlp است دارای بالاترین دقت خواهد بود  
</div>


```
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
models = []
models.append(("Logistic Regression:",LogisticRegression()))
models.append(("Naive Bayes:",GaussianNB()))
models.append(("K-Nearest Neighbour:",KNeighborsClassifier(n_neighbors=3)))
models.append(("Decision Tree:",DecisionTreeClassifier()))
models.append(("Support Vector Machine-linear:",SVC(kernel="linear")))
models.append(("Support Vector Machine-rbf:",SVC(kernel="rbf")))
models.append(("Random Forest:",RandomForestClassifier(n_estimators=7)))
models.append(("MLP:",MLPClassifier(hidden_layer_sizes=(45,30,15),solver='sgd',learning_rate_init=0.01,max_iter=500)))
models.append(("AdaBoostClassifier:",AdaBoostClassifier()))
models.append(("GradientBoostingClassifier:",GradientBoostingClassifier()))
print('Models appended...')
results = []
names = []
for name,model in models:
    kfold = KFold(n_splits=10,shuffle=True, random_state=0)
    cv_result = cross_val_score(model,X_train,y_train, cv = kfold,scoring = "accuracy")
    names.append(name)
    results.append(cv_result)
for i in range(len(names)):
    print(names[i],results[i].mean()*100)
```



Models appended...<br />
Logistic Regression: 68.91129032258065<br />
Naive Bayes: 71.40120967741936<br />
K-Nearest Neighbour: 78.93145161290323<br />
Decision Tree: 81.76411290322581<br />
Support Vector Machine-linear: 72.01612903225806<br />
Support Vector Machine-rbf: 84.8991935483871<br />
Random Forest: 81.76411290322581<br />
MLP: 84.91935483870968<br />
AdaBoostClassifier: 68.28629032258064<br />
GradientBoostingClassifier: 84.5866935483871<br />




</div>
<div dir="rtl">
در نهایت دیتاست نهایی را ذخیره می کنیم که از آن در rapidminer استفاده کنیم.  
</div

```
dataset.to_excel("covid-out.xlsx",index=False)
```
