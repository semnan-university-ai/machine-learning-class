<div dir="rtl">
سوال : الگوریتم c4.5 را مطالعه کنید و با ذکر یک مثال آنرا توضیح دهید.(مثال ها می تواند از جدول های تمرینات گذشته باشد.)
</div>
<br/>
<div dir="rtl">
الگوریتم C4.5 می‌تواند مقادیر گسسته یا پیوسته را در ویژگی‌ها درک کند و بر اساس آن درخت تصمیم را بسازد.
علاوه براین، این الگوریتم قادر است مقادیر ناموجود  (missing values) را نیز تحمل کند و با وجود مقادیری که ناموجود است، درخت تصمیم خود را بسازد. در حالی که الگوریتمی مانند ID3 و بسیاری دیگر از الگوریتم‌های طبقه‌بندی نمی‌توانند با مقادیر ناموجود، مدل خود را بسازند.
یکی دیگر از ویژگی های این الگوریتم قابلیت هرس کردن است.
<div/>
<br/>
<div dir="rtl">  
می خواهیم این الگوریتم را برای دسته بندی جدول زیر به کار ببریم:
<div/>
<br/>
  
![pic1](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/21/1.jpg)


<div dir="rtl">
در ابتدا آنتروپی کل را محاسبه می کنیم. 9 جواب "بله" و 5 جواب "خیر" داریم:

Entropy:-9/14 x log9/14 – 5/14 x log 5/14 = 0.94
  
حال باید تصمیم بگیریم کدام ویژگی در ریشه درخت قرار می گیرد. برای این کار، از فرمول های زیر استفاده میکنیم:
<div/>

![oic3](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/21/3.jpg)  

<br/>
<div dir="rtl">
برای ویژگی اول داریم:
<div/>  
<div dir="rtl">
Outlook:

Sunny: (-2/5 x log2/5 – 3/5 x log 3/5)=(-0.4 *(-1.3219)-0.6*((-0.7369))= (0.5281 + 0.4421)= 0.9702

Overcast: (-4/4 x log 4/4 – 0)=(-1 x log 1 – 0)=0

Rainy=(-3/5 x log 3/5 – 2/5 x log 2/5) = (-0.6 * (-0.7369)+0.4*(-1.3219))=0.9702

Splitinfo=-5/14 x log 5/14 – 4/14 x log 4/14 -5/14  x log 5/14 = 1.577

Gain (x)= 0.94 – 5/14 x 0.9702 – 4/14 *0 – 5/14*0.9702=0.94-0.693=0.247
Gain ratio=0.247/1.577=0.157      node
<div/>  
<br/>
<div dir="rtl">
Humidity:

High: (-3/7 x log 3/7 – 4/7 x loh 4/7)=0.985

Normal: (-6/7 x log 6/7 – 1/7 x log 1/7)=0.592

Info gain=0.94- 7/14 *0.985 – 7/14 *log 7/14=0.151

Split info=-7/14 x log 7/14 – 7/14 x log 7/14 = 1

Gan ratio= 0.151/1=0.151
<div/>  
<br/>
<div dir="rtl">
Tempreture:
  
Hot: (-2/4 x log 2/4 – 2/4 x log 2/4)=1

Mild: (-4/6 x log 4/6 – 2/6 x log 2/6)=0.9182

Cool: (-3/4 x log 3/4 – 1/4 x log 1/4)=0.8112

Info gain= 0.94 – 4/14 *1 – 6/14*0.9182 – 4/14 *0.8112= 0.292

Split info= -4/14 x log 4/14 – 6/14 x log 6/14 – 4/14 x log 4/14 = 1.556

Gain ratio= 0.292/1.556= 0.1876 
<div/>
<br/>

<div dir="rtl">
Wind:

Strong:(-3/6 x log 3/6 – 3/6 x log 3/6)=1

Weak: (-6/8 x log 6/8 – 2/8 x log 2/8)= 0.8112

Info gain=0.94 – 6/14 * 1 – 8/14 *0.8112 = 0.048

Split info = -6/14 x log 6/14 – 8/14 x log 8/14 = 0.9852

Gain ratio= 0.48/0.9852 = 0.049
<div/>
<div dir="rtl">
در مرحله بعد، مسیر هایی که از outlook می گذرند را برای ویژگی های دیگر بررسی می کنیم. ابتدا به سراغ sunny  می رویم:  
<div/>
<br/>  
<div dir="rtl">
Entrpopy= -2/5 x log 2/5 – 3/5 x log 3/5 = 0.97
<div/>  
<br/>
<div dir="rtl">
Humidity:

High: -0/3 x log 0/3 – 3/3 x log 3/3 = 0

Normal: -2/2 x log 2/2 – 0/2 x log0/2= 0

Info gain= 0.97 – 3/5 *0 – 2/5 *0= 0.971

Split info= - 1/5 x log 3/5 – 2/5 x log 2/5 = 0.971

Gain ratio= 0.971/0.971= 1 انتخاب می شود
<div/>  

<br/>
<div dir="rtl">
Tempreture:

Hot: -0/2 x log0/2 – 2/2 x log2/2= 0

Miid: - 1/2 x log1/2 – 1/2 x log 1/2= 1

Cool: -1/1 x log 1/1 – 0/1 x log0/1= 0

Info gain= 0.97 – 2/5*0 – 2/5*1 – 1/5*0 = 0.57

Split info= -2/5 x log 2/5 – 2/5 x log 2/5 – 1/5 x log 1/5= 1.522

Gain ratio= 0.57/1.522= 0.375
<div/>  
