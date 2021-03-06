<div dir="rtl">
###زبان برنامه نویسی اسکالا
<br/>
Scala یک زبان برنامه نویسی شئ گرا و تابعی است .
<br/>
ترکیب دو کلمه Scalable و Language است به معنای زبان مقیلس پذیر .
<br/>
در واقع تلفیق زبان های شی گرایی مثل روبی و جاوا و زبان های تابعی مثل Haskell و Erlang است .
<br/>
کد نهایی اسکالا بر روی یک ماشین مجازی جاوا اجرا می شود به همین دلیل پیش نیاز نصب اسکالا، نصب جاوا است .
<br/>
اسکالا به برنامه نویسان کمک می کند تا وظایف خود را با کد کمتر انجام دهند ولی ساختار پیچیده تری نسبت به جاوا دارد. اما خب برنامه نویسی اسکالا براساس جاوا است بنابراین اگر با دستور زبان جاوا آشنا باشیم یادگیری اسکالا بسیار آسان است و حتی اگر تخصصی در جاوا نداشته باشیم ولی آشنایی با زبان هایی مثل c یا c++ یا پایتون داشته باشیم سبب درک سریع این زبان خواهد شد.
<br/>
<br/>
###چرا اسکالا؟
<br/>
این زبان برنامه نویسی به گونه ای طراحی شده است که با توجه به نیازهای کاربران خود، از نوشتن اسکریپت های کوچک گرفته تا ساختن یک سیستم عظیم برای پردازش داده، رشد کند.
<br/>
- متن باز است و یک زبان سطح بالا است، بنابراین یادگیری اسکالا برای هرکس بسیار آسان می شود. 
<br/>
- شامل ویژگی های زبان های مختلف مانند سی و سی ++ و جاوا و .. است که باعث می شود این محصول مفیدتر، مقیاس پذیر و پر بار باشد. 
<br/>
- اکثر شرکت های معروف مانند اپل، توییتر، گوگل و غیره اکثر کدهای خود را از برخی زبان های دیگر به زبان برنامه نویسی اسکالا منتقل می کنند به این دلیل که بسیار مقیاس پذیر است.
<br/>
- برای برنامه های وب پشتیبانی را با گردآوری به جاوا اسکریپت ارائه می دهد. به طور مشابه برای برنامه دسکتاپ می توان آن را به برنامه کدگذاری ماشین مجازی جاوا وارد کرد.
<br/>
###تفاوت جاوا با اسکالا :
<br/>
اسکالا یک زبان برنامه نویسی با تایپ ایستا است در حالی که جاوا یک زبان برنامه نویسی چند پلتفرمی، شبکه محور است.
<br/>
زبان تایپ ایستا زبانی است (مانند جاوا، یا سی و سی++) که در آن انواع متغیر در زمان کامپایل شناخته می شوند. در اکثر این زبان ها، انواع باید به صراحت توسط برنامه نویس مشخص شود.
<br/>
علاوه بر این متغیرهای اسکالا به طور پیش فرض از نوع تغییرناپذیر هستند در حالی که متغیرهای جاوا از نوع پیش فرض قابل تغییر هستند. 
<br/>
###محیط برنامه نویسی :
<br/></div>
![](https://raw.githubusercontent.com/semnan-university-ai/machine-learning-class/main/presentation/fatemeh456/scala.png?token=AWODYOYM4ERHHWEJIUQ2XDLBV7O44)
<br/><div dir="rtl">
در قسمت میانی این برنامه امکان نوشتن برنامه و ذخیره سازی آن وجود دارد. در سمت چپ تمام پروژه ها و کلاس ها و ... و در سمت راست خروجی برنامه و در قسمت پایین تمام اشیاء تعریف شده در برنامه را خواهیم دید.
<br/>
لازم به ذکر است در اسکالا محیطی همچون ترمینال نیز وجود دارد که امکان اجرای مستقیم برنامه را فراهم می کند.
<br/>
####فرمان چاپ خروجی :
<br/></div>
'''println("Hello")<br/>
println("Bye")<br/>
println()<br/>
print("Hello")<br/>
print(" Bye")'''
<br/><div dir="rtl">
Println خروجی ها را در خطوط مجزا از هم چاپ می کند و print عمل چاپ در کنار هم را انجام می دهد.
<br/>
خروجی :
<br/>
'''Hello<br/>
Bye<br/>
Hello Bye'''
<br/>
###تعریف متغیر :
<br/>
دو نوع متغیر در اسکالا موجود است :
<br/>
**Val** = متغیری که غیر قابل تغییر است .
<br/>
**Var** = متغیری که قابل تغییر است .
<br/>
الزامی به تعریف نوع متغیر نیست و کامپایلر اسکالا آنقدر هوشمند است که متوجه نوع داده شود  ولی می توان این کار را هم انجام داد. بنابراین متغیر ها به صورت های زیر قابل تعریف است .
<br/>
'''
val string = "hello"<br/>
val boolean = true<br/>
val char = 'a'<br/>
<br/>
var mystring: String = "hello"<br/>
var myboolean: Boolean = true<br/>
var mychar: Char = 'a'<br/>
'''
###انواع Type های موجود در اسکالا :
<br/>
'''
val astring: String = "hello"<br/>
  val aBoolean: Boolean = true<br/>
  val achar: Char = 'a'<br/>
  val aint: Int = 42<br/>
  val ashort: Short = 123<br/>
  val along:Long = 1362596586L<br/>
  val afloat: Float = 2.3f<br/>
  val adouble: Double = 3.5
'''
<br/>
نوع خاصی از اعداد int ، اعداد short و long است که اولی محدودیت در ارقام دارد ولی دومی خیر.
<br/>
اما لازم است دقت شود برای معرفی اعداد Long باید انتهای عدد را به L ختم کنیم و در اعداد float هم لازم است به f ختم کنیم وگرنه عددمان با فرمت double شناخته خواهد شد.
<br/>
تمام متغیرهای بالا به شکل زیر نیز قابل تعریف هستند :
<br/>
'''
val astring = "hello"<br/>
  val aBoolean = true<br/>
  val achar = 'a'<br/>
  val aint = 42<br/>
  val ashort = 123<br/>
  val along = 1362596586L<br/>
  val afloat = 2.3f<br/>
  val adouble = 3.5
'''
<br/>
**نکته** :قرار دادن ; در انتهای دستورات الزامی نیست ولی اگر بخواهیم چندین دستور را پشت سر هم بنویسیم لازم است از ; بهره ببریم.
<br/>
'''var x=2; var y=2; var z=3;'''
<br/>
###کار بر روی رشته ها :
<br/>
برای ترکیب دو یا چند رشته، راه های مختلفی وجود دارد همچون :
<br/>
'''var name = "sara"<br/>
 var last = "Rezaee"<br/>
var fullname = name + " " + last<br/>
 println(fullname)<br/>
'''
یا استفاده از متد concat به صورت زیر :
<br/>
'''var full = println(name.concat(" ").concat(last))'''
<br/>
و یا استفاده از Interpolator ها .
<br/>
###Interpolator :
<br/>
به ما این امکان را می دهند تا از متغیر ها و عبارات محاسبه ای در رشته ها استفاده کنیم این کار را با به کار بردن $  انجام می دهیم .
<br/>
اولین نمونه آن s است که به صورت زیر به کار می رود :
<br/>
'''//s<br/>
 println(s"fullname is : $name $last")<br/>
 println(s"3*5+2 = ${3*5+2}")<br/>
'''
####خروجی :
<br/>
'''fullname is : sara Rezaee<br/>
3*5+2 = 17'''
<br/>
 و نوع دوم f است که ساختاری مشابه s  دارد اما با قابلیت های بیشتر
<br/>
در f می توان نوع داده ها را مشخص کرد که اگر جز آن ها وارد شد خطایی را به ما نشان دهد .
<br/>
'''//f<br/>
 var age = 18<br/>
 println(f"$name%s is $age%d years old") //%f = float  %s = string %d = int<br/>
'''
####خروجی :
<br/>
'''sara is 18 years old'''
<br/>
####سایر متدهای موجود در رشته ها :
<br/>
'''println(fullname.charAt(0))'''
<br/>
کاراکتر متناظر با آن کاراکتر را بر می گرداند.<br/>
'''println(name.isEmpty())'''
<br/>
بررسی تهی بودن رشته <br/>
'''println(fullname.length())'''
<br/>
محاسبه طول رشته
<br/>
'''println(name.toUpperCase())'''
<br/>
تبدیل کاراکتر ها به فرمت بزرگ آن ها
<br/>
'''var name2="SARA"<br/>
 println(name2.toLowerCase())'''
<br/>
تبدیل کاراکتر ها به فرمت کوچک آن ها
<br/>
###محاسبات ریاضی :
<br/>
علاوه بر محاسبات ریاضی ساده ، کتابخانه math در اسکالا موجود است که برای استفاده از آن باید ابتدا آن را فراخوانی کرد به صورت زیر :
<br/>
'''import scala.math._'''
<br/>
علامت _  به معنای فراخوانی تمام توابع آن کتابخانه می باشد .
<br/>
و سپس می توان به صورت زیر از تابعی مثل abs که در math موجود است استفاده نمود :
<br/>
'''
println(abs(-9))<br/>
println(-9.abs)<br/>
'''
الزامی به قرار دادن () در جلوی توابع نیست .
<br/>
###دستور شرطی if/ else و if/ else if :
<br/>
به صورت زیر می توان تعریف نمود :
<br/>
'''var x= 20<br/>
  if(x==20){<br/>
    println("x is 20")<br/>
  }else{<br/>
    println("x is not 20")<br/>
  }<br/>
'''
اگر بتوان در یک خط تابع را تعریف کرد نیازی به {} نیست همچون 
<br/>
'''var y = 30<br/>
  var r1 = if (x==20) 20 else 0<br/>
  println(r1)<br/>
'''
حتی می توان خروجی آن را در متغیری ذخیره و آن را چاپ نمود مثل
<br/>
'''var w = 100<br/>
  var res = if (w==100) "z == 100" else "z != 100"<br/>
  println(res)<br/>
'''
و می توان از چندین شرط در دستور خود استفاده کنیم حالا یا با && و یا با ||
<br/>
مثلا :
<br/>
'''
var r2 = if (x==20 &&  y==30) 50 else 0<br/>
  println(r2)<br/>
  <br/>
  var r3 = if (x==40 ||  y==35) 50 else 0<br/>
  println(r3)<br/>
'''
###حلقه های تکرار :
<br/>
**while** : تعریف آن به صورت زیر انجام می شود :
<br/>
'''var x = 1<br/>
  while (x<10){<br/>
    println(x)<br/>
    x += 1<br/>
  }
'''
مثال : جمع اعداد یک تا چهار
<br/>
'''var i = 0<br/>
    var sum = 0<br/>
    while (i<5){<br/>
      i = i + 1<br/>
      sum += i<br/>
    }<br/>'''
**Do-While** :ابتدا دستورات را چاپ میکند سپس شرط را چک می کند بنابراین حلقه ای که در while اجرا نمی شود در do-while یک بار اجرا خواهد شد مثلا
<br/>
'''var y = 0<br/>
    do{<br/>
      println("y = " + y)</br>
      y += 1<br/>
    }while(y<10)<br/>'''
**for** :در این حلقه ها هم to و هم until می توان به کار برد. To خود آن عدد را هم چاپ می کند اما until تا آن عدد را چاپ خواهد کرد .
<br/>
مثلا
<br/>
'''for (a <- 0 to 10){<br/>
      println(a)<br/>
    }<br/>
      println()<br/>
      <br/>
      for (b <- 0 until 10){<br/>
      println(b)<br/>
    }'''
<br/>
خروجی :
<br/>
'''0<br/>
1<br/>
2<br/>
3<br/>
4<br/>
5<br/>
6<br/>
7<br/>
8<br/>
9<br/>
10<br/>
<br/>
0<br/>
1<br/>
2<br/>
3<br/>
4<br/>
5<br/>
6<br/>
7<br/>
8<br/>
9<br/>
'''
حتی می توان چندین رنج در حلقه استفاده کرد مثلا
<br/>
'''for (i <- 1 to 3; j <- 1 to 2){<br/>
       println(i + " " + j)<br/>
     }'''
<br/>
خروجی :
<br/>
'''1 1<br/>
1 2<br/>
2 1<br/>
2 2<br/>
3 1<br/>
3 2'''
<br/>
حتی می توان از شرط یا شروطی در حلقه استفاده کرد که در صورت برقرار بودن آن ها حلقه اجرا شود مثلا
<br/>
'''println()<br/>
     for (i <- 1 to 10 if i%2==0){<br/>
       println(i)<br/>
     }<br/>
      
       println()<br/>
     for (i <- 1 to 50 if i%2==0 if i%3==0){<br/>
       println("i = " + i)<br/>
     }'''
<br/>
خروجی :
<br/>
'''2<br/>
4<br/>
6<br/>
8<br/>
10<br/>
<br/>
i = 6<br/>
i = 12<br/>
i = 18<br/>
i = 24<br/>
i = 30<br/>
i = 36<br/>
i = 42<br/>
i = 48'''
<br/>
###Match :
<br/>
این عبارت برای انتخاب یک مورد از بین چندین مورد است مشابه switch در جاوا (ولی قدرتمندتر)
<br/>
هر بار بسته به داده ورودی یک case اجرا می شود و بعنوان حالت پیش فرض نیز می تاون مقداری را مشخص نمود . برای این کار از _ استفاده می کنیم. به صورت زیر تعریف می شود :
<br/>
'''val age = 50<br/>
  age match {<br/>
    case 20 => println(age)<br/>
        case 30 => println(age)<br/>
            case _ => println(0)<br/>
  }'''
<br/>
خروجی  عدد 0 خواهد بود چون ورودی 50 است و جزء حالت پیش فرض به حساب می آید.
<br/>
مثال : تشخیص زوج یا فرد بودن عدد
<br/>
'''val i =8<br/>
  i match {<br/>
    case 1 | 3 | 5 | 7 | 9 => println("odd")<br/>
    case 2 | 4 | 6 | 8 | 10 => println("even")<br/>
  }'''
<br/>
در خروجی even چاپ خواهد شد.
<br/>
###توابع :
<br/>
ساختار توابع :
<br/>
'''/* def function-name [Parameters]: Output-type = {<br/>
   * ...<br/>
   * return<br/>
   * }'''
<br/>
قرار دادن return الزامی ندارد و توابع در اسکالا بطور پیش فرض آخرین مقدار  محاسبه شده را برمی گردانند .
<br/>
مثال : تعریف تابع جمع دو عدد و فراخوانی آن
<br/>
'''def sub (x:Int , y:Int):Int = return x - y<br/>
  println(sub(40,30))'''
<br/>
نام توابع می توانند عمگرها نیز باشند .
<br/>
همچنین می توان مقادیر پیش فرضی را به پارامترهای ورودی توابع اختصاص داد تا چنانچه کاربر مقداری را وارد ننمود آن مقادیر را در نظر بگیریم مثلا :
<br/>
'''def * (x:Int = 2 , y:Int = 3):Int ={<br/>
    return x * y<br/>
  }<br/>
  println(*(20,30))<br/>
  println(*())<br/>
  println(*(20))'''
<br/>
در خط اول از مقادیر ورودی استفاده می کند در خط دوم از مقادیر پیش فرض و در خط سوم x  را 20 گرفتخ و برای y از مقدار چیش فرض اسفاده می کتد.
<br/>
توابع بی نام : توابعی که نامی ندارند و به صورت درجا استفاده می شوند :
<br/>
'''var add = (x:Int , y:Int) => x + y<br/>
   println(add(5,6))'''
<br/>
###توابع partially applied function :
<br/>
'''
// partially applied function<br/>
  var myfunc = (a:Int , b:Int) => a + b<br/>
  val PAfunc = myfunc(30 , _:Int)<br/>
  println(PAfunc(2))'''
<br/>
در مثال بالا تابع PAfunc از نوع partially است به این معنا که ما تابعی را تعریف کردیم بخشی از پارامترها را فیکس نموده و مابقی آن را به عنوان ورودی دریافت می کنیم . علامت _ به معنای بهره بردن از تابع myfunc به ازای هر مقداری است .
<br/>
###انواع ساختمان داده ها در اسکالا :
<br/>
1- **آرایه** :<br/>
سایز آن ها ثابت ، دارای مقادیر هم نوع بوده و عناصر آن دارای اندیس است که از صفر شروع می شود .
<br/>
روش های مختلفی برای تعریف آن وجود دارد و انتساب مقادیر به آن نیز می تواند به صورت مستقیم یا غیر مستقیم باشد .
<br/>
'''val array_name:Array[type_value] = new Array[type_value](number of array)'''
<br/>
و یا
<br/>
'''val array_name = new Array [type_value](number of array)'''
<br/>
بعنوان مثال
<br/>
'''val arr1:Array[Int] = new Array[Int](4)<br/>
  arr1(0) = 10<br/>
  arr1(1) = 20<br/>
  arr1(2) = 30<br/>
  arr1(3) = 40'''
<br/>
برای چاپ آن با دستور print نمی توان این کار را انجام داد
<br/>
برای این کار می توان از حلقه for به شکل زیر استفاده کرد :
<br/>
'''for ( i <- arr1){<br/>
    println(i)<br/>
  }'''
<br/>
مقادیر آرایه قابلیت تغییر را نیز دارند مثلا
<br/>
'''arr1(0) = 5'''
<br/>
نوع دیگر تعریف آرایه و انتساب مقادیر به صورت زیر است :
<br/>
تعریف آرایه و انتساب مقادیر به صورت زیر است :
'''val arr2 = new Array [Int](3)<br/>
  arr2(0) = 100<br/>
  arr2(1) = 200<br/>
  arr2(2) = 300'''
<br/>
و چاپ آن به صورت 
<br/>
چاپ آن به صورت
<br/> 
'''for(j <- 0 to (arr2.length - 1)){<br/>
    println(arr2(j))'''
<br/>
اگر بخواهیم می توانیم مقادیر را مستقیما به آرایه منتسب کرد مثلا
<br/>
'''var arr3 = Array [Int](1,2,3,4,5,6,7,8,9)'''
<br/>
اگر مقادیر را از ابتدا اختصاص ندهیم تا پیش از این کار مقادیر پیش فرضی در آارایه ما قرار خواهد گرفت
<br/>
'''val arr4 = new Array [String](2)<br/>
for ( i <- arr4){<br/>
    println(i)<br/>
  }'''
<br/>
در این حالت مقدار پیش فرض Null است 
<br/>
'''val arr5 = new Array [Int](2)<br/>
for ( i <- arr5){<br/>
    println(i)<br/>
  }'''
<br/>
در این حالت مقدار پیش فرض 0 است 
<br/>
'''val arr6 = new Array [Boolean](2)<br/>
for ( i <- arr6){<br/>
    println(i)<br/>
  }'''
<br/>
در این حالت مقدار پیش فرض false است 
<br/>
برای ادغام دو آرایه و چاپ نتیجه نهایی داریم :
<br/>
'''var myarray1 = Array (1,2,3)<br/>
var myarray2 = Array (3,4,5)<br/>
val result = concat (myarray1 , myarray2)<br/>
println(result)<br/>
for (w <- result){<br/>
  println(w)<br/>
}'''
<br/>
2- **لیست** :
<br/>
همچون آرایه ، دارای عناصر هم نوع بوده اما با دو تفاوت :
<br/>
 تفاوت اول : آرایه قابل تغییر است ولی لیست خیر . تفاوت دوم : لیست ها نشان دهنده لیست پیوندی است ولی آرایه مسطح است . اما تکرار در عناصر لیست مجاز است .
<br/>
نحوه تعریف آن :
<br/>
'''  val list_name : List [type_value] = List (values)'''
<br/>
مثلا
<br/>
'''val mylist : List [Int] = List (1,2,3,4,4,5,6,7,7,8,9,10)<br/>
  val names : List [String] = List ("Sara" , "Mina" , "Ali")'''
<br/>
گفتیم که لیست ها غیر قابل تغییرند بنابراین نوشتن چنین دستوری خطا دارد:
<br/>
'''// error : names(0) = "Fatemeh"'''
<br/>
اما می توان با فرمت زیر به ابتدای آ رایه عناصری را افزود 
<br/>
'''println(-1 :: 0 :: mylist)'''
<br/>
حال داریم 
<br/>
'''List(-1, 0, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10)'''
<br/>
ولی یادمان نرود که لیست ها غیر قابل تغییرند و اگر مجدد لیست را چاپ کنیم خواهیم دید تغییری نکرده است .
<br/>
'''List(1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10)'''
<br/>
####متدهای موجود در لیست ها :
<br/>
'''//methods<br/>
  println(mylist.head)'''
<br/>
عنصر اول لیست را برمی گرداند
<br/>
'''println(mylist.tail)'''
<br/>
به جز عنصر اول لیست بقیه را بر میگرداند
<br/>
'''println(mylist.isEmpty)'''
<br/>
بررسی تهی بودن یا نبودن لیست
<br/>
'''println(mylist.reverse)'''
<br/>
معکوس کردن لیست
<br/>
'''println(mylist.min)'''
<br/>
چاپ کوپکترین مقدار لیست
<br/>
'''println(mylist.max)'''
<br/>
چاپ بزرگترین مقدار لیست
<br/>
'''mylist.foreach(println)'''
<br/>
از این متد برای اعمال تغییرات بر روی تک تک عناصر لیست استفاده می شود
<br/>
مثلا جمع تمام عناصر لیست
<br/>
'''//sum<br/>
  var sum:Int = 0<br/>
  mylist.foreach(sum += _)<br/>
  print(sum)'''
<br/>
3- **مجموعه** :
<br/>
مجموعه ای از داده ا که ترتیب ندارند یعنی اندیسی برای آن ها نداریم . برخلاف لیست  بر خلاف لیست ها  فاقد عناصر تکرای بوده و همه آن ها باید unique باشند . البته تکرار خطایی را ایجار نمی کند ولی تنها اولین مقدار را چاپ خواهد کرد . قابل تغییر نیز نیستند .
<br/>
نحوه تعریف :
<br/>
'''var set_name : Set [type] = Set (values)'''
<br/>
مثلا
<br/>
'''var myset : Set [Int] = Set (2,45,87,32,32,65,47)<br/>
  var names :Set [String] = Set ("Sara" , "Tom")'''
<br/>
می توان عناصری را با این ترفند به مجموعه افزود ولی به یاد داشته باشید همچنان مجموعه ما ثابت و بدون تغییر باقی خواهد ماند .
<br/>
'''println(myset + 10)<br/>
  println(myset + 100)<br/>
  println(myset)'''
<br/>
خروجی :
<br/>
'''Set(10, 65, 2, 32, 45, 87, 47)<br/>
Set(65, 2, 32, 45, 87, 47, 100)<br/>
Set(65, 2, 32, 45, 87, 47)'''
<br/>
از آنجا که عناصرمان اندیسی ندارند پس دستور زیر به معنای برگرداندن عناصر نیست بلکه بررسی می کند که آیا آن مقدار در مجموعه موجود هست یا خیر و نتیجه به صورت true یا false است .
<br/>
'''println(myset(2))<br/>
 println(myset(1))<br/>
 println(names("mina"))'''
<br/>
####متد های موجود در مجموعه ها :
<br/>
'''println(myset.head)'''
<br/>
عنصر اول را برمی گرداند
<br/>
'''println(myset.tail)'''
<br/>
بقیه عناصر به جز عنصر اول را بر میگرداند
<br/>
'''println(myset.isEmpty)'''
<br/>
بررسی تهی بودن با نبودن مجموعه
<br/>
<br/>
برای ادغام دو مجموعه داریم :
<br/>
'''//concat<br/>
  var myset1 : Set [Int] = Set (2,45,87,32,32,65,47)<br/>
  var myset2 : Set [Int] = Set (2,6,88)'''
<br/>
'''println(myset1 ++ myset2)'''
<br/>
یا
<br/>
'''println(myset.++(myset2))'''
<br/>
و برای چاپ عناصر مشترک دو مجموعه داریم 
<br/>
'''println(myset.&(myset2))'''
<br/>
چاپ کوچکترین و بزرگترین عنصر به صورت زیر انجام می شود :
<br/>
'''println(myset.max)<br/>
 println(myset.min)'''
<br/>
<br/>
انجام عملیات بر روی تمام عناصر مجموعه 
<br/>
'''//foreach<br/>
  names.foreach(println) //  By for : for ( name <- names){println(name)}'''
<br/>
4- **Map** :
<br/>
مجموعه ای از جفت های key-value دار که key ها باید unique باشند .
<br/>
نحوه تعریف  :
<br/>
'''val map_name: Map [key_type,value_type]= Map(keys1 -> values1 , … )'''
<br/>
مثلا داریم
<br/>
'''val mymap: Map [Int,String]= Map(801 -> "Ali" , 802-> "Sara")'''
<br/>
برای چاپ value ی یک key  داریم 
<br/>
'''println(mymap(802))'''
<br/>
####برخی متدهای موجود 
<br/>
فرض کنید داریم
<br/>
'''val mymap2: Map [Int,String]= Map(801 -> "Ali" , 802-> "Sara" , 802 -> "Omid")<br/>
   println(mymap.keys)'''
<br/>
چاپ تمامی
Key 
ها به صورت منحصر به فرد
<br/>
'''println(mymap.values)'''
<br/>
چاپ تمامی 
Value ها
<br/>
'''println(mymap.contains(801))'''
<br/>
بررسی وجود یا عدم وجود یک 
Key 
در بین 
Key ها
<br/>
####ادغام mapها
<br/>
'''val mymap10: Map [Int,String]= Map(801 -> "Ali" , 802-> "Sara")<br/>
   val mymap20: Map [Int,String]= Map(802 -> "Mina" , 804-> "Omid", 806 -> "Iman")<br/>
   println(mymap10 ++ mymap20)'''
<br/>
خروجی :
<br/>
'''Map(801 -> Ali, 802 -> Mina, 804 -> Omid, 806 -> Iman)'''
<br/>
از تکراری ها  فقط یکی را می آورد .
<br/>
####برخی متد های موجود :
'''println(mymap20.tail)<br/>
  println(mymap20.head)<br/>
  println(mymap20.size)'''
<br/>
5- **Tupel** : 
<br/>
کلاسی است که برخلاف سایر ساختمان داده ها می تواند  دارای عناصر غیر هم نوع باشد . ولی سایز آن ثابت بوده و نمی توانیم مقادیر آن را تغییر دهیم . مرتب است و اندیس آن از 1 شروع می شود .
<br/>
نحوه تعریف :
<br/>
'''val tupel_name = (values)'''
<br/>
یا
<br/>
'''val tupel_name = new TupleWithout space NUMBER OF MEMBERS (values)'''
<br/>
مثلا داریم 
<br/>
'''val mytuple = (1 , "Hello" , 3.56 , false)'''
<br/>
نحوه دسترسی به عناصر آن
<br/>
'''println(mytuple._1)<br/>
  println(mytuple._2)'''
<br/>
برای اعمال تغییرات روی تمام داده های تاپل باید دستور آن را بدین شکل نوشت :
<br/>
'''//print foreach<br/>
  mytuple.productIterator.foreach{<br/>
    i => println(i)<br/>
  }'''
<br/>
نوشتن چنین چیزی دقیقا به معنای تعریف تاپل است :.
<br/>
'''println(1 -> "Tom")<br/>
  println(1 -> "Tom" -> true)'''
<br/>
خروجی :
<br/>
'''(1,Tom)<br/>
((1,Tom),true)'''
<br/>
<br/>
فرض کنید در دل یک تاپل ، تاپل دیگری داریم و هدف دسترسی به یکی از اعضای آن زیر تاپل است .
<br/>
فرض کنید داریم :
<br/>
'''val mytuple2 = new Tuple3 (1 , "Hello" , (2,3)) //Tuple(number)<br/>
  println(mytuple2._3._2)'''
<br/>
به این صورت به عناصر زیر تاپل ها دسترسی خواهیم داشت .
<br/>


</div>
