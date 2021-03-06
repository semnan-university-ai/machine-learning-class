<div dir="rtl">
سوال : الگوریتم c4.5 را مطالعه کنید و با ذکر یک مثال آنرا توضیح دهید.(مثال ها می تواند از جدول های تمرینات گذشته باشد.)
</div>
<br/>
<div dir="rtl">
آقای )راس کوینلند (پیشنهاد دهنده‌ی الگوریتمِ (ID3(، بعد از اینکه به نقاط ضعفِ این الگوریتم پی‌برد، در مدتِ کوتاهی الگوریتمِ بعدی خود یعنی C4.5 را طراحی کرد. از نقاطِ ضعف الگوریتم ID3 که در C4.5 رفع شده است می‌توان به موارد زیر اشاره کرد:
<div/>
<br/>
<div dir="rtl">  
۱  . الگوریتم C4.5 می‌تواند مقادیر گسسته یا پیوسته را در ویژگی‌ها درک کند. در درسِ آشنایی با الگوریتم ID3 این نکته را گفتیم که الگوریتمِ ID3 اولیه نمی‌تواند تفاوتِ مقادیرِ عددیِ پیوسته را درک کند. برای مثال نمی‌تواند تفاوت بین معدل‌ها را درک کند. ولی الگوریتمِ C4.5 می‌تواند این کار را انجام دهد و مقادیرِ پیوسته را هم درک کرده و بر اساس آن درخت تصمیم را بسازد. مثلاً همان درخت مثالِ درسِ ID3 را مشاهده کنید:

![pic1](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Saedganjeey/21/1.png)
<br/>

الگوریتمِ ID3 نمی‌تواند یک همچین درختی را با مقادیر پیوسته بسازد زیرا ساختِ این درخت نیازمندِ این است که الگوریتم بتواند تعدادِ مقالات و معدلِ کل را به صورت پیوسته و عددی همراه با یک حدِ آستانه‌ی مشخص (۲ برای تعداد مقالات و ۱۶ برای معدل) پیدا کند و بر اساس آن شاخه‌های زیر درخت‌های چپ و راست را بسازد. ولی این کار توسطِ الگوریتم C4.5 قابل انجام است. منظور از مقادیر پیوسته مثلاً اعدادی است که پشت سرِ هم می‌آیند و منظور از مقادیر گسسته مثلاً مرد یا زن بودن است
<div/>
<div dir="rtl">  
۲. الگوریتمِ C4.5 قادر است تا مقادیری که موجود نیستند را هم تحمل کند. برای مثال تصویر زیر را که مانند جدول درس ID3 بود نگاه کنید:

![pic2](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Saedganjeey/21/2.png)
<br/>
در تصویر بالا مشاهده می‌کنید که تعدادی از داده‌ها وجود ندارند. به این داده‌ها، مقادیرِ ناموجود (missing  (valuesنیز می‌گویند. مثلاً فرد شماره‌ی ۱، تعدادِ مقالات نامعلومی دارد، یعنی در این مجموعه داده نتوانسته‌ایم تعدادِ مقالاتِ فرد ۱ را به دست بیاوریم. الگوریتم C4.5 می‌تواند این مقادیر را تحمل کند و با وجود مقادیری که ناموجود است، درخت تصمیم خود را بسازد. در حالی که الگوریتمی مانند ID3 و بسیاری دیگر از الگوریتم‌های طبقه‌بندی نمی‌توانند با مقادیر ناموجود، مدلِ خود را بسازند.
<div/>
<br/>
<div dir="rtl">  
۳. سومین موردی که باعث بهینه شدن الگوریتم C4.5 نسبت به ID3 می‌شود، عملیاتِ هرس کردن (prunning) جهت جلوگیری از overfitting است. الگوریتم‌هایی مانند ID3 به خاطر اینکه سعی دارند تا حد امکان شاخه و برگ داشته باشند (تا به نتیجه مورد نظر برسند) با احتمال بالاتری دارای پیچیدگی در ساخت مدل می‌شوند (بحث bias و variance را مطالعه داشته باشید) و این پیچیدگی در بسیاری از موارد الگوریتم را دچار overfitting و خطای بالا می‌کند. اما با عملیات هرس کردن درخت که در الگوریتم C4.5 انجام می‌شود، می‌توان مدل را به یک نقطه بهینه رساند که زیاد پیچیده نباشد (و البته زیاد هم ساده نباشد) و overfitting یا  underfitting رخ ندهد.
<div/>
<br/>
<div dir="rtl">  
۴. مورد چهارم که می‌تواند الگوریتم C4.5 را از بسیاری دیگر از الگوریتم‌ها متمایز کند بحثِ وزن‌دهی (weighting) به ویژگی‌ها است. اجازه بدهید به مثال اشاره شده در درس الگوریتم ID3 برگردیم. شما می‌خواهید یک طبقه‌بند بسازید تا از روی مدلِ ساخته شده پیش‌بینی کند که آیا یک شخص می‌تواند در مقطع دکتری قبول شود یا خیر؟ مانند تصویر:

![pic3](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Saedganjeey/21/3.png)
<br/>
حال فرض کنید، شما به عنون رئیسِ دانشکده (با توجه به تجربه‌ی بالای خود) می‌خواهید وزنِ ویژگیِ تعداد مقالات را بیشتر کنید. یعنی به این نتیجه رسیده‌اید که این ویژگی می‌تواند اثر بیشتری در انتخاب یک شخص در مقطع دکتری داشته باشد. الگوریتم C4.5 این قابلیت را دارد که وزن‌های مختلف و غیر یکسانی را به برخی از ویژگی‌ها بدهد
<div/>
