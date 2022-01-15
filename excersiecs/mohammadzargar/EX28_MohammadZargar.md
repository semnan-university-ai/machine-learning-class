ابتدا فراخوانی کتاب خانه ها راداریم:

```
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
```
# get sms and spam Data
```
spam = pd.read_csv('data/spam.txt', encoding='utf-8')
sms = pd.read_csv('data/sms.txt', encoding='utf-8')
spam = spam['شماره 1'].tolist()

```

# split sms words

```

usms =[]
for i in range(sms.shape[0]):
    usms.append(sms.iloc[i, 0].split())
x = usms
```
# pad sequence sms data

```
list_len = [len(i) for i in x]
csize = max(list_len)
x = [a + ['&'] * (csize - len(a)) for a in x]

```
# set lables for sms data 
```
y= []      
for j in range(len(usms)):
    if any(item in usms[j] for item in spam):
       y.append(1) 
    else:
        y.append(0)  
 ```
# get all unique sms words 
```
words = []   
for i in range(len(usms)):
    for j in range(len(usms[i])):
        words.append(usms[i][j]) 
words = set(words)
words = list(words)
words.append('&')
```
# numerize data
```
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j] = words.index(x[i][j])
```

# get train and test data
```
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)
```
# use Naive Bayes
```
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("Number of mislabeled points out of a total %d points : %d"
      % (len(X_test), (y_test != y_pred).sum()))
```
