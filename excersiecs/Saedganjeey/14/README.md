<div dir="rtl">
سوال :با کمک سه روش درخت تصمیم، Candidate-Elimination و ID3 داده های زیر را حل کنید.
</div>
<br/>
<div dir="rtl">
درختت تصمیم :: (مثال 4 نویز ایجاد کرده در اینصورت آن را حذف کردیم.)
</div>
<br/>
![pic1](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Saedganjeey/14/1.png)
<br/>
<div dir="rtl">
در مرحله  بعد نیازی به محاسبه ی خطاهای دئ ویژگی دیگر نیست
 و درخت تصمیم بصورت روبرو است.
</div>
<br/>
![pic2](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Saedganjeey/14/2.png)
<br/>
<div dir="rtl">
1.Size :

2.Big(1+,1-) =2/4 x -(1/2 x log 1/2 +1/2 x log 1/2)= 0.5

3.Small (0+,2-) = 0

4.Sum=0.5

5.Shape :

6.Circle (0+,3-) =0

7.Triangle (1+,0-) =0

8.Sum=0

9.Color :

10.Red (1+,2-) = 3/4 x –(2/3 x log 2/3 + 1/3 x log 1/3) = 0.68

11.Blue (0+,1-) = 0

12.Sum=0.68

</div>
<br/>
<div dir="rtl">
روش حذف کاندید :
1.G0=<?,?,?>

2.G1=<small,?,?><?,blue,?><?,?,triangle>

3.G2=<?,?,triangle>

4.G3=G2

5.G4=G3

6.G5=G4

7.S5=S4

8.S4=S3

9.S3=S2

10.S2=<big,red,triangle>

11.S1=S0

12.S0=<0,0,0>


</div>
