* normalize dataset <br>
 -----------------------------

نرمال  سازی به اسکیل بندی  ویژگی های عددی با ارزش واقعی در محدوده 00 تا 11 اشاره دارد.

نرمال سازی داده ها در یادگیری ماشینی استفاده می شود تا آموزش مدل نسبت به مقیاس ویژگی ها کمتر حساس باشد. این به مدل ما اجازه می دهد تا به وزن های بهتر همگرا شود و به نوبه خود منجر به مدل دقیق تری می شود.
نرمال سازی ویژگی ها را با یکدیگر سازگارتر می کند، که به مدل اجازه می دهد خروجی ها را با دقت بیشتری پیش بینی کند.
<br>
پایتون کتابخانه پیش پردازشی را فراهم می کند که حاوی تابع نرمال  سازی برای نرمال سازی داده ها است. آرایه ای را به عنوان ورودی می گیرد و مقادیر آن را بین 00 و 11 نرمال می کند. سپس آرایه خروجی را با همان ابعاد ورودی برمی گرداند.
<br>
xnormalized = (x - xminimum) / range of x
<br>
![normalize_1](https://user-images.githubusercontent.com/94124607/148960302-39f9c64a-05c1-497f-be54-2ced5ce71847.jpg)

<br>
ایتدا کتابخانه های مورد نظر را importمی کنیم و سپس فایل دیتاست را با فرمت json می خوانیم 
<br>
<div dir="rtl">
 MinMaxScalar را از روش پیش پردازش فراخوانی کردیم و یک شی (min_max_Scalar) برای آن ایجاد کردیم.  هیچ پارامتری را ارسال نکردیم زیرا باید داده  را بین 0 و 1 نرمال کنیم. اما <br>
  ابتدا تمام نام ستون ها را برای استفاده بیشتر برای نمایش نتایج می خوانیم. سپس fit_tranform را از شی ایجاد شده min_max_Scalar فراخوانی می کنیم و فایل json را به آن ارسال می کنیم.
ودر نهایت مقادیر نرمال شده بین 0 و یک را در حروجی می بینیم.
 <br>
 البته ابتا داده هارا از حالت string به حالت عددی تبدیل کردیم . و سپس دستورات را اعمال کردیم .<br>
 
 --------------------------------------
 * sorting dataset
 <div dir="rtl">
  برای مرتب سازی دیتا ست بعد از اینکه کتابخانه های مورد نظر را فراخوانی کردیم ، دیتاست مورد نظر را که در قالب json است می حوانیم  و نمایش می دهیم :<br>
  ![sort_1](https://user-images.githubusercontent.com/94124607/148960334-f4ab0edf-07d7-466a-a07d-4089292450c4.png)
  <br>
  سپس اطلاعاتی را راجع به دیتاست مورد طبق تصویر زیر به دست می آوریم : <br>
  ![sort_2](https://user-images.githubusercontent.com/94124607/148961006-ec3b869a-9ade-4efd-8f9a-4289a491f5cf.png)
بعد از آن چک می کنیم که داده ای null نباشد :<br>
  ![sort_3](https://user-images.githubusercontent.com/94124607/148961353-e45bc867-4e55-4163-acb9-b888844f9d32.png)<br>
  تابع () sort_values یک قاب داده را به ترتیب صعودی یا نزولی ستون عبوری مرتب می کند. این با تابع مرتب شده پایتون متفاوت است زیرا نمی تواند یک قاب داده را مرتب کند و ستون خاصی را نمی توان انتخاب کرد.
  <br>
  <div dir="ltr">
  Dataframe.sort_values() Single Parameter Sorting:Syntax: <br>
  DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’)
  <br>
   define parameters:<br>
   by: Single/List of column names to sort Data Frame by. <br>
axis: 0 or ‘index’ for rows and 1 or ‘columns’ for Column. <br>
ascending: Boolean value which sorts Data frame in ascending order if True. <br>
inplace: Boolean value. Makes the changes in passed data frame itself if True. <br>
kind: String which can have three inputs(‘quicksort’, ‘mergesort’ or ‘heapsort’) of algorithm used to sort data frame. <br>
na_position: Takes two string input ‘last’ or ‘first’ to set position of Null values. Default is ‘last’.<br>
  
<div dir="rtl">
 مرتب سازی را بر اساس سن انجام داده ام و مقادیرnull نیز به طور پیش فرض last می باشد .
 <br>
 ![sort_4](https://user-images.githubusercontent.com/94124607/148962665-77d7b352-ecf1-403a-a318-4d01dd18f085.png)
 <br>
 
 ------------------------------------------------
 * drop similar and itrative values:<br>
 برای این بحش از کد که در فایل drop duplicate and similar code  می باشد ، بعد از اینکه کتابخانه را فراحوانی کردیم و دیتاست را نمایش داددیم باید:
 <br>![drop_1](https://user-images.githubusercontent.com/94124607/149157632-e1f136fd-6683-490c-8687-290e76d800ab.jpg)<br>

  1. یافتن ردیف های تکراری<br>
برای یافتن موارد تکراری در یک ستون خاص، می‌توانیم به سادگی متد()duplicate را روی ستون فراخوانی کنیم.<br>
 ![drop_2](https://user-images.githubusercontent.com/94124607/149157895-c0212850-2e0c-46f9-a6ad-c4abedbdcf6d.jpg)<br>
 نتیجه یک سری بولی با مقدار True به معنای تکراری است. به عبارت دیگر، مقدار True به معنای یکسان بودن ورودی با ورودی قبلی است.
برای نگاهی به تکثیر در DataFrame به طور کلی ، فقط متد duplicated() در DataFrame را فراخوانی می کنیم . اگر یک سطر کامل با سطر قبلی یکسان باشد، True را خروجی می دهد.
<br>
 مانند تصویر فوق.<br>
 برای در نظر گرفتن ستون‌های خاصی برای شناسایی موارد تکراری، می‌توانیم فهرستی از ستون‌ها را به زیر مجموعه آرگومان ارسال کنیم: که داریم :<br>
 ![drop_3](https://user-images.githubusercontent.com/94124607/149158846-c44bd38e-9ce5-47ad-ae43-42bf1dcaa944.jpg)<br>
 2. شمارش موارد تکراری و غیر تکراری
نتیجه duplicated() یک سری بولی است و می‌توانیم آنها را جمع کنیم تا تعداد تکرارها را بشماریم. True به 1 و False به 0 تبدیل می شود، سپس آنها را جمع می کند.<br>
![Uploading drop_4.jpg…]()<br>
درست مثل قبل، می‌توانیم موارد تکراری را در یک DataFrame و روی ستون‌های خاصی بشماریم.<br>
 سپس تعداد غیر تکراری ها یعنی تعداد false هرا شمردیم و بازهم جمع زدیم .که برابر با 301  بود .<br>
 3. استخراج ردیف های تکراری با loc<br>
 Pandas duplicated() یک سری بولی را برمی گرداند.loc می تواند یک سری بولی بگیرد و داده ها را بر اساس True و False فیلتر کند. اولین آرگومان df.duplicated() ردیف هایی را که توسط duplicated() شناسایی شده اند را پیدا می کند. آرگومان دوم : تمام ستون ها را نمایش می دهد.<br>
 ![drop-5](https://user-images.githubusercontent.com/94124607/149160581-230fd984-9699-40ae-aaa3-bf1592b24c67.jpg)<br>
 4. تعیین موارد تکراری برای علامت گذاری با keep
یک آرگومان keep در Pandas duplicated() وجود دارد تا مشخص کند کدام تکرارها را علامت گذاری کنند. پیش‌فرض‌ها را روی "اول" نگه می داریم  به این معنی که اولین مورد حفظ می‌شود و بقیه موارد تکراری شناسایی می‌شوند.
می‌توانیم آن را به «آخرین» تغییر دهیم و آخرین رخداد را حفظ کنیم و بقیه را به‌عنوان تکراری علامت‌گذاری کنیم.<br>
 ![drop_6](https://user-images.githubusercontent.com/94124607/149161177-9cff4b87-899a-40ed-b9c1-4b233c681935.jpg)<br>
 ![drop_7](https://user-images.githubusercontent.com/94124607/149161375-5cedd0aa-1003-4e3d-ab83-1457f6de6684.jpg)<br>
 گزینه سومی وجود دارد که می توانیم از keep=False استفاده کنیم. همه موارد تکراری را به عنوان True علامت گذاری می کند و به ما امکان می دهد تمام ردیف های تکراری را ببینیم.<br>
 ![drop_8](https://user-images.githubusercontent.com/94124607/149161950-cfcc92cd-156e-4078-8a77-b24f63ddc131.jpg)<br>
 5. حذف ردیف های تکراری
می‌توانیم از روش  Pandas drop_duplicate() برای حذف  کردن ردیف‌های تکراری استفاده کنیم.<br>
 و درنهایت هم داده های مشابه را حذف می کنیم:<br>
 ![drop_9](https://user-images.githubusercontent.com/94124607/149162922-35fab121-7ea4-4413-b4bb-563798c484e8.jpg)<br>
 ---------------------------------------
 





 


 
 
 
 
