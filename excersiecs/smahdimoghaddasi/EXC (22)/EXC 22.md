

<div dir="rtl">
  
  ### 22) مفاهیم زیر را به صورت خلاصه بررسی کنید.
  <br/>
  
  ### Ovefitting
  ### Local minimum
  ### Gradient descent
  ### Eager and lazy learning
  <br/><br/>
  
  ##### Ovefitting:
  <br/>
  
  در شکل 1 خط (فرضیه) روی مثال های آموزشی نسبتا خوب جواب می دهد و
  در شکل 2 فرضیه روی تمامی نمونه های آموزشی فیت شده است، و اگر نمونه ی تستی وارد شود فرضیه ی 1  نسبت به 2 بهتر عمل می کند، چون منطق بهتری دارد و به عبارتی داده های 
   آموزشي را حفظ نکره است. 
   <br/>
  فرضیه ای که روی مثال های آموزشی خیلی خوب عمل می کند، اما در مثال های آزمایشی (داده های واقعی ) دقت اش کم تر است، 
  در اين حالت، فرضیه روی مثال های آموزشی overfit شده است
  و به مثال های آموزشی خیلی خیلی بها داده ايم.
 
  <br/>
  
  ### شکل 1
  
  ![22-1.jpg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(22)/22-1.jpg)
       
  ### شکل 2
  
   ![22-2.jpg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(22)/22-2.jpg) 
    
   <br/>
  
   <div dir="rtl">
   دو نوع خطای فرضیه داریم خطای آموزش که خطا روی داده های آموزش (error train) است و خطای اصلی که خطا در کل توزیع (error D) است 
    <br/>  
  error D خطا در کل توزیع (خطای اصلی) برای ما مهم تر از error train است.
  <br/>
  
  
  error train (h) < error train (h`)  <br/>
  
  error D (h) > error D (h`)
  <br/>
  <br/>
  <div dir="rtl">
   در آموزش h بهتر عمل کرده است اما `h بهتر است. 
   <div/>
  
   D= کل توزیع(همه ی نمونه ها)
   <br/>
     <div dir="rtl"> 
   
 در شکل زیر میبینیم از یک جایی به بعد خطا زیاد شده است که همان جا باید trian شبکه متوقف گردد.
  <br/>
      
 ![22-3.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(22)/22-3.png)
      
  
      
      
  

