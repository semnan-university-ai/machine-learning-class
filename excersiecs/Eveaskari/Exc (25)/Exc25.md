<div dir="rtl">
  
  ###  با کمک توابع رندوم در یک زبان برنامه نویسی روی یک صفحه ی مختصات دوبعدی 100 نقطه با x و yهای رندوم در بازه ی 1 تا 50 بدست آورید و برنامه ای بنویسید که k=3 را نسبت به 43 یا چهل و سومین نقطه ی تولید شده ی شما دارد.
  
  </div>
  <br/>
  
  ```
  import pandas as pd
import numpy
from numpy import random
import sklearn.metrics as met
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

#selecting dataset

x = random.randint(50, size=(1, 100))
y = random.randint(50, size=(1, 100))

arr = numpy.dstack((x, y))

print(arr)

plt.style.use('ggplot')
plt.scatter(x, y, c = 'r', s = 9, label = 'Data')
plt.scatter(x, y, c = 'b', s = 50, label = 'Center', marker = '*')
plt.title('Scatter Plot of Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

#K-nn for point 43

z = train_test_split(x, y, random_state=43)


knn = KNeighborsClassifier(n_neighbors=3, weights='uniform',
                           algorithm='auto', metric='euclidean')
knn.fit(x, y)
y_pred_knn = knn.predict(z)
  ```
  <br/>
  
  <div dir="">
  
  <br/>
  
  ![3-nn-43](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(25)/knn43.JPG)
  
  <br/>
  
  <br/>
  
  </div>
