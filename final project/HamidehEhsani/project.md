# Covid dataset

حمیده احسانی

شماره دانشجویی: 9911624001

## بخش import کردن کتابخانه های مورد نیاز

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
```

## خواندن از فایل و نمایش اطلاعات 
```
#Let's Read csv file
df=pd.read_csv("covid.csv")
#Show records of dataframe
df
```
![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/HamidehEhsani/namayesh%20etelaat%20dataset.PNG)

دیتاست حاوی 487 نمونه می باشد.

![](info)

## مرتب سازی بر اساس سن


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

### برچسب دادن به نمونه ها
نمونه های موجود در دیتاست کویید به عنوان داده های مثبت در نظر گرفته شده اند و نمونه های منفی به طور تصادفی ایجاد شده اند

in:
```
new_df["target"]=[1 for i in range(487)]+[0 for i in range(487)]
new_df.iloc[:,-1]
```
out:
```0      1
1      1
2      1
3      1
4      1
      ..
969    0
970    0
971    0
972    0
973    0
Name: target, Length: 974, dtype: int64
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
The accuracy of Logistic Regression is:  0.9897959183673469
The recall of Logistic Regression is:  0.9807692307692307
The precision of Logistic Regression is:  1.0
```
## یافتن ویژگی های کم اهمیت
in:
```
importance = logreg.coef_[0]
plt.bar([x for x in range(len(importance))], importance)
plt.show()
```
![](Trivial feature)
# KNN Algorithm
```

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
0.9920091324200914
The recall of knn is:  0.9807692307692307
The precision of knn is:  0.9807692307692307
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
The accuracy of DT is:  0.9795918367346939
The recall of DT is:  0.9807692307692307
The Precision of DT is:  0.9807692307692307
```
# ID3 Algorithm


# Find-S Algorithm

# Candidate elimination Algorithm


# Naive Bayes Algorithm


# K-Means Algorithm
