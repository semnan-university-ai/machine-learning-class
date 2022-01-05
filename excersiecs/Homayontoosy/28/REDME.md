<div dir="rtl">
سوال : با دیتاست جمع آوری شده از پیامک ها و دیتاست کلمات اسپم پیامک های فارسی به همراه الگوریتم بیز تصمیم گیری در مورد هر پیامک را داشته باشید.
</div>
<br/>
<div dir="rtl">
  در ابتدا برای دسترسی به فایل هایمان به گوگل درایو متصل می شویم:
  </div>
  
  <div dir="rtl">
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
  </div>

<br/>

<div dir="rtl">
سپس فایل پیامک ها را خوانده و کلمه به کلمه آن را جدا می کنیم تا با تابع فرهنگ لغتمان مقایسه کنیم:
  </div>
