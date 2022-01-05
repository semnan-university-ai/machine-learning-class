<div dir="rtl">
سوال : با دیتاست جمع آوری شده از پیامک ها و دیتاست کلمات اسپم پیامک های فارسی به همراه الگوریتم بیز تصمیم گیری در مورد هر پیامک را داشته باشید.
</div>
<br/>

<div dir="rtl">
در ابتدا برای دسترسی به فایل هایمان به گوگل درایو متصل می شویم:  
</div>
  
  
import pandas as pd

myvokab = {}

spam = pd.read_csv('/content/gdrive/MyDrive/dataset/spam.txt', encoding='utf-8')

#set_word = set(words.words())

def my_vokab(text):

indx = len(myvokab)

for word in text:

#if word.lower() not in myvokab and word.lower() in set_word:
myvokab[word] = indx
indx += 1

if __name__ == '__main__':
for i in range(spam.shape[0]):
text = spam.iloc[i,0].split()
print('the length of vokabulary is ', len(myvokab))

my_vokab(text)

file = open("myvokab.txt", "w")

file.write(str(myvokab))

file.close()

<br/>

<div dir="rtl">
سپس فایل پیامک ها را خوانده و کلمه به کلمه آن را جدا می کنیم تا با تابع فرهنگ لغتمان مقایسه کنیم:
</div>
<br/>

import numpy as np

import pandas as pd

import ast

data = pd.read_csv('/content/gdrive/MyDrive/dataset/sms.txt', encoding='utf-8')

file = open('myvokab.txt', 'r', encoding='utf-8')

cntnt = file.read()

myvokab = ast.literal_eval(cntnt)

x = np.zeros((data.shape[0], len(myvokab)))

y = np.zeros((data.shape[0]))

for i in range(data.shape[0]):

sms = data.iloc[i,0].split()

for sms_word in sms:

if sms_word.lower() in myvokab:

x[i, myvokab[sms_word]] +=1

#y[i] = data.iloc[i, 0]

np.save('/content/gdrive/MyDrive/dataset/x.npy', x)

np.save('/content/gdrive/MyDrive/dataset/y.npy', y)
  

