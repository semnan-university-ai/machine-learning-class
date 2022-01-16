
  ## Havva askari
  ## St code : 40011920006
  ## havvaaskari0702@gmail.com
  
  ## Covi-19 Project
  ### ID3
  
  #### Hello everyone. I'm going to test one dataset over ID3 algorithm.Let's see what's going to happen!
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

Splitting our dataset in two part one train and one test:

```
X = full_data
X.shape
```

(786, 22)

```
from sklearn.model_selection import train_test_split

X_train, X_test = train_test_split(X, test_size=0.25)

print("X_train: ",X_train.shape)
print("X_test: ",X_test.shape)
print(X_train)
print(X_test)
```

![id1](https://github.com/semnan-university-ai/machine-learning-class/blob/main/final%20project/Eveaskari/id1.JPG)

Defining our algorithm:
```
#Entropy
def calc_total_entropy(x_train, label, class_list):
    total_row = x_train.shape[0] 
    total_entr = 0
    
    for c in class_list: 
        total_class_count = x_train[x_train[label] == c].shape[0] 
        total_class_entr = - (total_class_count/total_row)*np.log2(total_class_count/total_row) 
        total_entr += total_class_entr 
    
    return total_entr
```

```
#Feature Entropy
def calc_entropy(feature_value_data, label, class_list):
    class_count = feature_value_data.shape[0]
    entropy = 0
    
    for c in class_list:
        label_class_count = feature_value_data[feature_value_data[label] == c].shape[0] 
        entropy_class = 0
        if label_class_count != 0:
            probability_class = label_class_count/class_count 
            entropy_class = - probability_class * np.log2(probability_class)  
        entropy += entropy_class
    return entropy
```
```
    #Gain
def calc_info_gain(feature_name, x_train, label, class_list):
    feature_value_list = x_train[feature_name].unique() 
    total_row = x_train.shape[0]
    feature_info = 0.0
    
    for feature_value in feature_value_list:
        feature_value_data = x_train[x_train[feature_name] == feature_value] 
        feature_value_count = feature_value_data.shape[0]
        feature_value_entropy = calc_entropy(feature_value_data, label, class_list) 
        feature_value_probability = feature_value_count/total_row
        feature_info += feature_value_probability * feature_value_entropy 
        
    return calc_total_entropy(x_train, label, class_list) - feature_info 
```
```
    #High Gain
def find_most_informative_feature(x_train, label, class_list):
    feature_list = x_train.columns.drop(label) 
                                            
    max_info_gain = -1
    max_info_feature = None
    
    for feature in feature_list:  
        feature_info_gain = calc_info_gain(feature, x_train, label, class_list)
        if max_info_gain < feature_info_gain: 
            max_info_gain = feature_info_gain
            max_info_feature = feature
            
    return max_info_feature
```
```
    #SubTree
def generate_sub_tree(feature_name, x_train, label, class_list):
    feature_value_count_dict = x_train[feature_name].value_counts(sort=False) 
    tree = {} 
    
    for feature_value, count in feature_value_count_dict.iteritems():
        feature_value_data = x_train[x_train[feature_name] == feature_value] 
        
        assigned_to_node = False 
        for c in class_list: 
            class_count = feature_value_data[feature_value_data[label] == c].shape[0] 

            if class_count == count: 
                tree[feature_value] = c 
                x_train = x_train[x_train[feature_name] != feature_value] 
                assigned_to_node = True
        if not assigned_to_node: 
            tree[feature_value] = "?" 
            
    return tree, x_train
```
```
    #Tree
def make_tree(root, prev_feature_value, x_train, label, class_list):
    if x_train.shape[0] != 0: 
        max_info_feature = find_most_informative_feature(x_train, label, class_list) 
        tree, x_train = generate_sub_tree(max_info_feature, x_train, label, class_list) 
        next_root = None
        
        if prev_feature_value != None: 
            root[prev_feature_value] = dict()
            root[prev_feature_value][max_info_feature] = tree
            next_root = root[prev_feature_value][max_info_feature]
        else: 
            root[max_info_feature] = tree
            next_root = root[max_info_feature]
        
        for node, branch in list(next_root.items()): 
            if branch == "?": 
                feature_value_data = x_train[x_train[max_info_feature] == node] 
                make_tree(next_root, node, feature_value_data, label, class_list)
```
```
#ID3
def id3(X_train, label):
    x_train = X_train.copy() 
    tree = {} 
    class_list = x_train[label].unique() 
    make_tree(tree, None, X_train, label, class_list) 
    return tree
```
```
#Predict
def predict(tree, instance):
    if not isinstance(tree, dict): 
        return tree 
    else:
        root_node = next(iter(tree)) 
        feature_value = instance[root_node] 
        if feature_value in tree[root_node]: 
            return predict(tree[root_node][feature_value], instance) 
        else:
            return None
```
```
#Evaluate
def evaluate(tree, x_test, label):
    correct_preditct = 0
    wrong_preditct = 0
    for index, row in x_test.iterrows(): 
        result = predict(tree, x_test.iloc[index]) 
        if result == x_test[label].iloc[index]: 
            correct_preditct += 1 
        else:
            wrong_preditct += 1 
    accuracy = correct_preditct / (correct_preditct + wrong_preditct) 
    return accuracy
```
```
#Tree
from pprint import pprint

tree = id3(X_train, 'Covid-19')
pprint(tree)
accuracy = evaluate(tree, X_test, 'Covid-19')
```

```
{'urticaria': {'no': {'Vomit': {'no': {'Abdominal_pain': {'no': {'Body_discoloration': {'no': {'Diarrhea': {'no': {'Chest_pain': {'no': {'Ague': {'no': 'yes',
                                                                                                                                                  'yes': {'runny_nose': {'no': 'yes',
                                                                                                                                                                         'yes': {'Sleep_problems': {'no': 'no',
                                                                                                                                                                                                    'yes': 'yes'}}}}}},
                                                                                                                                  'yes': {'Cough': {'no': {'Loss_of_taste': {'no': {'body_pain': {'no': 'yes',
                                                                                                                                                                                                  'yes': {'Shortness_of_breath': {'no': 'yes',
                                                                                                                                                                                                                                  'yes': 'no'}}}},
                                                                                                                                                                             'yes': 'no'}},
                                                                                                                                                    'yes': {'Headache': {'no': 'yes',
                                                                                                                                                                         'yes': {'Sneezing': {'no': {'Fatigue': {'no': 'no',
                                                                                                                                                                                                                 'yes': {'runny_nose': {'no': 'yes',
                                                                                                                                                                                                                                        'yes': {'Ague': {'no': 'no',
                                                                                                                                                                                                                                                         'yes': 'yes'}}}}}},
                                                                                                                                                                                              'yes': 'yes'}}}}}}}},
                                                                                                            'yes': {'Decreased_appetite': {'no': {'Loss_of_taste': {'no': 'yes',
                                                                                                                                                                    'yes': 'no'}},
                                                                                                                                           'yes': {'body_pain': {'no': 'no',
                                                                                                                                                                 'yes': {'Sore_throat': {'no': 'no',
                                                                                                                                                                                         'yes': {'Loss_of_taste': {'no': 'no',
                                                                                                                                                                                                                   'yes': 'yes'}}}}}}}}}},
                                                                                        'yes': {'Sneezing': {'no': {'Sleep_problems': {'no': {'body_pain': {'no': {'Cough': {'no': 'no',
                                                                                                                                                                             'yes': 'yes'}},
                                                                                                                                                            'yes': {'Nausea': {'no': 'yes',
                                                                                                                                                                               'yes': {'Diarrhea': {'no': 'no',
                                                                                                                                                                                                    'yes': 'yes'}}}}}},
                                                                                                                                       'yes': 'no'}},
                                                                                                             'yes': 'no'}}}},
                                                          'yes': {'Nausea': {'no': {'Ague': {'no': {'Loss_of_smell': {'no': {'Sneezing': {'no': {'Loss_of_taste': {'no': 'yes',
                                                                                                                                                                   'yes': 'no'}},
                                                                                                                                          'yes': {'Diarrhea': {'no': 'no',
                                                                                                                                                               'yes': {'Sleep_problems': {'no': 'yes',
                                                                                                                                                                                          'yes': 'no'}}}}}},
                                                                                                                      'yes': {'Diarrhea': {'no': {'Sleep_problems': {'no': 'no',
                                                                                                                                                                     'yes': 'yes'}},
                                                                                                                                           'yes': 'no'}}}},
                                                                                             'yes': {'Body_discoloration': {'no': {'body_pain': {'no': 'no',
                                                                                                                                                 'yes': {'Sleep_problems': {'no': {'Sore_throat': {'no': 'no',
                                                                                                                                                                                                   'yes': 'yes'}},
                                                                                                                                                                            'yes': 'no'}}}},
                                                                                                                            'yes': 'no'}}}},
                                                                             'yes': {'Ague': {'no': 'no',
                                                                                              'yes': {'Decreased_appetite': {'no': 'no',
                                                                                                                             'yes': {'Diarrhea': {'no': 'yes',
                                                                                                                                                  'yes': 'no'}}}}}}}}}},
                                'yes': {'Cough': {'no': {'Body_discoloration': {'no': {'Shortness_of_breath': {'no': {'Sleep_problems': {'no': {'Decreased_appetite': {'no': {'Abdominal_pain': {'no': {'Fever': {'no': 'yes',
                                                                                                                                                                                                                  'yes': 'no'}},
                                                                                                                                                                                                 'yes': 'no'}},
                                                                                                                                                                       'yes': 'yes'}},
                                                                                                                                         'yes': {'Abdominal_pain': {'no': 'no',
                                                                                                                                                                    'yes': 'yes'}}}},
                                                                                                               'yes': {'Abdominal_pain': {'no': 'no',
                                                                                                                                          'yes': {'Sneezing': {'no': 'yes',
                                                                                                                                                               'yes': 'no'}}}}}},
                                                                                'yes': {'body_pain': {'no': 'no',
                                                                                                      'yes': {'Ague': {'no': 'no',
                                                                                                                       'yes': {'Abdominal_pain': {'no': 'no',
                                                                                                                                                  'yes': {'Sleep_problems': {'no': 'no',
                                                                                                                                                                             'yes': 'yes'}}}}}}}}}},
                                                  'yes': 'no'}}}},
               'yes': {'Cough': {'no': 'no',
                                 'yes': {'Fever': {'no': 'no',
                                                   'yes': {'Decreased_appetite': {'no': {'Diarrhea': {'no': {'Headache': {'no': {'Body_discoloration': {'no': 'yes',
                                                                                                                                                        'yes': 'no'}},
                                                                                                                          'yes': 'no'}},
                                                                                                      'yes': 'no'}},
                                                                                  'yes': {'body_pain': {'no': 'no',
                                                                                                        'yes': {'Headache': {'no': {'Sleep_problems': {'no': {'Body_discoloration': {'no': 'yes',
                                                                                                                                                                                     'yes': 'no'}},
                                                                                                                                                       'yes': 'no'}},
                                                                                                                             'yes': {'Sleep_problems': {'no': 'no',
                                                                                                                                                        'yes': {'Fatigue': {'no': {'Shortness_of_breath': {'no': 'yes',
                                                                                                                                                                                                           'yes': 'no'}},
                                                                                                                                                                            'yes': 'yes'}}}}}}}}}}}}}}}}

```
