<div dir="rtl">
سوال : با کمک توابع رندوم در یک زبان برنامه نویسی روی یک صفحه ی مختصات دوبعدی 100 نقطه با x و yهای رندوم در بازه ی 1 تا 50 بدست آورید و برنامه ای بنویسید که k=3 را نسبت به 43 یا چهل و سومین نقطه ی تولید شده ی شما دارد.
</div>
<br/> 
<div dir="rtl">
با استفاده از زبان برنامه نویسی پایتون انجام دادم. کار با این برنامه را دوستان آموزش دادند


 تولید اعداد رندوم با استفاده از پکیج نامپای


np as numpy import. 1


2. from numpy import randomاستفاده از توابع رندوم  ه



 استفاده از تابع زیر برای حساب کردن فاصله اعداد 


(m,n(func_dis def. 3
 


4. z=np.sqt(np.power((m[0]-n[0],2)+np.power((m[1]-n[1],2))


5. return rand(z,3) )  فاصله را مشخص کردم


6. n=dict()


7. z=dict()


8. m=random.randint(1,50),size=(100,2))) روبرو سایز با 50تا1 بین اعداد)


9. for i in range(100)فاصله بین دو نقطه


10.n[i]=dis_func(m[i],m[43])


11.y=sorted(n.items(),reverse=false,key=lambda x:x[1]) مرتب سازی 


12.print(“ k=3 from 43th point is %s and its distance is equal to %s 
and it was %snd random number “ % 
(m[y[3][0],y[3][1],y[3][0])
</div>
<br/> 