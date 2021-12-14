

<div dir="rtl">
  
  ### 22) مفاهیم زیر را به صورت خلاصه بررسی کنید.
  <br/>
  
  ### Ovefitting
  ### Local minimum
  ### Gradient descent
  ### Eager and lazy learning
  <br/><br/>
  
  ##### Ovefitting:
  
  فرضیه ای که روی مثال های آموزشی خیلی خوب عمل می کند اما در مثال های آزمایشی (داده های واقعی ) دقت اش کم تر است. در واقع به مثال های آموزشی خیلی خیلی بها می دهیم.
  <div/>
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
   دو نوع خطای فرضیه داریم خطای آموزش که خطا روی داده های آموزش (error train) است و خطای اصلی که خطا در کل توزیع (error D) است 
    <br/>  
  error D خطا در کل توزیع (خطای اصلی) برای ما مهم تر از error train است.
  <br/>
      
   ![22-1.jpg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(22)/22-1.jpg)
      
   ![22-2.jpg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(22)/22-2.jpg) 
    
   <br/>
      در شکل زیر میبینیم از یک جایی به بعد خطای ترین زیاد شده است که همان جا باید trian شبکه متوقف گردد. 
      
 ![22-3.jpg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(22)/22-3.jpg)
      
  
      
      
  

