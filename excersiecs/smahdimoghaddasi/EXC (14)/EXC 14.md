
<div dir="rtl">
  
 ### 14) با کمک سه روش درخت تصمیم،  Candidate-Elimination و ID3 داده های زیر را حل کنید.
  </div>
  
| Example | Size  | Color | Shape    | Class/Label |
|---------|-------|-------|----------|-------------|
| 1       | big   | red   | circle   | No          |
| 2       | big   | red   | triangle | Yes         |
| 3       | small | red   | circle   | No          |
| 4       | big   | red   | triangle | No          |
| 5       | small | blue  | circle   | No          |
  <div dir="rtl">
  <br/>
  حل به روش حذف کاندید:
  </div>
  
  <br/>
  S0=<0,0,0> 
  
  G0=<?,?,? >
  <br/>
  
  X1=<big,red,circle> - <br/>
  S1=<0,0,0><br/>
  G1=<small,?,?>   <?,blue,? >  <?,?,triangle>
  <br/> 

  X2=<big,red,triangle> + <br/>
  S2=<big,red,triangle><br/>
  G2=<?,?,triangle><br/>
  
  X3=<small,red,circle> - <br/>
  S3=<big,red,triangle><br/>
  G3=<?,?,? ><br/>

  X4=<big,red,triangle> -<br/>
  S4=<big,red,triangle><br/>
  G4=<?,?,? ><br/>
 
  X5=<small,blue,circle> -<br/>
  S5=<big,red,triangle><br/>
  G5=<?,?,? ><br/>
 <div dir="rtl">
در نتیجه به فرضیه ی درستی نمی رسیم.
  
  
