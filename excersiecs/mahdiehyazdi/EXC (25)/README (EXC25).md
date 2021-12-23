### با کمک توابع رندوم در یک زبان برنامه نویسی روی یک صفحه ی مختصات دوبعدی 100 نقطه با x و yهای رندوم در بازه ی 1 تا 50 بدست آورید و برنامه ای بنویسید که k=3 را نسبت به 43 یا چهل و سومین نقطه ی تولید شده ی شما دارد.

<br/>

```
import random
import numpy as np
from tabulate import tabulate
from scipy.spatial import distance
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
 
list1 =[]

for i in range(0, 100):
    list1.append(random.randint(1, 50))
    
index = list(range(0, 100))
head = ["i", "list1"]
mydata = zip(index, list1[42])
print(tabulate(mydata, headers=head, tablefmt="grid"))

X_train, X_test, y_train, y_test = train_test_split(
             list1[42], list1[45], test_size = 0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))


# euclidean distance Method one
print(np.linalg.norm(list1[42] - list1[45]))
# euclidean distance Method two
print(distance.euclidean(list1[42], list1[42:45]))


```
