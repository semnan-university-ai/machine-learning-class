# eighth_task
 حل تمرین شماره 8
### first step
<div dir="rtl">
 در مرحله اول بایستی ریشه درخت را مشخص کرد. برای این منظور بایستی information gain تک تک ویژگی عا را حساب کرد و هرکدوم که بیشتر شد بایستی به عنوان ریشه انتخاب شود. رابطه این بهره اطلاعات به صورن زیر حاصل می‌شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145264870-7d21a5b8-3265-4eb5-9974-a6e254c91074.png)

<div dir="rtl">
ابتدا انتروپی کل را محاسبه میکنیم که به صورت زیر حاصل می‌شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145271749-11ee0b71-d42d-44ac-b30f-3dfda380708d.png)

<div dir="rtl">
حال به ویژگی outlook میپردازیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145271888-c85093a3-6161-402b-80dc-b260207ebfdc.png)

<div dir="rtl">
بهره اطلاعات این ویژگی به صورت زیر حاصل می شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145274336-3ad79ff6-b8ba-4770-b2f2-9864aaec6884.png)

<div dir="rtl">
حال به ویژگی Temperature میپردازیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145274877-268dc584-d436-48ad-ba1f-c32d49184fb6.png)

<div dir="rtl">
بهره اطلاعات این ویژگی به صورت زیر حاصل می شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145275455-59bf9f35-317a-48a7-8450-b595ecc279b9.png)

<div dir="rtl">
حال به ویژگی humidity میپردازیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145275802-012d82fe-7a3d-468c-b29c-a1019d4d205d.png)

<div dir="rtl">
بهره اطلاعات این ویژگی به صورت زیر حاصل می شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145277719-ae0b3243-e0b2-4f3b-b5e1-d849b6b2c0ae.png)


<div dir="rtl">
حال به ویژگی Windy میپردازیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145278071-835e445a-035b-4738-98e4-6dacfbf0108a.png)

<div dir="rtl">
بهره اطلاعات این ویژگی به صورت زیر حاصل می شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145278611-325382f1-2a45-461c-b4d1-dfa6150fee88.png)

<div dir="rtl">
چون بهره اطلاعاتی ویژگی tempreture از همه بیشتر شده است لذا این وسژگی به عنوان ریشه درخت در نظر گرفته می شود. 
</div>

### second step

<div dir="rtl">
مقدار cool انتخاب شود، حال آنتروپی کل را محاسبه میکنیم:
</div>


![image](https://user-images.githubusercontent.com/95109502/145289096-7da45591-605a-44e3-933e-2042f21dcd70.png)


<div dir="rtl">
حال به ویژگی outlook میپردازیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145289645-26601b89-5a24-4f0d-9552-3d2680f8c58c.png)


<div dir="rtl">
بهره اطلاعات این ویژگی به صورت زیر حاصل می شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145290199-8fbc26ad-88c4-4efc-bc3b-577e421a571e.png)

<div dir="rtl">
حال به ویژگی humidity میپردازیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145290528-b05ea769-1f9e-4a54-9a57-8053c589ee5c.png)

<div dir="rtl">
بهره اطلاعات این ویژگی به صورت زیر حاصل می شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145290968-a36e113d-5853-4b8d-a656-277209e092f8.png)

<div dir="rtl">
حال به ویژگی windy میپردازیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145291388-480eb6c6-ebb8-403c-9456-51fcc24243e9.png)

<div dir="rtl">
بهره اطلاعات این ویژگی به صورت زیر حاصل می شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145292219-3d0278e8-55f2-4318-9f7c-2860aec3b7ce.png)

<div dir="rtl">
لذا با تصمیم گیری cool ویژگی humidity بالاترین بهره اطلعاتی را دارد و به عنوان ویيگی برتر انتخاب می‌شود.
</div>

<div dir="rtl">
مقدار mild انتخاب شود، حال آنتروپی کل را محاسبه میکنیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145293302-b9cf99a9-3b1c-43d5-a09e-7b9a264cb503.png)

<div dir="rtl">
حال به ویژگی outlook میپردازیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145293690-c433178e-2c05-4bbb-9179-23ff601397de.png)

<div dir="rtl">
بهره اطلاعات این ویژگی به صورت زیر حاصل می شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145293922-9f6e0151-ac0f-4fff-9714-44d744583522.png)

<div dir="rtl">
حال به ویژگی humidity میپردازیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145297638-cf192f97-5df9-4f6c-993e-461054a60be0.png)

<div dir="rtl">
بهره اطلاعات این ویژگی به صورت زیر حاصل می شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145302259-928d47df-0882-4d41-ad3a-d90988407685.png)


<div dir="rtl">
حال به ویژگی windy میپردازیم:
</div>

![image](https://user-images.githubusercontent.com/95109502/145302360-9ec6e950-b497-4247-9fea-e5c9e1fcaba3.png)

<div dir="rtl">
بهره اطلاعات این ویژگی به صورت زیر حاصل می شود:
</div>

![image](https://user-images.githubusercontent.com/95109502/145302082-6730deb6-535e-45d8-92c7-f5b615c3c718.png)

<div dir="rtl">
لذا با تصمیم گیری cool ویژگی outlook بالاترین بهره اطلعاتی را دارد و به عنوان ویيگی برتر انتخاب می‌شود.
</div>

<div dir="rtl">
 
 در نهایت شکل درخت تصمیم به صورت زیر حاصل می شود:
 </div>
 
 ![image](https://user-images.githubusercontent.com/95109502/145304814-b69be6f9-8d13-4f19-b29a-198c6dd5bc85.png)
