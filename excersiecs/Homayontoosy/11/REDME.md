
##
####

<div dir="rtl">
 
 سوال :  .مراحل انجام الگوریتم ID3 را به صورت خالصه با یک مثال توضیح دهید
</div>
<br/>
<div dir="rtl">
 
مراحل الگوریتم درخت ID3 به شرح زیر است:
- گره ای برای ریشه درخت ایجاد کن
 - اگر تمامی نمونه های examples، نمونه ی مثبت اند، ریشه را با + علامتگذاری کن و درخت را خروجی بده
- اگر تمام نمونه های examples نمونه های منفی اند، ریشه را با – علامت گذاری کن و درخت را خروجی بده
- اگر مجموعه attributes تهی است، ریشه را با متداول ترین دسته بندی نمونه ها علامت گذاری کن و درخت را خروجی بده
- در غیر این صورت:
    </div>
<br/>

<div dir="rtl">
A را ویژگی قرار بده که examples را بهتر دسته بندی می کند
</div>

<div dir="rtl">
ویژگی متناسب با گره ریشه A را قرار بده
 </div>
 
 <div dir="rtl">

برای هر مقدار v_i از A
 </div>

<br/>

<div dir="rtl">
 	یک شاخه جدید در زیر ریشه متناسب با مقدار v_i اضافه کن.
 </div>
<div dir="rtl">
 [example]_(v_i )را زیر مجموعه ای از examples قرار بده که مقدار v_i را برای ویژگی A دارند
 </div>
 <div dir="rtl">
	اگر examples  تهی بود،
<div/>

 
 <div dir="rtl">
	در زیر شاخه جدید گره برگی اضافه کن و آن را با متداول ترین مقدار target-attribute در examples علامت گذاری کن.  
 <div/>

 
 <div dir="rtl">
  	در غیر این صورت، در زیر این شاخه جدید زیر درخت  
 <div/>
  
  <div dir="rtl">
ID3(examples vi.target attribute. attribute-{A}) را اضافه کن  
    <div/>
	  
<div dir="rtl">   
درخت ایجاد شده را برگردان.
 <div/>  
 <br/> 
<div dir="rtl">
یک نمونه ساده از این درخت:
	
می خواهیم درخت A∪(B∩C) را بکشیم. ابتدا جدول درستی آن را که به صورت زیر است میکشیم:
<div/> 

  </div>
  
 ![جدول درستی](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/11/1.jpg)
 
 <br/>

<div dir="rtl">	
سپس مقادیر مثبت و منفی را برای محاسبه آنتروپی در جدول زیر قرار می دهیم:	
 </div>	
  </div>
  
 ![مقادیر مثبت و منفی](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/11/2.jpg)
 
 <br/>			  
 </div>
<div dir="rtl">	 
در محله بعد، Gain هر کدام از نمونه ها را محاسبه می کنیم:	 
 </div>  
	 
 ![gain](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/11/3.jpg)
 
 <br/>	  	
 </div>
<div dir="rtl"> 
در هر مرحله، ویژگی که Gain بیشتری دارد در سطح بالاتری نسبت به بقیه قرار می گیرد. درختی که از محاسبات بالا بدست می آید به صورت زیر است (شاخه های سمت چب مسیر 0 و شاخه های سمت راست مسیر 1 هستند)	 
</div>
	 
 ![عکس](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/11/4.jpg)
 
 <br/>	 
	
	
	
	

