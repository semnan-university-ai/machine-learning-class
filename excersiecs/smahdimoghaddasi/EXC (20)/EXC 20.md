<div dir="rtl">
  
  ### 20) مفهوم Voronoi diagram را به طور خلاصه بیان کنید.
  
  <br/>
  knn یکی از روش های یادگیری مبتنی بر نمونه است که معمولا در این روش از معیار های فاصله ای همچون فاصله ی اقلیدسی و فاصله منهتن  برای پیدا کردن  k تا از نزدیک ترین همسایه ها به داده ی مورد نظر استفاده می شود.(فاصله اقلیدسی پر کاربردتر است )
<br/>
<br/>
  
![euclidean.png]( https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(20)/euclidean.png)

![manhattan.png]( https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(20)/manhattan.png)
  
<br/>
  Voronoi Diagramروشی برای تقسیم فضا به تعدادی ناحیه می باشد. در این دیاگرام به هر مجموعه ای از نقاط  ناحیه ای اختصاص داده می شود. این نواحی سلول هایVoronoi نامیده می شود. برای یک مجموعه از نقاط Voronoi Diagram سطح را به مناطقی تقسیم بندی می کند که برای هر نقطه از مجموعه نقاط یک منطقه تعریف می شود. به طوری که تمام نقاط این منطقه به نقطه تولیدکننده آن منطقه نزدیکتر می باشد.
  <br/>
  Voronoi Diagram در واقع عمود منصف بین نمونه های آموزشی را رسم می کند و چند ضلعی ای را پیرامون هر نمونه ایجاد می کند. 
  چند ضلعی ای  که نمونه هایش فقط تحت تاثیر یک نمونه آموزشی خاص هستند.
  نمونه های خارج هر چند ضلعی به نمونه دیگری نزدیک ترند.
  <br/>
  Voronoi Diagram  سرعت محاسبات را در 1NN  زیاد می کند  ولی آماده سازی و پیدا کردن Voronoi Diagram خود زمان بر است. 
  </div>
<br/>

![voronoi%20diagram.png]( https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(20)/voronoi%20diagram.png)


 
