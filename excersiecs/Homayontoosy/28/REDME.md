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
  
<div dir="rtl">
و در نهایت تابع بیز مان را تعریف می کنیم و دسته بندی متن را انجام میدهیم:
</div>
<br/>

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

<div dir="rtl">
و یکی از خروجی های اسپم ما به صورت زیر در موقعیت 67 قرار دارد:
</div>  

<div dir="rtl">
خروجی
</div>

![خروجی]("https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/28/1.jpg")

<div dir="rtl">
با استفاده از حل تمرین خانم عسکری
</div>
@EvEaskari
