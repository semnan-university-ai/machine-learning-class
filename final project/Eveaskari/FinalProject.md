
  ## Havva askari
  ## St code : 40011920006
  ## havvaaskari0702@gmail.com
  
  ## Covi-19 Project
  
  ### Hello everyone. I'm going to test one dataset over some algorithms.Let's see what's going to happen!
  first of all i'm going to import my dataset from my google drive:
  ```
  from google.colab import drive
  drive.mount ('/content/gdrive')
  ```
  ![gdrive](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/1.JPG)
  
  Now that we have our drive we can upload our dataset and importing libraries thas we need:
  ```
import numpy as np
import pandas as pd
import json as js

data = pd.read_json('/content/gdrive/MyDrive/Covid_Project/covid.json')
data.head()
```
I used data.head() to see what my dataset is:

![2](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/2.JPG)

And now i chech how many rows and columns do i have:

```
data.info()
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 487 entries, 0 to 486
Data columns (total 23 columns):
 #   Column               Non-Null Count  Dtype 
---  ------               --------------  ----- 
 0   #                    487 non-null    int64 
 1   age                  487 non-null    object
 2   Sleep_problems       487 non-null    object
 3   Headache             487 non-null    object
 4   Diarrhea             487 non-null    object
 5   Abdominal_pain       487 non-null    object
 6   body_pain            487 non-null    object
 7   Body_discoloration   487 non-null    object
 8   Cough                487 non-null    object
 9   Fever                487 non-null    object
 10  Ague                 487 non-null    object
 11  Sore_throat          487 non-null    object
 12  Fatigue              487 non-null    object
 13  runny_nose           487 non-null    object
 14  Chest_pain           487 non-null    object
 15  Decreased_appetite   487 non-null    object
 16  Vomit                487 non-null    object
 17  Nausea               487 non-null    object
 18  Sneezing             487 non-null    object
 19  Shortness_of_breath  487 non-null    object
 20  Loss_of_smell        487 non-null    object
 21  Loss_of_taste        487 non-null    object
 22  urticaria            487 non-null    object
dtypes: int64(1), object(22)
memory usage: 87.6+ KB
```
Next step is up to you!I didnt want to use age featur and indeces!

```
del data["#"]
del data["age"]
data.head()
```
![3](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/3.JPG)

Now we change our values to 0,1 to have easy normalization!

```
import sklearn
from sklearn import preprocessing

data.replace(('yes', 'no'), (1, 0), inplace=True)
data.replace(('Yes', 'No'), (1, 0), inplace=True)
data.replace('es', 1, inplace=True)
data.head()
```

![4](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/4.JPG)

Making another dataset by random selection for our "No" class:

```
from numpy import random

data_no = np.random.randint(2, size=(500,21))
no_data = pd.DataFrame(data_no, columns=('Sleep_problems', 'Headache', 'Diarrhea', 'Abdominal_pain',
                                              'body_pain', 'Body_discoloration',
                                              'Cough', 'Fever', 'Ague', 'Sore_throat',
                                              'Fatigue', 'runny_nose', 'Chest_pain',
                                              'Decreased_appetite', 'Vomit', 'Nausea',
                                              'Sneezing', 'Shortness_of_breath',
                                              'Loss_of_smell', 'Loss_of_taste', 'urticaria'))
no_data.head(500)
```

![5](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/5.JPG)

Merging our datasets to set a new dataset inclouding "yes,no" classes:

```
full_data = data.merge(no_data, indicator=True, how='outer')
full_data.head(1000)
```

![6](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/6.JPG)

Now were giving our dataset our labeles:

```
full_data = full_data.rename(columns = {"_merge":"Covid-19"})
full_data.replace(('left_only','both', 'right_only'), (1, 1, 0), inplace=True)
full_data.head(1000)
```

![7](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/7.JPG)

Splitting our dataset in two part for features and concept:

```
y = full_data['Covid-19'].values
y = y.reshape(-1,1)
X = full_data.drop(['Covid-19'],axis = 1)
X.shape
```

(987, 21)

Normalizing our dataset:

```
normal_data = preprocessing.normalize(full_data)
eve_covid = pd.DataFrame(normal_data, columns=('Sleep_problem', 'Headache', 'Diarrhea', 'Abdominal_pain',
                                              'body_pain', 'Body_discoloration',
                                              'Cough', 'Fever', 'Ague', 'Sore_throat',
                                              'Fatigue', 'runny_nose', 'Chest_pain',
                                              'Decreased_appetite', 'Vomit', 'Nausea',
                                              'Sneezing', 'Shortness_of_breath',
                                              'Loss_of_smell', 'Loss_of_taste', 'urticaria', 'Covid-19'))
eve_covid.head()
```

![8](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/8.JPG)

Sorting our dataset by our class:
Removing all of our duplicate rows:

```
eve_covid.sort_values('Covid-19')
eve_covid.drop_duplicates(keep='first', inplace=True)
eve_covid.info()
```

```
<class 'pandas.core.frame.DataFrame'>
Int64Index: 786 entries, 0 to 986
Data columns (total 22 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   Sleep_problem        786 non-null    float64
 1   Headache             786 non-null    float64
 2   Diarrhea             786 non-null    float64
 3   Abdominal_pain       786 non-null    float64
 4   body_pain            786 non-null    float64
 5   Body_discoloration   786 non-null    float64
 6   Cough                786 non-null    float64
 7   Fever                786 non-null    float64
 8   Ague                 786 non-null    float64
 9   Sore_throat          786 non-null    float64
 10  Fatigue              786 non-null    float64
 11  runny_nose           786 non-null    float64
 12  Chest_pain           786 non-null    float64
 13  Decreased_appetite   786 non-null    float64
 14  Vomit                786 non-null    float64
 15  Nausea               786 non-null    float64
 16  Sneezing             786 non-null    float64
 17  Shortness_of_breath  786 non-null    float64
 18  Loss_of_smell        786 non-null    float64
 19  Loss_of_taste        786 non-null    float64
 20  urticaria            786 non-null    float64
 21  Covid-19             786 non-null    float64
dtypes: float64(22)
memory usage: 141.2 KB
```

As we can see our rows reduced from 986 to 786. Its means that we had 200 duplicate rows!<br/>
<br/>
Finding the less important feature in dataset <br/>
Now we're gonna find 5 feature that are less important in our dataset . actually for doing that i'm gonna find my other best features!

```
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

X_new = SelectKBest(chi2, k=16).fit_transform(X, y)
X_new.shape
```
(786, 16)

we pick 75% of our data for making our hypothesis and the other 25% is for testing our work to find out how much accuracy we have!

```
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=50)

y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

print("X_train: ",X_train.shape)
print("X_test: ",X_test.shape)
print("y_train: ",y_train.shape)
print("y_test: ",y_test.shape)
```

X_train:  (589, 21) <br/>
X_test:  (197, 21) <br/>
y_train:  (589, 1) <br/>
y_test:  (197, 1) <br/>

### Now let's do the magic!
we're going to use different algorithm on our data set...

### Naive Bayes
Let's see what this algorithm does!

```
from sklearn.naive_bayes import GaussianNB
NB_rslt = GaussianNB()
NB_rslt.fit(X_train, y_train.ravel())
print("Naive Bayes Algorithm Test Accuracy: ", NB_rslt.score(X_test, y_test))
```

#### Naive Bayes Algorithm Test Accuracy:  0.902834008097166

### K-NN

```
from sklearn.neighbors import KNeighborsClassifier
K = 3
eve_kneighbor = KNeighborsClassifier(n_neighbors=K)
eve_kneighbor.fit(X_train, y_train.ravel())
print(" K-NN Algorithm Test Accuracy For k = {} Is : {}".format(K, eve_kneighbor.score(X_test, y_test)))
print("K-NN Algorithm Train Accuracy For k = {} Is : {}".format(K, eve_kneighbor.score(X_train, y_train)))
```

#### K-NN Algorithm Test Accuracy For k = 3 Is : 0.9271255060728745
#### K-NN Algorithm Train Accuracy For k = 3 Is : 0.9378378378378378

### Decision Tree

```
from sklearn.tree import DecisionTreeClassifier
eve_tree = DecisionTreeClassifier()
eve_tree.fit(X_train, y_train.ravel())
print("Decision Tree Algorithm Test Accuracy: ", eve_tree.score(X_test, y_test))
```
#### Decision Tree Algorithm Test Accuracy:  0.8987854251012146

### KMeans

```
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0)

kmeans.fit(X_train, y_train.ravel())
print("KMeans Algorithm Test Accuracy: ", kmeans.score(X_test, y_test))
kmeans.cluster_centers_
```
```
#### KMeans Algorithm Test Accuracy:  -1016.7373300215618
array([[0.51139241, 0.53417722, 0.46582278, 0.47088608, 0.59240506,
        0.49367089, 0.51392405, 0.58227848, 0.53417722, 0.53924051,
        0.53164557, 0.54177215, 0.5443038 , 0.53417722, 0.48101266,
        0.50886076, 0.51139241, 0.57468354, 0.56202532, 0.53924051,
        0.45822785],
       [0.06086957, 0.35072464, 0.17101449, 0.04927536, 0.3884058 ,
        0.03768116, 0.42898551, 0.55072464, 0.02898551, 0.22028986,
        0.40289855, 0.15652174, 0.05507246, 0.14202899, 0.03188406,
        0.09565217, 0.02608696, 0.27826087, 0.13623188, 0.06086957,
```
