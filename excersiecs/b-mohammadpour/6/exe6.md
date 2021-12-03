## الگوریتم find-s
| example| citation | size   | in_library | price          | editions  | buy |
|--------|----------|--------|------------|----------------|-----------|-----|
| 1      | some     | small  | no         | affordable     | many      | no  |
| 2      | many     | big    | no         | expensive      | one       | yes |
| 3      | some     | big    | always     | expensive      | few       | no  |
| 4      | many     | medium | no         | expensive      | many      | yes |
| 5      | many     | small  | no         | affordable     | many      | yes |
<div dir="rtl">
الگوریتم find-s ابتدا مثال های اموزشی را می گیرد و براساس انها فرضیه تولید می کند
  <div/>
  </br>
  <div dir="rtl">
  در ابتدا فرضیه اول تهی می باشد
  <div/>
  </br>
  h0={0,0,0,0,0}
    </br>
    <div dir="rtl">
  برچسب سطر اول ما no است و در الگوریتم find-s اولین برچسب مثبت را در نظر می گیریم، بنابراین فرضیه قبلی ا تکرار می کنیم
  <div/>
  </br>
  h1={0,0,0,0,0}
    </br>
    x1={some,small,no,affordable,many}, -
    </br>
     <div dir="rtl">
در سطر دوم برچسب مثبت است بنابراین مقادیر تمامی ویژگی ها را به عنوان فرضیه در نظر می گیریم    <div/>
  </br>
  h2={many,big,no,expensive,one}
    </br>
    x2={many,big,no,expensive,one}, +
    </br>
    <div dir="rtl">
در سطر سوم برچسب منفی است بنابراین فرضیه دو را تکرار می کنیم    <div/>
  </br>
  h3={many,big,no,expensive,one}
    </br>
    x3={some,big,always,expensive,few}, -
    </br>
    
<div dir="rtl">
در سطر چهارم big و one تغییر کرده اند که جای ان ? قرار می دهیم   <div/>
  </br>
  h4={many,?,no,expensive,?}
    </br>
    x4={many,medium,always,expensive,many}, +
    </br>
    <div dir="rtl">
در سطر پنجم عبارت expensive تغییر کرده است    <div/>
  </br>
  h3={many,?,no,?,?}
    </br>
    x3={many,small,no,affordable,many}, +
    </br>
