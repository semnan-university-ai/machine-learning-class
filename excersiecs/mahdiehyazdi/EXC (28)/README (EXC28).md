### با دیتاست جمع آوری شده از پیامک ها و دیتاست کلمات اسپم پیامک های فارسی به همراه الگوریتم بیز تصمیم گیری در مورد هر پیامک را داشته باشید.

<div align="justify" dir="rtl">
  در ابتدا بری انجام کار در محیط colab لازم است  تا دیتاست های مورد نظر را در گوگل درایو بارگذاری نماییم در ادامه با import کتابخانه گوگل و mount کردن آن امکان دسترسی به داده های موجود در گوگل درایو را خواهیم داشت 
</div>
  <br/>
  
 ```
 from google.colab import drive
drive.mount('/content/gdrive')
```
<div align="justify" dir="rtl">
در ادامه با import  کتابخانه ی pandas تابعی ایجاد کرده ایم تا لیستی از کلماتی که جنبه ی spam دارند را جدا کنیم .
</div>
<br/>

```
import pandas as pd

wordList = {}
spam = pd.read_csv('./gdrive/MyDrive/spam-words.txt', encoding='utf-8')

def word_list(text):
  indx = len(wordList)

  for word in text:
    wordList[word] = indx
    indx += 1

if __name__ == '__main__':
  for i in range(spam.shape[0]):
    text = spam.iloc[i,0].split()
  print('the length of vokabulary is ', len(wordList))

  word_list(text)

file = open("word_list.txt", "w")
file.write(str(wordList))
file.close()
```
<div align="justify" dir="rtl">
  حال دیتاست شامل تمام پیمک ها را بارگذاری میکنیم با این کار امکان مقایسه کلمات موجود در لیست spam ها با کلمات موجود در فایل sms وجود دارد در نتیجه تمام لغات در sms ها با تمام spam ها مقایسه میشوند
  </div>
  <br/>
  
  ```
  import numpy as np
import pandas as pd
import ast

data = pd.read_csv('./gdrive/MyDrive/sms_data.txt', encoding='utf-16')
file = open('word_list.txt', 'r', encoding='utf-8')
cntnt = file.read()
word_list = ast.literal_eval(cntnt)

x = np.zeros((data.shape[0], len(word_list)))
y = np.zeros((data.shape[0]))

for i in range(data.shape[0]):
  sms = data.iloc[i,0].split()

for sms_word in sms:
  if sms_word.lower() in word_list:
    x[i, word_list[sms_word]] +=1
    #y[i] = data.iloc[i, 0]

np.save('/content/gdrive/MyDrive/dataset/x.npy', x)
np.save('/content/gdrive/MyDrive/dataset/y.npy', y)
```

<div align="justify" dir="rtl">
    در این قسمت با ایجاد تابع بیز دسته بندی را برای متن ایجاد میکنیم که با انجام این عمل میتوان متون را به دو دسته ی هرزنامه و غیر هرزنامه تقسیم نمود و برچسب گذاری را انجام داد و نتیجه را به صورت x و y ذخیره میکنیم و دshape های ایجاد شده را print میکنیم و در آخر  تابع naivebayes ایجاد شده را آموزش میدهیم    
  </div>
  <br/>
  
  ```
import numpy as np

class naivebayes():
  def __init__(self, X, y):
    self.num_examples, self.num_features = X.shape
    self.num_classes = len(np.unique(y))
    self.eps = 1e-6
  def fit(self, X, y):
    self.classes_mean = {}
    self.classes_variance = {}
    self.classes_prior = {}

    for c in range(self.num_classes):
      X_c = X[y==c]
      self.classes_mean[str(c)] = np.mean(X_c, axis=0)
      self.classes_variance[str(c)] = np.var(X_c, axis=0)
      self.classes_prior[str(c)] = X_c.shape[0]/self.num_examples

  def predict(self, X):
    probs = np.zeros((self.num_examples, self.num_classes))

    for c in range(self.num_classes):
      prior = self.classes_prior[str(c)]
      probs_c = self.density_function(X, self.classes_mean[str(c)], self.classes_variance[str(c)])
      probs[:, c] = probs_c +np.log(prior)

    return np.argmax(probs, 1)

  def density_function(self, X, mean, sigma):
    const = -self.num_features/2 * np.log(2*np.pi) - 0.5*np.sum(sigma+self.eps)
    probs = 0.5*np.sum(np.power(x-mean, 2)/(sigma+self.eps), 1)
    return const - probs
 
  if __name__ == '__main__':
    X = np.load('/content/gdrive/MyDrive/dataset/x.npy')
    y = np.load('/content/gdrive/MyDrive/dataset/y.npy')
    print(X.shape)
    print(y.shape)

    NB = naivebayes(X, y)
    NB.fit(X, y)
    y_pred = NB.predict(X)

print(sum(y_pred == y)/X.shape[0])
  ```
