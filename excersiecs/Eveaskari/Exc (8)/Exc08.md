<div dir="rtl">

### با روش ID3 درخت تصمیم جدول زیر را رسم کنید.
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
روش ID3 یک روش ساخت درخت تصمیم گیری با استفاده از احتمال است.
  <br/>
  این روش در ساخت درخت های غیر باینری بهتر عمل میکند.
  <br/>
  در این روشی از مفهومی به نام Entropy استفاده می شود، که منظور همان بی نظمی است.
  <br/>
  فرمول انتروپی: <div dir="ltr"> -(p+.logp+ + p-.logp-) </div>
  <br/>
  که در آن لگاریتم ما بر مبنای 2 است.
  <br/>
  برای مثال دو حالت 0 و 1 را برای احتمال p در نظر بگیرید:
  <br/>
  در این حالت انتروپی 0 می شود .که یعنی سیستم بی نظمی ندارد و جواب همیشه قطعی است.
  <br/>
  برای حالت p که 50/50 باشد: در این حالت انتروپی 1 میشود که بدین معنیست که سیستم کاملا بی نظم است و میشه گفت غیر قابل پیش بینی است و سیستم قطعی نیست.
  <br/>
  برای ساخت درخت تصمیم و جایگاه گره ها باید information Gain را بدست آوریم:
  <br/>
    Gain(S,A) = Entropy(S) - ∑(|Sv |)/(|S|).Entropy(Sv)
  <br/>
  حل:<br/>
  
  ![Gain](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(8)/Gain.jpg)
  
  از آنجایی که به دنبال gain بالا هستیم temperatur با Gain = 0.178 به عنوان ریشه انتخاب میشود.
  <br/>
  برای ادامه کار مرحله بعد را با انتخاب دو حالت  mild و cool  که جواب نهایی ندارند را بررسی میکنیم تا بفهمیم گره بعدی درخت کدام ست.
  <br/>
  
  ![id3-p2](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(8)/id3-p2.JPG)
  
  و در نهایت درخت بدین شکل در می آید:<br/>
  
  ![tree](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(8)/ID3tree.JPG)
  

 </div>

