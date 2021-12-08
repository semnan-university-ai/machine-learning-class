<div dir="rtl">
8 .با روش ID3 درخت تصمیم جدول زیر را رسم کنید.

</div>  

| day | outlook  | temperature | humidity | windy | play |
|-----|----------|-------------|----------|-------|------|
| 1   | overcast | hot         | high     | false | yes  |
| 2   | rainy    | mild        | high     | false | yes  |
| 3   | rainy    | cool        | normal   | false | no   |
| 4   | sunny    | mild        | high     | false | no   |
| 5   | overcast | mild        | high     | false | yes  |
| 6   | sunny    | cool        | normal   | true  | no   |
| 7   | sunny    | hot         | normal   | true  | yes  |
| 8   | rainy    | cool        | high     | false | yes  |
| 9   | sunny    | cool        | high     | false | yes  |
| 10  | overcast | cool        | normal   | true  | yes  |
| 11  | sunny    | hot         | high     | true  | yes  |
| 12  | rainy    | hot         | high     | true  | yes  |
  <div dir="rtl">
  <br/>
  <br/>
حل:
  <br/>
  
 روش درخت تصمیم با استفاده از محاسبه ی خطا را تنها وقتی می توان استفاده کرد که ویژگی ها باینری باشند. اگر ویژگی ها غیر باینری باشند، از روش ID3 استفاده می کنیم. 
<br/>
   این روش بر مبنای محاسبه ی آنتروپی و گین است. درختی که با محاسبه ی بهره اطلاعاتی بدست می آید را ID3  گویند  و این روش چون  با احتمالات است، حساسیت به نویز کمتری نسبت به روش  محاسبه ی خطا دارد  و روش بهتری است، تاثیر اشتباه را کمتر می کند و آماری تر است. 
  <br/>هر چه آنتروپی (بی نظمی) یک سیستم زیاد باشد یعنی سیستم تصادفی تر است و از حالت قابل پیش بینی بودن خارج می شود. اگر آنتروپی صفر باشد، یعنی سیستم بی نظم نیست و قطعی است و اگر سیستم دارای ماکزیمم آنتروپی(یک) باشد، یعنی سیستم کاملا تصادفی است و گین آن کم است.
<br/>
  در روشID3 برای تمام ویژگی ها باید بهره اطلاعاتی را بدست آوریم و گره ای که دارای بالاترین گین است بهترین گره است و مناسب ریشه درخت تصمیم است .
<br/>
  در این روش هم درخت با عمق کم ساخته می شود و ممکن است اصلا برخی از ویژگی ها در ساخت درخت استفاده نشوند.
  <br/>
 در مرحله ی اول برای انتخاب گره ریشه، Entropy(S) برای تمام ویژگی ها یکسان است. فرمول محاسبه آنتروپی بصورت زیر است:(log در مبنای 2 است) 
  
<br/>
<br/>
  </div>
 Entropy(S)= -((p+ logp+) + (p-logp-))
 <div dir="rtl">
 برای محاسبه information gain از رابطه زیر استفاده می کنیم:
  <br/>
  گین یک سری دیتا مثل S نسبت به یک ویژگی خاص مثلا A
  <br/>
  </div>
 Information Gain(S, A) = Entropy(S) - ∑((|Sᵥ| / |S|) * Entropy(Sᵥ))
  <div dir="rtl">
 S: تعدادمثال های آموزشی  
 <div dir="rtl">
 A :ویژگی خاصی ک بررسی می کنیم
 <div dir="rtl">
 |S|: تعداد کل مثال ها
 <div dir="rtl">
 |Sv|: ویژگی هایی که آن مقدار خاص را دارند 
 
  </div>
  <br/>
 <br/>
  
  
  
  ![8-1](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(8)/8-1.jpeg)
  
  ![8-2](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(8)/8-2.jpeg)
  
  ![8-3](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(8)/8-3.jpeg)
  
 
