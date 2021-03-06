<div dir="rtl">
  
  ## 10) یک نمونه ی واقعی از استفاده ی درخت تصمیم در دنیای واقعی را به صورت کوتاه توضیح دهید.
  <br/>
 
  درخت تصمیم، ساختاری بالا به پایین دارد و مربوط به مسائل classification یا دسته بندی است. درخت تصمیم می تواند دودویی باشد ولی لزوما درخت دودویی درخت تصمیم نیست.
  درخت تصمیم بیشتر در جاهایی کاربرد دارد که بحث پیش نیاز و سلسله مراتب مطرح است.
   <br/>
  <br/>
  ### مثال اول : پیش بینی بیماری نادر
   
  هدف، پيش بيني عوامل جمعيت شناختي بر بيماري نادر است كه بر اساس نادر یا غير نادر بودن طبقه بندي
مي شود؛  طول مدت اقامت ( LOS )، به عنوان دانش حاصل از مدل پيش بيني، به عنوان
مهمترین عامل كه یک بيماري نادر را پيش بيني مي كند، ظاهر مي شود؛ به عبارت دیگر، طول مدت اقامت ( LOS ) قوي
ترین شاخص پيش بيني بيماري هاي نادر است كه ما را قادر مي سازد تا طول مدت اقامت ( LOS ) بيماران را با توجه
به وضعيت بيماري، جنسيت و سن پيش بيني نماییم.
  
  این مطالعه براساس اطلاعات بيماران نادر متعلق به بنياد بيماريهاي نادر ایران براي پيش بيني عوامل موثر بر بيماري هاي
نادر با استفاده از درخت تصميم گيري به عنوان تكنيک داده كاوي بهره گرفته است که ویژگی ها به صورت زیر می باشند:
   <br/>
  <br/>
  ![10.j]( https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(10)/10.j.jpg)
   <br/>
  
  جدول 2 عوامل موثر بر بيماري نادر را نشان ميدهد كه مي توان از آن نتيجه گيري كرد كه اكثر
بيماران مبتلا به بيماري هاي نادر سرپایي، داراي سن بيش از 48 سال مي باشند.
   <br/>
 
   ![10.j2](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(10)/10.j2.jpg)
   <br/>
  درخت تصميم گيري كه خواندن و تفسير را آسان مي نماید نيز به افراد
شاغل در بنياد در ترسيم اطلاعات، كمک شایاني مي نمایند. برخي پيشنهاداتي كه مي تواند در مراكز درماني بيماران نادر
به كارگرفته شود به شرح زیر مي باشد؛ اینكه با این روش ممكن است بنياد بيماري هاي نادر ایران قادر به شناسایي مدت
زمان بستري شدن بيماران مبتلا به بيماري نادر شود كه این موضوع مي تواند مخاطب را در اختصاص ميزان بودجه بيشتر
براي خدمات بهداشتي و داروها به بيماران نادر بستري شده در مقابل بيماران سرپایي مبتلا به بيماري هاي نادر، جهت
برآورد نمودن ميزان پوشش بيمه اي كه باید براي یک بيمار بستري شده در نظر گرفته شود و نيز برآورد نمودن ميزان
پرداختي هزینه حق بيمه پذیرش شدگان در هر ماه، كمک و راهنمایي نماید. همچنين مشاوره هاي بهداشتي مي بایست
صورت گيرند، مخصوصا براي زناني كه مستعد ابتلا به بيماري هاي نادر در مقایسه با همتایان مرد خود مي باشند، دانش،
توانایي، آگاهي از بيماري هاي نادر و درک پذیرش شدگان مي بایست افزایش یابند و حداقل یک بار در سال براي پذیرش
شدگان بالاي 48 سال، غربالگري پزشكي انجام شود. هدف این مطالعه شناسایي عوامل مخاطره آميز براي بيماري هاي نادر
است.
   <br/>
  استخراج اطلاعات از درخت تصميم، ساده تر است.
 از نتایج، مي توان این جمع بندي را نمود كه طول مدت اقامت (LOS) مهمترین عاملي است كه بر وضعيت بيماري ها
تأثير مي گذارد و ما را قادر مي سازد تا طول مدت اقامت بيمار را با توجه به عوامل مختلف مانند سن، جنس و نوع
بيماري شناسایي نماییم.
  
   <br/>
  الگوریتم C4.5 یک مدل طبقه بندي را در قالب درخت تصميم با موفقيت ایجاد مي كند
كه مي تواند به راحتي براي پيش بيني بيماري نادر مورد مطالعه و تفسير قرار گيرد.
<br/>
  
  درخت تصمیم توليد شده در شكل زیر نشان داده شده است. برخي از گره ها در شكل  با عنوان مدت زمان اقامت
( LOS )، به عنوان مهمترین عامل پيش بيني بيماري مي باشد. گره مدت زمان اقامت ( LOS ) ریشه درخت تصميم گيري و
طبقه بندي مي شود، زیرا از ميان دیگر ویژگي ها بيشترین اطلاعات را به خود اختصاص داده است. از این رو، قوانين طبقه
بندي شده از درخت تصميم گيري در دو قسمت، یكي بيماران سرپایي (براي بيماراني كه در یک
روز اقامت دارند) و دیگري تحت عنوان بيماران بستري (براي بيماران كه بيش از یک روز اقامت دارند) توضيح داده شده
است.
    ![10-2](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(10)/10-2.jpg)
  
  <br/>
 
 ### مثال دوم : ازدواج 
  انتخاب همسر، انتخاب یک شریک دائمی در تمام امور زندگی است و یکی از مهمترین و سرنوشت سازترین انتخاب های زندگی هر فرد است. فواید انتخاب شایسته و با معیارهای صحیح در این مرحله به همان اندازه فراوان است که زیان ها و خسارت های ناشی از انتخاب عجولانه و بر اساس ملاک های غلط بسیار است، معیارهای زیادی برای انتخاب همسر وجود دارد، اینکه همسر آینده ما باید دارای چه ویژگی ها و خصیصه هایی باشد بسیار مهم است و اینکه چه ملاک هایی برای ما الویت بیشتری دارد نیز بسیار حائز اهمیت است.
   <br/>
  در واقع برای انتخاب همسر باید چندین معیار را مدنظر قرار داد؛ معیارهای اصلی نظیر ایمان و تدین، اخلاق نیک، شرافت و نجابت خانوادگی، سلامت جسمی و روانی، معیارهای فرعی و ترجیحی مانند تناسب در زیبایی، تناسب سنی، تناسب تحصیلی، تناسب جسمی و جنسی، تناسب اقتصادی، تناسب فرهنگی- اجتماعی. <br/>
  معیارهای اصلی آن دسته از معیارهایی است که وجودشان در امر انتخاب همسر لازم و ضروری است و به هیچ عنوان قابل چشم پوشی نیست؛ اما معیارهای فرعی معیارهای ترجیحی هستند و با رعایت آن ها احتمال به وجود آمدن اختلاف در زندگی مشترک به حداقل می رسد.
  <br/>
  معیارهای اصلی که بیان شد در واقع به عنوان گره های بالایی درخت تصمیم انتخاب می شوند و معیارهای فرعی بعد از معیار های اصلی در درخت تصمیم قرار می گیرند که این ترتیب قرارگیری ویژگی ها در درخت، در واقع اهمیت هر ویژگی را نشان می دهد.  
  
