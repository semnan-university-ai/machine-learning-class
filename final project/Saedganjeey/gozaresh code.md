<div dir="rtl"> 
تحلیل و بررسی دیتاست کویید
<br/>
دیتا ست کویید 487 مورد ابتال به کرونا دارد و 23 ستون
</div>
<br/>
<div dir="rtl">
اولش میایم کتابخونه ی موزد نیازمونو بارگزاری میکنیم

import pandas as pd
<br/>
import numpy as np
<br/>
from sklearn.model_selection

import train_test_split
<br/>
import matplotlib.pyplot as plt
<br/>
import seaborn as sns
<br/>
<div/>
<div dir="rtl">
بعدش دیتا رو فراخونی میکنیم

covid = pd.read_excel('covid.xlsx');

covid

![saed](1.png)

<div/>
<div dir="rtl">
همانطور که مالحظه میکنیم تعداد ستون ها برابر 23 و تعداد موارد 487 است.
اما ستون # یک ستون اضافه هست و فقط اندیس را نشان میدهد که باید آن را حدف 
کنیم با دستور

covid=covid.drop(['#'], axis=1);

covid
<div/>
<div dir="rtl">
سپس با دستور زیر اطاعات کلی از جدول را بدست می آوریم


![saed1](2.png)

اطالعاتی که از این جدول و توصیف ها بدست می آید :

1.تعداد داده های ما 487 مورد است. بنابراین مقدار count همه سطر ها باید 487
باشد در حالی که در ستون headache 486 مورد است .) یک مورد missing
 value داریم(

2.بیشترین تعداد تکرار در ستون سن برابر – است که نشان دهنده این است که 359
مورد سن نداریم.

3.بقیه ست ون ها باید دو حالت بله یا خیر داشته باشند در صورتی که تعداد مقدار 
 unique آنها اکثرا 3 و 4 مقدار است.

<div/>

