<div dir="rtl">
  
  با توجه به دیتاست covid که در پوشه ی data موجود است عملیات زیر را روی این دیتاست انجام دهید:
  - نرمالیزه کردن
  - مرتب سازی داده
  - حذف داده های یکسان و تکراری
  - بدست آوردن 5 ویژگی که کمترین اهمیت را دارند
  -  اجرای الگوریتم های find-s و ce و بیز و knn و کلاسترینگ و درخت تصمیم یکبار به صورت تصادفی و یک بار با الگوریتم id3
  - داده های زیر همگی به عنوان true برچسب گذاری خواهند شد و ترکیبات داده ای دیگر به عنوان false تمام ترکیبات داده ای که قابل کشف می باشد را بدست آورید.
  - الگوریتم های اجرا شده را با rappid minner نیست اجرا کنید و نتیجه ی خود را با آن مقایسه کنید
  - دیتاست در سایت kaggle ثبت شده است در صورتی که کد خود را در بخش notebook های kaggle ثبت کنید نمره ی اضافه دریافت خواهید کرد.
  ----------------------------------
  ابتدا کتابخانه های مورد نظر را فراخوانی می کنیم که داریم:<br>
 <div dir="ltr"> 
  
 ``` 
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
``` 
<br>
   <div dir="rtl">
     سپس دیتا ست مورد نظر را می حوانیم :<br>
 <div dir="ltr"> 
  
 ```      
# making data frame from json file
data = pd.read_csv("covid.csv")
# display
data
  ```  
   ![image](https://user-images.githubusercontent.com/94124607/149666192-6990cf8c-ca90-405b-9c97-e5a87b963dcc.png)<br>
   سپس اطلاعاتی را از دیتاست با توجه به دستور زیر به دست می آوریم:<br>
   
 <div dir="ltr"> 
   
 ```      
data.info()
data.describe().transpose()
 ```    
![image](https://user-images.githubusercontent.com/94124607/149666282-df93f7fc-f3e1-4b55-831e-74471a7a93dd.png)<br>
   ![image](https://user-images.githubusercontent.com/94124607/149666311-78f1af1f-2fec-431a-8616-7a768c04c7d9.png)<br>
   
 سپس چک می کنیم که آبا مقدار null  ای در دیتا ست وجود دارد یا خیر که اگر موجود بود با مقداری جایگزین می کنیم :<br>
   
   <div dir="ltr"> 
  
 ```  
     data.isnull().sum()
 ```
 ![image](https://user-images.githubusercontent.com/94124607/149666430-6895f614-6475-4929-b1d1-3abf3558a1a9.png)<br>
  
  باتوجه به اینکه یک مقدار نال در ستون هدک موجود است بنابراین مقدار آن را با یس جایگزین می کنیم .<br>
    ![image](https://user-images.githubusercontent.com/94124607/149666613-1fd1a923-9af0-40db-8fe4-8b8b93e1d3e4.png)<br>
     سپس چک می کنیم که مقدار nan نداشته باشسم :<br>
     <br>
     <br>
     با توجه به اینکه مقادیر miss value زیادی در سن در دیتاست موجود است ، بنابراین ستون را حذف می کنیم :<br>
   ![image](https://user-images.githubusercontent.com/94124607/149666730-93f94398-46d4-49f5-a30f-e0806b4cf588.png)<br>
    مرحله بعدی تمام داده های موجود در دیتاست را با عدد جایگزین می کنیم :<br>
     ![image](https://user-images.githubusercontent.com/94124607/149666789-25a137db-21d2-4b30-8f3b-6f2a697c01bc.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149666813-b08a1300-a82b-437f-b58d-488154919790.png)<br>
     مرحله بعدی ستون concept  را ایجاد می نماییم :<br>
     ![image](https://user-images.githubusercontent.com/94124607/149666877-0024577f-7779-46c0-b910-46df01a72049.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149666895-bd287e3b-cce2-4b14-882f-e4089382c4a5.png)<br>
     مرحله بعد داده های را اسکیل بندی و نورمالیزه می کنیم کخ برای این کار ابتدا کتابخانه  هارا فراحوانی می کنیم و داریم :<br>
     ![image](https://user-images.githubusercontent.com/94124607/149666949-c32dc333-d45c-4552-a350-d3b85792ac16.png)<br>
     و به حالت دیتافریم در می آوریم:
     ![image](https://user-images.githubusercontent.com/94124607/149666967-322e0183-ced3-4d43-9f6c-b585f5f2307d.png)<br>
     مرحله بعدی مقدار تارگت را لیبل گذار ی می کنیم که اگر همه فیچرها برابر صفر بود آنگاه مقدار تارگت صفر و در غیر این صورت مقدار کانسپت برابر یک می شود.<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667028-f928b194-a29e-4c50-8b00-11b22c465e23.png)<br>
    ![image](https://user-images.githubusercontent.com/94124607/149667082-8d86bf7a-8fd8-47da-916a-ade7fa2331ed.png) <br>
سپس داده هارا بر اساس ستون sleep  مرتب سازی  می کنیم :<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667186-f12e2a2c-2b24-4f48-a7f5-0aba329f5d8b.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667202-357d6d16-b1a4-402c-a8a6-5d16df67b352.png)<br>
مرحله بعد داده های مشابه و تکراری را پیدا می کنیم و  می شمریم وحذف می نماییم  :<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667244-02789a7f-a076-4a4b-9d0a-f409e9a8381f.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667304-f0d4d720-838f-4c22-b0ed-7650d7ed66e5.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667334-7ceb28d7-d380-4e94-8637-1ceac2dcf530.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667386-9ac8f498-084b-40f4-8f5d-62447cb531ca.png)<br>
     مرحله بعدی با استفاده از هیت مپ ویژگی هارا رسم می کنیم و سپس مرتب می کنیم و 5 ویژگی اول به عنوان کم اهمیت ترین می باشد .<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667467-285d1eb4-5302-4e6f-a41c-8a9222731caf.png)<br>
     مرحله بعدی الگوریتم find-s را اجرا می کنیم کخ داریم:<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667516-947c08e5-a624-40d0-8c6f-9909a3b7188f.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667531-bad9ac1c-d795-43ad-b89b-ebe426317afc.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667566-d1ef7d0f-c2a8-48d4-9b2a-b1e9b45bd9ce.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667589-13f030f8-ff71-4bb5-b19d-1c5e28fc6609.png)<br>
     مرحله بعدی الگوریتم condidate elimination را اجرا می کنیم :<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667631-ddd3dfb7-3daa-4cc9-9bb1-06bf10952501.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149667645-8df0c5e9-2ec4-45e4-8c0b-9c36155ec2bd.png)<br>
     مرحله بعد الگوریتم بیز را اجرا می کنیم :<br>
     ![image](https://user-images.githubusercontent.com/94124607/149671141-1c18a938-4599-47e7-90da-6276751be309.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149671169-bb75b818-07ed-49e4-ae93-f2e666965b2f.png)<br>
     مرحله بعدی الگوریتم درخت تصمیم را اجرا می کنیم : <br>
     ![image](https://user-images.githubusercontent.com/94124607/149672317-e2af45c2-e77a-41ed-b23a-cb994d936ee8.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149672333-a5a243c9-43a5-482d-910e-f183f5853bcd.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149672357-90a4fec0-7651-4cd6-ae72-7dce52351c6e.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149672370-dda3e978-8317-4c23-a46c-bdf1eb316b97.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149672416-a73dfdf4-0e4d-44a3-882b-08eaf082aa95.png)<br>
     مرحله بعد اجرای الگویتم clustering:<br>
     ![image](https://user-images.githubusercontent.com/94124607/149673550-23fd8ef8-6380-44a0-83e0-7cf8f9fdb70c.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149673578-e70a9cc4-15d4-4bf1-8ff3-697117633b98.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149673602-0df74249-c753-444e-804c-89141893a77c.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149673609-9402223a-593f-4472-8109-300f995daffa.png)<br>
     ![image](https://user-images.githubusercontent.com/94124607/149673623-10cf839a-89fb-41f1-ae9d-025b040a3840.png)<br>





     







     
     






     

     



     






     




     
 
     
     
     
 


