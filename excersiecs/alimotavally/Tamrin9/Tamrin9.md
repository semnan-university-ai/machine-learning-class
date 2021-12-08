<div dir="rtl">
  
  ### با توجه به داده های زیر این جدول را با کمک الگوریتم find-s حل کنید.
  </div>
  
| Example | Color  | Toughness | Fungus | Appearance | Poisonous |
|---------|--------|-----------|--------|------------|-----------|
| 1       | Green  | Soft      | no     | Wrinkled   | yes       |
| 2       | Green  | Soft      | yes    | Smooth     | no        |
| 3       | Brown  | Hard      | no     | Smooth     | yes       |
| 4       | Green  | Soft      | yes    | Smooth     | no        |
| 5       | Orange | Soft      | yes    | Wrinkled   | yes       |
<div dir="rtl">
در ابتدا h0 را کاملا خاص فرض میکنیم.
<br/>
h0=(0,0,0,0)
<br/>
چون جواب x1= yes هست مقدار x1 به طور کامل در h1 قرار می گیرد.<br/>
<br/>
x1=(G,S,N,W) ->YES<br/>
h1=(G,S,N,W)<br/>
<br/>
چون جواب x2= NO هست مقدار h1 تغییر نمی کند.<br/>
<br/>
x2=(G,S,N,W) ->NO<br/>
h2=(G,S,N,W)<br/>
<br/>
جواب x3= YES در نتیجه تغییرات x2 و x3 را ؟ قرار می دهیم.<br/>
<br/>
x3=(B,H,N,S) ->YES<br/>
h3=(?,?,N,?)<br/>
<br/>
جواب x4= NO پس مقدار h4 تغییر نمی کند.<br/>
<br/>
x4=(G,S,Y,S) ->NO<br/>
h4=(?,?,N,?)<br/>
<br/>
در نهایت x5= YES و h5 تغییر می کند.<br/>
<br/>
x5=(O,S,Y,W) ->YES<br/>
 h5=(?,?,?,?)
</div>
