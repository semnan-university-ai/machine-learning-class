### مفهوم Voronoi diagram را به طور خلاصه بیان کنید.

<div dir="rtl" align="justify" >
 در مسائل پیدا کردن نزدیک ترین همسایه (یافتن k)معمولا از مفاهیم فاصله اقلدیسی استفاده میشود و این مسائل کاربرد زیادی در مسائل دنیای واقعی همچون تشخیص الگو ، یادگیری ماشین و ... دارد از جمله روش های حل این مسائل نمودار ورونی میباشد 
<br/>
Voronoi Diagram یک ابزار محاسباتی پایه در محاسبات هندسی می باشد، که در کاربرد هایی مانند برنامه ریزی حرکت، یادگیری، بازیابی سطوح و خوشه بندی به کار می رود
همچنین نمودار ورونی سرعت را در مسائل NN 1 زیاد میکند

  <br/>
  <br/>
  در نظر بگیرید p مجموعه ای از n نقطه واقع برروی صفحه است. ایده کلی اینگونه می باشد که به هر یک از نقطه ها، یک ناحیه اثر به بعضی که مجموع این نواحی برابر با صفحه شود، نسبت داده می شود. اما در ابعاد بزرگتر، مثلا در مدل های استفاده شده در کاربرد های طراحی با استفاده از کامپیوتر که تمامی آنها ۳ بعدی می باشند، بدست آوردن نزدیکترین نقطه (ناحیه) اثر به سادگی میسر نخواهد بود.

با در نظر گرفتن این که عمومی کردن دیاگرام ورونوی به جهت دسته بندی مواردی غیر از نقطه هم کاربرد فراوانی دارد اما در ابعاد بزرگتر، چون محاسبات سنگین می باشد، استفاده از آن مشکل تر و دردسر ساز می شود.

در الگوریتم های تکرارپذیر به جهت اینکه محاسبات دیاگرام ورونوی، در هر یک از مرحله تکرار الگوریتم سنگین می شود، روند حل مسئله نسبت به دیگر الگوریتم های ناحیه بندی بسیار طولانی خواهد بود.
  
 نمودار ورونوی در شبه کد به صورت زیر می‌تواند باشد :

  <div dir="ltr">
    
  ```
  for each (point in plane){
voronoi[point] = null; // Clear site owner of the point
     for each (site in list_sites){
         double tempdist = distance(point,site);
                  if (voronoi[point] == null || tempdist < distance(point, voronoi[point]) )
voronoi[point] = site; // Update site owner if it’s nearest.
    }
}
                                                                          
```
</div>
   <div align="center">
<img src="voronoi.jpg"/>
   </div>
  در تصویر فوق همانطور که مشخص است بازی بازیکنان B و C بعد از مشاهده‌ی بسته ۴ ممکن است به سمت آن هجوم برند.  اما باتوجه به نمودار Voronoi ، بازیکن D سریعتر به آن می رسد. اگر این سه بازیکن بسته‌ی ۴ را مورد هدف قرار دهند ، با اطمینان بالا می‌توان پیش‌بینی کرد که بازیکن D آن را از آن خود می کند. در این صورت ، هوش مصنوعی بازی باید تصمیم بگیرد که آیا هدفی را انتخاب کند که خارج از Voronoi Area قرار داردو یا ایمن بازی کرده و بسته هایی را انتخاب کند که در همان منطقه Voroni قرار دارند.
 
<br/>
    علاوه بر این، از نمودارهای Voronoi برای به حداکثر رساندن مناطق کنترل استفاده می شود. در بازی متا که در مورد به حداکثر رساندن منطقه کنترل شده است ، شما می توانید در چهار جهت حرکت کنید ، می توان با بررسی دقیق حرکتی را در هر ۴ جهت شبیه سازی کرد و نمودار Voronoi را محاسبه کرد. حرکتی که بزرگترین منطقه Voronoi را ایجاد می کند احتمالاً بهترین حرکت است.
</div>
