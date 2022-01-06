### با دیتاست جمع آوری شده از پیامک ها و دیتاست کلمات اسپم پیامک های فارسی به همراه الگوریتم بیز تصمیم گیری در مورد هر پیامک را داشته باشید

</div>

```  
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
sb.set(style='dark')

```  
ده خط اول متن را نمایش میدهیم:

```  
!head -n 10 sms.txt

```  




طول دیتاست را نمایش میدهیم:

```

sms= open('sms.txt', 'r').read()
len(sms)

```

```
splited= sms.split('\n')
splited[:5]
```

```
print(splited[2])
```

برای برچسب زدن به فایل های spam و sms به این صورت عمل میکنیم:

ابتدا دیتاست را فراخوانی میکنیم:

```
spam = pd.read_csv('spam-word.txt', encoding='utf-8')
```

یک لیستی از متن ها و کلمه ها ایجاد میکنیم:

```
kalame = {}
text={}
```
یک تابعی از متن به طول کلمات درست میکنیم:
```
def kalamat(text):
  indx = len(kalame)
```

برای هر کلمه در متن برچسب گذاری را انجام میدهیم:

```
for word in text:
  
    kalame[word] = indx
    indx += 1

if __name__ == '__main__':
  for i in range(spam.shape[0]):
    text = spam.iloc[i,0].split()
    print('the length of kalamat is ', len(kalame))

  kalamat(text)
```
لیست تولید شده را به صورت یک فایل kalame.txt ذخیره میکنیم:

```
file = open("kalame.txt", "w")
file.write(str(kalame))
file.close()
```




