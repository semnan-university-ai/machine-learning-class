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
h0=<0,0,0,0>
<br/>
چون جواب x1 yes هست مقدار x1 به طور کامل در h1 قرار می گیرد.
<br/>
x1=<G,S,N,W> ->YES
h1=<G,S,N,W>
<br/>
چون جواب x2 NO هست مقدار h1 تغییر نمی کند.
<br/>
x2=<G,S,N,W> ->NO
h2=<G,S,N,W>
<br/>
جواب x3 YES در نتیجه تغییرات x2 و x3 را ؟ قرار می دهیم.
<br/>
x3=<B,H,N,S> ->YES
h3=<?,?,N,?>
<br/>
جواب x4 NO پس مقدار h4 تغییر نمی کند.
<br/>
x4=<G,S,Y,S> ->NO
h4=<?,?,N,?>
<br/>
در نهایت x5 YES و h5 تغییر می کند.
<br/>
x5=<O,S,Y,W> ->YES
h5=<?,?,?,?>
</div>
