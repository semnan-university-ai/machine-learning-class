## یکی از نرم افزارهایی که بر پایه الگوریتم بیز کار می کند
الگوریتم بیز در مایکروسافت
<div dir="rtl">
          به عنوان یک استراتژی تبلیغاتی، بخش بازاریابی برای شرکت Adventure Works Cycle تصمیم گرفته است که مشتریان بالقوه را از طریق ارسال آگهی های پستی هدف قرار دهد. برای کاهش هزینه ها، آنها می خواهند فقط برای آن دسته از مشتریانی که احتمالاً به آنها پاسخ می دهند، بروشور ارسال کنند. این شرکت اطلاعات مربوط به اطلاعات جمعیتی و پاسخ به یک پست قبلی را در یک پایگاه داده ذخیره می کند. آنها می خواهند از این داده ها استفاده کنند تا ببینند چگونه اطلاعات جمعیتی مانند سن و مکان می تواند به پیش بینی پاسخ به یک تبلیغ کمک کند، با مقایسه مشتریان بالقوه با مشتریانی که ویژگی های مشابهی دارند و در گذشته از شرکت خرید کرده اند. به طور خاص، آنها می خواهند تفاوت بین آن دسته از مشتریانی که دوچرخه خریداری کرده اند و مشتریانی که دوچرخه خریداری نکرده اند، ببینند.

با استفاده از الگوریتم Naive Bayes، بخش بازاریابی می تواند به سرعت یک نتیجه را برای یک پروفایل مشتری خاص پیش بینی کند، و بنابراین می تواند تعیین کند که کدام مشتریان به احتمال زیاد به آگهی ها پاسخ خواهند داد. با استفاده از Microsoft Naive Bayes Viewer در SQL Server Data Tools، آنها همچنین می توانند به طور بصری بررسی کنند که کدام ستون های ورودی به پاسخ های مثبت به آگهی ها کمک می کنند.
الگوریتم مایکروسافت Naive Bayes احتمال هر حالت هر ستون ورودی را با توجه به هر حالت ممکن از ستون قابل پیش بینی محاسبه می کند.
برای درک نحوه کار، از Microsoft Naive Bayes Viewer در SQL Server Data Tools همانطور که در نمودار زیر نشان داده شده است استفاده کنید تا به صورت بصری نحوه توزیع حالت ها توسط الگوریتم را بررسی کنید.
در اینجا، Microsoft Naive Bayes Viewer هر ستون ورودی را در مجموعه داده فهرست می کند و نحوه توزیع حالت‌های هر ستون را با توجه به هر وضعیت ستون قابل پیش‌بینی نشان می‌دهد.
شما می توانید از این نمای مدل برای شناسایی ستون های ورودی که برای تمایز بین حالت های ستون قابل پیش بینی مهم هستند استفاده کنید.
به عنوان مثال، در ردیف فاصله رفت و آمد نشان داده شده در اینجا، توزیع مقادیر ورودی برای خریداران در مقایسه با غیرخریداران به طور مشهودی متفاوت است. چیزی که این به شما می گوید این است که ورودی، مسافت رفت و آمد = 0-1 مایل، یک پیش بینی بالقوه است.
بیننده همچنین مقادیری را برای توزیع ها ارائه می دهد، بنابراین می توانید ببینید که برای مشتریانی که از یک تا دو مایل به محل کار خود رفت و آمد می کنند، احتمال خرید دوچرخه از آنها 0.387 و احتمال عدم خرید دوچرخه 0.287 است. در این مثال، الگوریتم از اطلاعات عددی مشتق شده از ویژگی‌های مشتری (مانند مسافت رفت‌وآمد) برای پیش بینی اینکه آیا مشتری دوچرخه می  خرد استفاده می کند.
  </div>

![bayes](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/b-mohammadpour/19/1.jpg)



  <br/>
