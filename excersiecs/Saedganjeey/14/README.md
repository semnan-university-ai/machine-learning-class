<div dir="rtl">
سوال :با کمک سه روش درخت تصمیم، Candidate-Elimination و ID3 داده های زیر را حل کنید.
</div>
<br/>
<div dir="rtl">
درخت تصمیم : (مثال 4 نویز ایجاد کرده در اینصورت آن را حذف کردیم.)
</div>
<br/>
![pic1](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/14/1.png)
<br/>
<div dir="rtl">
در مرحله  بعد نیازی به محاسبه ی خطاهای دئ ویژگی دیگر نیست
 و درخت تصمیم بصورت روبرو است.
</div>
<br/>
![pic1](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/14/2.png)
<br/>
<div dir="rtl">
Size :
Big(1+,1-) =2/4 x -(1/2 x log 1/2 +1/2 x log 1/2)= 0.5
Small (0+,2-) = 0
Sum=0.5
Shape :
Circle (0+,3-) =0
Triangle (1+,0-) =0
Sum=0
Color :
Red (1+,2-) = 3/4 x –(2/3 x log 2/3 + 1/3 x log 1/3) = 0.68
Blue (0+,1-) = 0
Sum=0.68
</div>
<br/>
<div dir="rtl">
روش حذف کاندید :
G0=<?,?,?>
G1=<small,?,?><?,blue,?><?,?,triangle>
G2=<?,?,triangle>
G3=G2
G4=G3
G5=G4
S5=S4
S4=S3
S3=S2
S2=<big,red,triangle>
S1=S0
S0=<0,0,0>

</div>
