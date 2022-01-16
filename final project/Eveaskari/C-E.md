
  ## Havva askari
  ## St code : 40011920006
  ## havvaaskari0702@gmail.com
  
  ## Covi-19 Project
  ### Candidat-Elimination
  
  #### Hello everyone. I'm going to test one dataset over some algorithms.Let's see what's going to happen!
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

Now were giving our dataset our labeles,But we change values to "yes, no" again!:

```
full_data = full_data.rename(columns = {"_merge":"Covid-19"})
full_data.replace(('left_only', 'both', 'right_only'), ('yes', 'yes', 'no'), inplace=True)
full_data.replace((1, 0), ('yes', 'no'), inplace=True)
full_data.head(1000)
```

![f7](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/f7.JPG)

Now for doing the find-s algorithm we should change our dataframe to array! :

```
full_data.to_numpy
print(full_data)
```

![f8](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/f8.JPG)

Splitting our dataset in two part one features and one concept:

```
atrbt = np.array(full_data)[:, :-1]
print("my attributes are:", atrbt)
```

![f9](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/f9.JPG)

```
cncpt = np.array(full_data)[:, -1]
print("my concept is:", cncpt)
```

![f10](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/f10.JPG)

Defining our algorithm:
```
def learn(atr, cpt): 
    specific_h = atrbt[0].copy()
    print("\nInitialization of specific_h and genearal_h")
    print("\nSpecific Boundary: ", specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("\nGeneric Boundary: ",general_h)  

    for i, h in enumerate(atrbt):
        print("\nInstance", i+1 , "is ", h)
        if cncpt[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(specific_h)): 
                if h[x]!= specific_h[x]:                    
                    specific_h[x] ='?'                     
                    general_h[x][x] ='?'
                   
        if cncpt[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(specific_h)): 
                if h[x]!= specific_h[x]:                    
                    general_h[x][x] = specific_h[x]                
                else:                    
                    general_h[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", specific_h)         
        print("Generic Boundary after ", i+1, "Instance is ", general_h)
        print("\n")

    idxs = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in idxs:   
        general_h.remove(['?', '?', '?', '?', '?', '?']) 
    return specific_h, general_h 

S_final, G_final = learn(atrbt, cncpt)

print("Final Specific_h: ", S_final, sep="\n")
print("Final General_h: ", G_final, sep="\n")
```

![ce1](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/C-E1.JPG)

```
Final Specific_h: 
['?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?'
 '?' '?' '?']
Final General_h: 
[['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?']]
```
