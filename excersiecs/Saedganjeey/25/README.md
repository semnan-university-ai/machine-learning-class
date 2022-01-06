<div dir="rtl">
سوال : با کمک توابع رندوم در یک زبان برنامه نویسی روی یک صفحه ی مختصات دوبعدی 100 نقطه با x و yهای رندوم در بازه ی 1 تا 50 بدست آورید و برنامه ای بنویسید که k=3 را نسبت به 43 یا چهل و سومین نقطه ی تولید شده ی شما دارد.
</div>
<br/> 
<div dir="rtl">
با استفاده از زبان برنامه نویسی پایتون انجام دادم


 تولید اعداد رندوم با استفاده از پکیج نامپای


1. import numpy as p


استفاده از توابع رندوم  


2. from numpy import random




 استفاده از تابع زیر برای حساب کردن فاصله اعداد 


3. dev dis_func(n,m)


4. z=np.sqt(np.power((m[0]-n[0],2)+np.power((m[1]-n[1],2))

فاصله را مشخص کردم


5. return rand(z,3) )


6. n=dict()


7. z=dict()

اعدا بین 1تا 50 با سایز زیر


8. m=random.randint(1,50),size=(100,2))) 


فاصله بین دو نقطه


9. for i in range(100)


10.n[i]=dis_func(m[i],m[43])

مزتب سازی 


11.y=sorted(n.items(),reverse=false,key=lambda x:x[1]) 


12.print(“ k=3 from 43th point is %s and its distance is equal to %s 
and it was %snd random number “ % 
(m[y[3][0],y[3][1],y[3][0])
</div>
<br/> 