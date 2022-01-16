# Covid dataset

حمیده احسانی

شماره دانشجویی: 9911624001

ما در این پروژه از کتابخانه های Id3 و candidate elimination  استفاده کرده ایم.
```
pip install decision-tree-id3
pip install classic-CandidateElimination
```
## بخش import کردن کتابخانه های مورد نیاز

```
#Let's Import the Packages...
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB
import six
import sys
sys.modules['sklearn.externals.six'] = six
from id3 import Id3Estimator
from id3 import export_graphviz
from graphviz import Source
from sklearn import metrics
```

## خواندن از فایل - مرتب سازی بر اساس سن و حذف مقادیر تکراری 
```
#Let's Read csv file
df=pd.read_csv("covid.csv")
#Show records of dataframe
df=df.sort_values( 'age',ascending=False)
df.drop_duplicates(inplace=True)
df
```
![]()

دیتاست حاوی 487 نمونه می باشد.

![](info)

## نرمالسازی 

در ابتدا برای یافتن missing value ،مقادیری که نشان دهنده ی آن در دیتاست هستند(یعنی "-") را به عنوان مقادیر NAN معرفی میکنیم.سپس با کد های زیر بررسی می کنیم که هرستون دارای چه تعداد missing value  است.

in:
```
df.replace('-',np.nan,inplace=True)
df.isnull().sum()
```
out:
```
#                        0
age                    359
Sleep_problems           0
Headache                 1
Diarrhea                 0
Abdominal_pain           0
body_pain                0
Body_discoloration       0
Cough                    0
Fever                    0
Ague                     0
Sore_throat              0
Fatigue                  0
runny_nose               0
Chest_pain               0
Decreased_appetite       0
Vomit                    0
Nausea                   0
Sneezing                 0
Shortness_of_breath      0
Loss_of_smell            0
Loss_of_taste            0
urticaria                0
dtype: int64
```
مطابق کد زیر،برای نرمالسازی دیتاست چون بیشتراز  73 درصد از ستون سن، مقدار گمشده دارد، این  ستون راحذف می کنیم و همچنین سطری که در آن مقدار ستون "سردرد" مقداردهی نشده است نیز حذف می شود
```
df=df.drop(["#","age"],1)
df.dropna(axis=0)
```
![](info2)

## تولید نمونه های با برچسب منفی و تبدیل مقادیر ستون ها به صفر و یک
```
new_df = pd.DataFrame()
for j in df.columns:
    a=list(df[j].copy())
    for i in range(486) :
        if a[i]== 'yes':
            a[i]=1
        else:
            a[i]=0
    new_df[j]=a
l=list(new_df.values)

while len(l)<972:
    row=random.randint(2, size=(21))
    for i in l:
        if list(i)==list(row):
            break
    else:
        l.append(row)
            
        
dataset=np.array(l)
dataset.shape
```
#### اندازه دیتاست جدید
in:
```
target= np.concatenate((np.ones(486), np.zeros(486)))
target.shape
```
out:
```
(972,)
```

بخش داده ها در متغیر dataset و بخش label در متغیر target قرار داده شد.
```
target=new_df.iloc[:,-1].values
dataset=new_df.iloc[:,:-1].values
```
#### مشخص کردن بخش آموزش و تست
```
X_train, X_test, y_train, y_test = train_test_split(dataset, target, test_size=0.1)
```
برای قسمت آموزش از 90 درصد نمونه ها و برای قسمت تست از 10 درصد نمونه ها استفاده می کنیم.
# Logistic Regression Algorithm
```
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
```
### مقادیر accuracy,precision,recall برای الگوریتم logestic regression
in:
```
print('The accuracy of Logistic Regression is: ', (metrics.accuracy_score(y_test, y_pred)))
print('The recall of Logistic Regression is: ', (metrics.recall_score(y_test, y_pred)))
print('The precision of Logistic Regression is: ', (metrics.precision_score(y_test, y_pred)))
```
out:
```
The accuracy of Logistic Regression is:  0.9795918367346939
The recall of Logistic Regression is:   1.0
The precision of Logistic Regression is:  0.9629629629629629
```
## یافتن ویژگی های کم اهمیت
in:
```
importance = logreg.coef_[0]
plt.figure(figsize=(60,15)) 
plt.bar(new_df.columns, importance) 
plt.show()
```
![](Trivial feature)
# KNN Algorithm
```
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

```
### مقادیر accuracy,precision,recall برای الگوریتم KNN
in:
```
knn.score(X_train, y_train)
print('The recall of knn is: ', (metrics.recall_score(y_test, y_pred)))
print('The precision of knn is: ', (metrics.precision_score(y_test, y_pred)))
```
out:
```
0.9496567505720824
The recall of knn is: 1.0
The precision of knn is:  0.8666666666666667
```
### کدهای مربوط به بخش نمودار error rate برحسب k
in:
```
error_rate = []
# Might take some time
for i in range(1,40):
    
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))
    plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
```
out:

![](error rate vs k value giagram)

# DecisionTree Algorithm
in:
```
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
```
out:
```
DecisionTreeClassifier(criterion='entropy', random_state=0)
```
### مقادیر accuracy,precision,recall برای الگوریتم Decosion Tree
in:
```
print('The accuracy of DT is: ', (metrics.accuracy_score(y_test, y_pred)))
print('The recall of DT is: ', (metrics.recall_score(y_test, y_pred)))
print('The Precision of DT is: ', (metrics.precision_score(y_test, y_pred)))
```
out:
```
The accuracy of DT is:  0.9081632653061225
The recall of DT is:  0.9807692307692307
The Precision of DT is:  0.864406779661017

# ID3 Algorithm
```
estimator = Id3Estimator()
estimator.fit(X_train, y_train)
y_pred=estimator.predict(X_test)
```
### مقادیر accuracy,precision,recall برای الگوریتم Decosion Tree
in:
```
print('The accuracy of id3 is: ', (metrics.accuracy_score(y_test, y_pred)))
print('The recall of id3 is: ', (metrics.recall_score(y_test, y_pred)))
print('The Precision of id3 is: ', (metrics.precision_score(y_test, y_pred)))
```
out:
```
The accuracy of id3 is:  0.9285714285714286
The recall of id3 is:  0.9807692307692307
The Precision of id3 is:  0.8947368421052632
```

# Find-S Algorithm
```
def train(c,t):
    for i, val in enumerate(t):
        if val == 1:
            specific_hypothesis = c[i].copy()
            break
             
    for i, val in enumerate(c):
        if t[i] == 1:
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = -1
                else:
                    pass
                 
    return specific_hypothesis
 
#obtaining the final hypothesis
print("n The final hypothesis is:",train(X_train, y_train))
```
out:
```
n The final hypothesis is: [-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1]
```

# Candidate elimination Algorithm
in:
```
from classic_CandidateElimination import Candidate_Elimination
ce = Candidate_Elimination()
ce.fit(X_train, y_train)

```
out:
```
Initial Specific Hypothesis :  [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1]
Initial General Hypothesis :  [['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?']]
Final Specific Hypothesis :  ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
Final General Hypothesis :  [['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?']]
Final Version Space :  [['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?']]
434   440
1
```

```
y_pred=ce.predict(X_test)

```
### مقادیر accuracy,precision,recall برای الگوریتم candidate elimination
```
The accuracy of ce is:  0.46938775510204084
The recall of ce is:  0.0
The Precision of ce is:  0.0
```


# Naive Bayes Algorithm
```
nb = GaussianNB()
nb.fit(X_train, y_train)
print("Naive Bayes test accuracy: ", nb.score(X_test, y_test))
```
### دقت الگوریتم naive bayes
```
Naive Bayes test accuracy:  0.9489795918367347
```
# K-Means Algorithm
```
kmeans = KMeans(n_clusters = 2)
kmeans.fit(dataset)
y_kmeans = kmeans.predict(dataset)
```
