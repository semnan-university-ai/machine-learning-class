
با سلام

لینک پروژه در سایت:https://www.kaggle.com/viemnileg/notebook055ac4525b

فقط به دلیل نابلد بودن در محیط موفق به نامگزاری درست نشدم

منابع برای کد زنی پایین صفحه



داده را خوانده و مقادیر را به مقدار 0 و 1 تبدیل کرده سپس داده را مرتب میکنیم
```
%matplotlib inline
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler(feature_range =(0,100))
from itertools import product

data = pd.read_json('/kaggle/input/covid-patient-datasets/covid.json')

data.head()
data.isnull().sum()
data=data.replace(['yes', 'Yes','No','no',''], 
                     ['1', '1','0','0','0']) 


data.sort_values("age", axis = 0, ascending = False,
                inplace = True, na_position ='last')
data
```
![1](https://user-images.githubusercontent.com/94211519/149675695-0b2f947b-5215-4ea8-be8e-f801241c7125.PNG)




بررسی اینکه آیا داده مقدار خالی دارد
```
data.isnull().sum()
```
![2](https://user-images.githubusercontent.com/94211519/149675704-76f74382-6125-4452-a14b-4a6bfc472dfe.PNG)




حذف ردیف هایی که مقدار خالی دارند
```
data = data.dropna()
data
```
![3](https://user-images.githubusercontent.com/94211519/149675708-564ee7c9-7dc8-403a-adf7-4a27481fcd31.PNG)




اضافه کردن کلاس به مقدار 1
```
data['result']=1
data
```
![4](https://user-images.githubusercontent.com/94211519/149675717-6edb3f44-306a-4b79-96bc-de6d685305d8.PNG)



نرمالیزه کردن مقدار ویژگی ها
```
for i in data.columns:
  if(i=='age'or i=='#'):
    continue
  data[i]=encoder.fit_transform(data[i])
data
```
![5](https://user-images.githubusercontent.com/94211519/149675729-6eb1d222-ec63-4f03-8525-a86fbc70fd06.PNG)



ساخت تمام داده های موجود و دادن کلاس 0 به آن
```
from itertools import product


Sleep_problems=['yes','no']
Headache=['yes','no']
Diarrhea=['yes','no']
Abdominal_pain=['yes','no']
body_pain=['yes','no']
Body_discoloration=['yes','no']
Cough=['yes','no']
Fever=['yes','no']
Ague=['yes','no']
Sore_throat=['yes','no']
Fatigue=['yes','no']
runny_nose=['yes','no']
Chest_pain=['yes','no']
Decreased_appetite=['yes','no']
Vomit=['yes','no']
nausea=['yes','no']
Sneezing=['yes','no']
Shortness_of_breath=['yes','no']
Loss_of_smell=['yes','no']
Loss_of_taste=['yes','no']
urticaria=['yes','no']

result1 = pd.DataFrame(product(Sleep_problems,Headache, Diarrhea, Abdominal_pain,body_pain, Body_discoloration,
                              Cough,    Fever, Ague, Sore_throat, Fatigue, runny_nose, Chest_pain, Decreased_appetite,Vomit, 
                              nausea,Sneezing, Shortness_of_breath, Loss_of_smell, Loss_of_taste,  urticaria), columns=['Sleep_problems','Headache', 'Diarrhea', 'Abdominal_pain',
                 'body_pain', 'Body_discoloration', 'Cough',    'Fever', 'Ague', 
                  'Sore_throat', 'Fatigue', 'runny_nose', 'Chest_pain', 'Decreased_appetite',
                  'Vomit'  , 'nausea',    'Sneezing', 'Shortness_of_breath', 'Loss_of_smell', 
                  'Loss_of_taste',  'urticaria'])

result1['result']='no'
result1
```
![5](https://user-images.githubusercontent.com/94211519/149675762-93ca4ac5-1783-48b7-9e71-59349f770f8a.PNG)



اجرای الگوریتم FS
```
def train(c,t):
    for i, val in enumerate(t):
        if val == 0:
            specific_hypothesis = c[i].copy()
            break
             
    for i, val in enumerate(c):
        if t[i] == 0:
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
                 
    return specific_hypothesis
    
    d = np.array(data)[:,0:21]
target = np.array(data)[:,22]
print("n The final hypothesis is:",train(d,target))
```
![6](https://user-images.githubusercontent.com/94211519/149675767-f529b823-da3a-4960-8a55-cf7d66bae353.PNG)
 
   
   
   اجرای الگوریتم CE
```
def learn(concepts, target): 
    specific_h = concepts[0].copy()
    print("\nInitialization of specific_h and genearal_h")
    print("\nSpecific Boundary: ", specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("\nGeneric Boundary: ",general_h)  

    for i, h in enumerate(concepts):
        print("\nInstance", i+1 , "is ", h)
        if target[i] == 0:
            print("Instance is Positive ")
            for x in range(len(specific_h)): 
                if h[x]!= specific_h[x]:                    
                    specific_h[x] ='?'                     
                    general_h[x][x] ='?'
                   
        if target[i] == 1:            
            print("Instance is Negative ")
            for x in range(len(specific_h)): 
                if h[x]!= specific_h[x]:                    
                    general_h[x][x] = specific_h[x]                
                else:                    
                    general_h[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", specific_h)         
        print("Generic Boundary after ", i+1, "Instance is ", general_h)
        print("\n")

    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:   
        general_h.remove(['?', '?', '?', '?', '?', '?']) 
    return specific_h, general_h 
    
    concepts = np.array(data.iloc[:,0:22])

target = np.array(data.iloc[:,22])

s_final, g_final = learn(concepts, target)

print("Final Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")

```
![7](https://user-images.githubusercontent.com/94211519/149675768-d03baeee-b71c-401d-9f68-8224ffd008cc.PNG)




اجرای الگوریتم NB
```

data.drop('#', axis=1, inplace=True)
data.drop('age', axis=1, inplace=True)
X = data.iloc[:,0:-1].values
y = data.iloc[:,-1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
ac = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test, y_pred)
print(ac)
```

اجرای الگوریتم KNN
```
X = data.iloc[:, 0:21].values
y = data.iloc[:, 21].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```
![8](https://user-images.githubusercontent.com/94211519/149675777-1f71ba9f-a96e-45a5-989a-1f2279965d35.PNG)



اجرای DT
```
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
  
# Function importing Dataset
def importdata():
    balance_data = pd.read_json('/kaggle/input/covid-patient-datasets/covid.json')
    balance_data['result']=1
    balance_data.drop('#', axis=1, inplace=True)
    balance_data.drop('age', axis=1, inplace=True)
    for i in balance_data.columns:
      if(i=='age'or i=='#'):
        continue
      balance_data[i]=encoder.fit_transform(balance_data[i])
    # Printing the dataswet shape
    print ("Dataset Length: ", len(balance_data))
    print ("Dataset Shape: ", balance_data.shape)
      
    # Printing the dataset obseravtions
    print ("Dataset: ",balance_data.head())
    return balance_data
  
# Function to split the dataset
def splitdataset(balance_data):
  
    # Separating the target variable
    X = balance_data.values[:, 0:20]
    Y = balance_data.values[:,21 ]
  
    # Splitting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split( 
    X, Y, test_size = 0.3, random_state = 100)
      
    return X, Y, X_train, X_test, y_train, y_test
      
# Function to perform training with giniIndex.
def train_using_gini(X_train, X_test, y_train):
  
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion = "gini",
            random_state = 100,max_depth=3, min_samples_leaf=5)
  
    # Performing training
    clf_gini.fit(X_train, y_train)
    return clf_gini
      
# Function to perform training with entropy.
def tarin_using_entropy(X_train, X_test, y_train):
  
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
            criterion = "entropy", random_state = 100,
            max_depth = 3, min_samples_leaf = 5)
  
    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy
  
  
# Function to make predictions
def prediction(X_test, clf_object):
  
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred
      
# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
      
    print ("Accuracy : ",
    accuracy_score(y_test,y_pred)*100)
      
    print("Report : ",
    classification_report(y_test, y_pred))
  
# Driver code
def main():
      
    # Building Phase
    data = importdata()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    clf_gini = train_using_gini(X_train, X_test, y_train)
    clf_entropy = tarin_using_entropy(X_train, X_test, y_train)
      
    # Operational Phase
    print("Results Using Gini Index:")
      
    # Prediction using gini
    y_pred_gini = prediction(X_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)
      
    print("Results Using Entropy:")
    # Prediction using entropy
    y_pred_entropy = prediction(X_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)
      
      
# Calling main function
if __name__=="__main__":
    main()

```
![9](https://user-images.githubusercontent.com/94211519/149675820-fd931ad8-4e9c-4322-8953-122b9f4c8423.PNG)




اجرای ID3
```
data1 = pd.read_json('/kaggle/input/covid-patient-datasets/covid.json')


data1.drop('#', axis=1, inplace=True)
data1.drop('age', axis=1, inplace=True)
data1 = data1.dropna()
data1['result1']=1
dict1 = {'Sleep_problems':'no','Headache':'no', 'Diarrhea':'no', 'Abdominal_pain':'no',
                 'body_pain':'no', 'Body_discoloration':'no', 'Cough':'no',    'Fever':'no', 'Ague':'no', 
                  'Sore_throat':'no', 'Fatigue':'no', 'runny_nose':'no', 'Chest_pain':'no', 'Decreased_appetite':'no',
                  'Vomit':'no'  , 'nausea':'no',    'Sneezing':'no', 'Shortness_of_breath':'no', 'Loss_of_smell':'no', 
                  'Loss_of_taste':'no',  'urticaria':'no','result1':0}
data1 = data1.append(dict1, ignore_index = True)
def entropy(probs):  
    import math
    return sum( [-prob*math.log(prob, 2) for prob in probs] )

#Function to calulate the entropy of the given Data Sets/List with respect to target attributes
def entropy_of_list(a_list):  
    #print("A-list",a_list)
    from collections import Counter
    cnt = Counter(x for x in a_list)   # Counter calculates the propotion of class
   # print("\nClasses:",cnt)
    #print("No and Yes Classes:",a_list.name,cnt)
    num_instances = len(a_list)*1.0   # = 14
    print("\n Number of Instances of the Current Sub Class is {0}:".format(num_instances ))
    probs = [x / num_instances for x in cnt.values()]  # x means no of YES/NO
    print("\n Classes:",min(cnt),max(cnt))
    print(" \n Probabilities of Class {0} is {1}:".format(min(cnt),min(probs)))
    print(" \n Probabilities of Class {0} is {1}:".format(max(cnt),max(probs)))
    return entropy(probs) # Call Entropy :


total_entropy = entropy_of_list(data['result1'])

def information_gain(df, split_attribute_name, target_attribute_name, trace=0):
    print("Information Gain Calculation of ",split_attribute_name)
    '''
    Takes a DataFrame of attributes, and quantifies the entropy of a target
    attribute after performing a split along the values of another attribute.
    '''
    # Split Data by Possible Vals of Attribute:
    df_split = df.groupby(split_attribute_name)
   # for name,group in df_split:
    #    print("Name:\n",name)
     #   print("Group:\n",group)
    
    # Calculate Entropy for Target Attribute, as well as
    # Proportion of Obs in Each Data-Split
    nobs = len(df.index) * 1.0
   # print("NOBS",nobs)
    df_agg_ent = df_split.agg({target_attribute_name : [entropy_of_list, lambda x: len(x)/nobs] })[target_attribute_name]
    #print([target_attribute_name])
    #print(" Entropy List ",entropy_of_list)
    #print("DFAGGENT",df_agg_ent)
    df_agg_ent.columns = ['Entropy', 'PropObservations']
    #if trace: # helps understand what fxn is doing:
     #   print(df_agg_ent)
    
    # Calculate Information Gain:
    new_entropy = sum( df_agg_ent['Entropy'] * df_agg_ent['PropObservations'] )
    old_entropy = entropy_of_list(df[target_attribute_name])
    return old_entropy - new_entropy

def id3(df, target_attribute_name, attribute_names, default_class=None):
    
    ## Tally target attribute:
    from collections import Counter
    cnt = Counter(x for x in df[target_attribute_name])# class of YES /NO
    
    ## First check: Is this split of the dataset homogeneous?
    if len(cnt) == 1:
        return next(iter(cnt))  # next input data set, or raises StopIteration when EOF is hit.
    
    ## Second check: Is this split of the dataset empty?
    # if yes, return a default value
    elif df.empty or (not attribute_names):
        return default_class  # Return None for Empty Data Set
    
    ## Otherwise: This dataset is ready to be devied up!
    else:
        # Get Default Value for next recursive call of this function:
        default_class = max(cnt.keys()) #No of YES and NO Class
        # Compute the Information Gain of the attributes:
        gainz = [information_gain(df, attr, target_attribute_name) for attr in attribute_names] #
        index_of_max = gainz.index(max(gainz)) # Index of Best Attribute
        # Choose Best Attribute to split on:
        best_attr = attribute_names[index_of_max]
        
        # Create an empty tree, to be populated in a moment
        tree = {best_attr:{}} # Iniiate the tree with best attribute as a node 
        remaining_attribute_names = [i for i in attribute_names if i != best_attr]
        
        # Split dataset
        # On each split, recursively call this algorithm.
        # populate the empty tree with subtrees, which
        # are the result of the recursive call
        for attr_val, data_subset in df.groupby(best_attr):
            subtree = id3(data_subset,
                        target_attribute_name,
                        remaining_attribute_names,
                        default_class)
            tree[best_attr][attr_val] = subtree
        return tree

# Get Predictor Names (all but 'class')
attribute_names = list(data.columns)
print("List of Attributes:", attribute_names) 
attribute_names.remove('result1') #Remove the class attribute 
print("Predicting Attributes:", attribute_names)

from pprint import pprint
tree = id3(data,'result1',attribute_names)
print("\n\nThe Resultant Decision Tree is :\n")
#print(tree)
pprint(tree)
attribute = next(iter(tree))
print("Best Attribute :\n",attribute)
print("Tree Keys:\n",tree[attribute].keys())
```


منابع:
https://stackoverflow.com/questions/60025324/creating-all-possible-combinations-of-rows-in-dataframe-in-python
https://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python
https://stackoverflow.com/questions/46432681/how-to-select-best-worst-features-in-dataset-for-classification/46439107
https://stackoverflow.com/questions/42196589/any-way-to-get-mappings-of-a-label-encoder-in-python-pandas
https://stackoverflow.com/questions/56121561/pythons-json-attributeerror-str-object-has-no-attribute-keys
https://www.edureka.co/blog/find-s-algorithm-in-machine-learning/
https://www.vtupulse.com/machine-learning/candidate-elimination-algorithm-in-python/
https://www.programmerall.com/article/45071136945/
https://sefiks.com/2017/11/20/a-step-by-step-id3-decision-tree-example/
https://www.geeksforgeeks.org/decision-tree-implementation-python/
https://scikit-learn.org/stable/modules/tree.html
https://www.analyticsvidhya.com/blog/2021/01/a-guide-to-the-naive-bayes-algorithm/
https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
and ........


