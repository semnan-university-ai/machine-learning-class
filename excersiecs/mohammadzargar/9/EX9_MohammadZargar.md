<div dir="rtl">

با توجه به داده های زیر این جدول را با کمک الگوریتم find-s حل کنید.
  
  
|     Example    |     Color     |     Toughness    |     Fungus    |     Appearance    |     Poisonous    |
|----------------|---------------|------------------|---------------|-------------------|------------------|
|     1          |     Green     |     Soft         |     No        |     Wrinkled      |     Yes          |
|     2          |     Green     |     Soft         |     Yes       |     Smooth        |     No           |
|     3          |     Brown     |     Hard         |     No        |     Smooth        |     Yes          |
|     4          |     Green     |     Soft         |     Yes       |     Smooth        |     No           |
|     5          |     Orange    |     Soft         |     Yes       |     Wrinkled      |     Yes          |
  
  
  مرحله اول همه را 0 می گذاریم.
  
  h0=<0,0,0,0>
  
  از اینجا به بعد هر سطر Yes فرضیه را تغییر می دهد ولی سطرهای No تاثیری روی فرضیه ندارند.
  
  h1=<W,N,S,G>
  
  h2=<W,N,S,G>
  
  h3= < ?,N,?,? >
  
  h4= < ?,N,?,? >
  
  h5= < ?,?,?,? >
  
  در نتیجه فرضیه نهایی را به صورت زیر داریم:
  
  h = < ?,?,?,? >
  
  
  
  
  
  
  
  
  
  </div>
