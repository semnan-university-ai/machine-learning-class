```
#1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

sns.set_style("darkgrid")

```
<br/>

```
#2
data = pd.read_excel('ccovid.xlsx')
data.drop(396, axis=0 , inplace= True)
data.drop(['#' , 'age'], axis=1 , inplace= True)


from operator import le

l1 = LabelEncoder()
label = l1.fit_transform(data['Sleep_problems'])
new_data = data
data = new_data.drop('Sleep_problems' , axis='columns')
data['Sleep_problems'] = label

l2 = LabelEncoder()
label = l2.fit_transform(data['Headache'])
new_data = data
data = new_data.drop('Headache' , axis='columns')
data['Headache'] = label

l3 = LabelEncoder()
label = l3.fit_transform(data['Diarrhea'])
new_data = data
data = new_data.drop('Diarrhea' , axis='columns')
data['Diarrhea'] = label

l4 = LabelEncoder()
label = l4.fit_transform(data['Abdominal_pain'])
new_data = data
data = new_data.drop('Abdominal_pain' , axis='columns')
data['Abdominal_pain'] = label

l5 = LabelEncoder()
label = l5.fit_transform(data['Diarrhea'])
new_data = data
data = new_data.drop('Diarrhea' , axis='columns')
data['Diarrhea'] = label

l6 = LabelEncoder()
label = l6.fit_transform(data['body_pain'])
new_data = data
data = new_data.drop('body_pain' , axis='columns')
data['body_pain'] = label

l7 = LabelEncoder()
label = l7.fit_transform(data['Body_discoloration'])
new_data = data
data = new_data.drop('Body_discoloration' , axis='columns')
data['Body_discoloration'] = label

l8 = LabelEncoder()
label = l8.fit_transform(data['Cough'])
new_data = data
data = new_data.drop('Cough' , axis='columns')
data['Cough'] = label

l9 = LabelEncoder()
label = l9.fit_transform(data['Fever'])
new_data = data
data = new_data.drop('Fever' , axis='columns')
data['Fever'] = label

l10 = LabelEncoder()
label = l10.fit_transform(data['Ague'])
new_data = data
data = new_data.drop('Ague' , axis='columns')
data['Ague'] = label

l11 = LabelEncoder()
label = l11.fit_transform(data['Loss_of_taste'])
new_data = data
data = new_data.drop('Loss_of_taste' , axis='columns')
data['Loss_of_taste'] = label

l12 = LabelEncoder()
label = l12.fit_transform(data['Sore_throat'])
new_data = data
data = new_data.drop('Sore_throat' , axis='columns')
data['Sore_throat'] = label

l13 = LabelEncoder()
label = l13.fit_transform(data['Fatigue'])
new_data = data
data = new_data.drop('Fatigue' , axis='columns')
data['Fatigue'] = label

l14 = LabelEncoder()
label = l14.fit_transform(data['runny_nose'])
new_data = data
data = new_data.drop('runny_nose' , axis='columns')
data['runny_nose'] = label

l15 = LabelEncoder()
label = l15.fit_transform(data['Chest_pain'])
new_data = data
data = new_data.drop('Chest_pain' , axis='columns')
data['Chest_pain'] = label

l16 = LabelEncoder()
label = l16.fit_transform(data['Decreased_appetite'])
new_data = data
data = new_data.drop('Decreased_appetite' , axis='columns')
data['Decreased_appetite'] = label

l17 = LabelEncoder()
label = l17.fit_transform(data['Vomit'])
new_data = data
data = new_data.drop('Vomit' , axis='columns')
data['Vomit'] = label

l18 = LabelEncoder()
label = l18.fit_transform(data['Nausea'])
new_data = data
data = new_data.drop('Nausea' , axis='columns')
data['Nausea'] = label

l19 = LabelEncoder()
label = l19.fit_transform(data['Sneezing'])
new_data = data
data = new_data.drop('Sneezing' , axis='columns')
data['Sneezing'] = label

l20 = LabelEncoder()
label = l20.fit_transform(data['Shortness_of_breath'])
new_data = data
data = new_data.drop('Shortness_of_breath' , axis='columns')
data['Shortness_of_breath'] = label

l21 = LabelEncoder()
label = l21.fit_transform(data['Loss_of_smell'])
new_data = data
data = new_data.drop('Loss_of_smell' , axis='columns')
data['Loss_of_smell'] = label

l22 = LabelEncoder()
label = l22.fit_transform(data['urticaria'])
new_data = data
data = new_data.drop('urticaria' , axis='columns')
data['urticaria'] = label

data['class'] = 1
data
```
<br/>
```
#3
y = data['class'].values
y = y.reshape(-1,1)
x_data = data.drop(['class'], axis=1)
#normalization
x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data)).values
x.head(500)
```
<br/>
```
#4

#Splitting dataset
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x , y  , test_size=0.2 , random_state=100 )

y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

print("x_train: " , x_train.shape)
print("x_test: " , x_test.shape)
print("y_train: " , y_train.shape)
print("y_test: " , y_test.shape)
```
<br/>
```
#5
#remove Duplicate

x_train.duplicated()
(x_train.duplicated()).sum() #189=Duplicate
x = x_train.loc[~x_train.duplicated(), :]
x
```
<br/>
```
#6
#KNN
from sklearn.neighbors import KNeighborsClassifier
k = 1
knn = KNeighborsClassifier (n_neighbors = k)
knn.fit(x_train, y_train.ravel())
print("when k = {} neighbors , KNN test accuracy : {}".format(k, knn.score(x_test,y_test)))
print("when k = {} neighbors , KNN train accuracy : {}".format(k, knn.score(x_train,y_train)))
```

ran = np.arange(1,30)
train_list = []
test_list = []
for i,each in enumerate(ran):
  knn = KNeighborsClassifier(n_neighbors = each)
  knn.fit (x_train , y_train.ravel())
  test_list.append (knn.score(x_test , y_test))
  train_list.append (knn.score(x_train , y_train))

plt.figure(figsize=[15,10])
plt.plot(ran , test_list , label = 'Test score')
plt.plot(ran , train_list , label = 'Train score')
plt.xlabel('Number of Neighbors')
plt.ylabel('RI/Na/Mg/Al/Si/K/Ca/Ba/Fe')
plt.xticks(ran)
plt.legend()
print("Best test score is {} and K = {}".format(np.max(test_list), test_list.index(np.max(test_list)) + 1 ))
print("Best train score is {} and K = {}".format(np.max(train_list), train_list.index(np.max(train_list)) + 1 ))
```
<br/>
```
#7
#Bayes
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train , y_train.ravel())
print("Naive Bayes test accuracy: " , nb.score(x_test , y_test))
```
<br/>
```
#8
#Find-s
concepts = np.array(x.iloc[:,0:-1])
print("\nInstances are:\n",concepts)
target = np.array(x.iloc[:,-1])
print("\nTarget Values are: ",target)

def learn(concepts, target): 
    specific_h = concepts[0].copy()
    print("\nInitialization of specific_h and genearal_h")
    print("\nSpecific Boundary: ", specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("\nGeneric Boundary: ",general_h)  

    for i, h in enumerate(concepts):
        print("\nInstance", i+1 , "is ", h)
        if target[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(specific_h)): 
                if h[x]!= specific_h[x]:                    
                    specific_h[x] ='?'                     
                    general_h[x][x] ='?'
                   
        if target[i] == "no":            
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

s_final, g_final = learn(concepts, target)

print("Final Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")
```
<br/>
```
#9
#Candidate Elimination

def learn(concepts, target):
    specific_h = concepts[0].copy()
    print("Initialization of specific_h and general_h")
    print("specific_h: ",specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("general_h: ",general_h)
    print("concepts: ",concepts)
    for i, h in enumerate(concepts):
        if target[i] == "yes":
            for x in range(len(specific_h)):
                #print("h[x]",h[x])
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        if target[i] == "no":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
    print("\nSteps of Candidate Elimination Algorithm: ",i+1)
    print("Specific_h: ",i+1)
    print(specific_h,"\n")
    print("general_h :", i+1)
    print(general_h)

    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    print("\nIndices",indices)
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    return specific_h, general_h
s_final,g_final = learn(concepts, target)
print("\nFinal Specific_h:", s_final, sep="\n")
print("Final General_h:", g_final, sep="\n")
```
<br/>
```
#10
#clustering
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import AffinityPropagation
from matplotlib import pyplot
# define dataset
X, _ = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
# define the model
model = AffinityPropagation(damping=0.9)
# fit the model
model.fit(X)
# assign a cluster to each example
yhat = model.predict(X)
# retrieve unique clusters
clusters = unique(yhat)
# create scatter plot for samples from each cluster
for cluster in clusters:
	# get row indexes for samples with this cluster
	row_ix = where(yhat == cluster)
	# create scatter of these samples
	pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
# show the plot
pyplot.show()
```
<br/>
```
#11
#ID3
def calc_total_entropy(train_data, label, class_list):
    total_row = train_data.shape[0] #the total size of the dataset
    total_entr = 0
    
    for c in class_list: #for each class in the label
        total_class_count = train_data[train_data[label] == c].shape[0] #number of the class
        total_class_entr = - (total_class_count/total_row)*np.log2(total_class_count/total_row) #entropy of the class
        total_entr += total_class_entr #adding the class entropy to the total entropy of the dataset
    
    return total_entr

def calc_entropy(feature_value_data, label, class_list):
    class_count = feature_value_data.shape[0]
    entropy = 0
    
    for c in class_list:
        label_class_count = feature_value_data[feature_value_data[label] == c].shape[0] #row count of class c 
        entropy_class = 0
        if label_class_count != 0:
            probability_class = label_class_count/class_count #probability of the class
            entropy_class = - probability_class * np.log2(probability_class)  #entropy
        entropy += entropy_class
    return entropy

def calc_info_gain(feature_name, train_data, label, class_list):
    feature_value_list = train_data[feature_name].unique() #unqiue values of the feature
    total_row = train_data.shape[0]
    feature_info = 0.0
    
    for feature_value in feature_value_list:
        feature_value_data = train_data[train_data[feature_name] == feature_value] #filtering rows with that feature_value
        feature_value_count = feature_value_data.shape[0]
        feature_value_entropy = calc_entropy(feature_value_data, label, class_list) #calculcating entropy for the feature value
        feature_value_probability = feature_value_count/total_row
        feature_info += feature_value_probability * feature_value_entropy #calculating information of the feature value
        
    return calc_total_entropy(train_data, label, class_list) - feature_info #calculating information gain by subtracting

def find_most_informative_feature(train_data, label, class_list):
    feature_list = train_data.columns.drop(label) #finding the feature names in the dataset
                                            #N.B. label is not a feature, so dropping it
    max_info_gain = -1
    max_info_feature = None
    
    for feature in feature_list:  #for each feature in the dataset
        feature_info_gain = calc_info_gain(feature, train_data, label, class_list)
        if max_info_gain < feature_info_gain: #selecting feature name with highest information gain
            max_info_gain = feature_info_gain
            max_info_feature = feature
            
    return max_info_feature

def generate_sub_tree(feature_name, train_data, label, class_list):
    feature_value_count_dict = train_data[feature_name].value_counts(sort=False) #dictionary of the count of unqiue feature value
    tree = {} #sub tree or node
    
    for feature_value, count in feature_value_count_dict.iteritems():
        feature_value_data = train_data[train_data[feature_name] == feature_value] #dataset with only feature_name = feature_value
        
        assigned_to_node = False #flag for tracking feature_value is pure class or not
        for c in class_list: #for each class
            class_count = feature_value_data[feature_value_data[label] == c].shape[0] #count of class c

            if class_count == count: #count of feature_value = count of class (pure class)
                tree[feature_value] = c #adding node to the tree
                train_data = train_data[train_data[feature_name] != feature_value] #removing rows with feature_value
                assigned_to_node = True
        if not assigned_to_node: #not pure class
            tree[feature_value] = "?" #should extend the node, so the branch is marked with ?
            
    return tree, train_data

def make_tree(root, prev_feature_value, train_data, label, class_list):
    if train_data.shape[0] != 0: #if dataset becomes enpty after updating
        max_info_feature = find_most_informative_feature(train_data, label, class_list) #most informative feature
        tree, train_data = generate_sub_tree(max_info_feature, train_data, label, class_list) #getting tree node and updated dataset
        next_root = None
        
        if prev_feature_value != None: #add to intermediate node of the tree
            root[prev_feature_value] = dict()
            root[prev_feature_value][max_info_feature] = tree
            next_root = root[prev_feature_value][max_info_feature]
        else: #add to root of the tree
            root[max_info_feature] = tree
            next_root = root[max_info_feature]
        
        for node, branch in list(next_root.items()): #iterating the tree node
            if branch == "?": #if it is expandable
                feature_value_data = train_data[train_data[max_info_feature] == node] #using the updated dataset
                make_tree(next_root, node, feature_value_data, label, class_list) #recursive call with updated dataset

def id3(train_data_m, label):
    train_data = train_data_m.copy() #getting a copy of the dataset
    tree = {} #tree which will be updated
    class_list = train_data[label].unique() #getting unqiue classes of the label
    make_tree(tree, None, train_data_m, label, class_list) #start calling recursion
    return tree

def predict(tree, instance):
    if not isinstance(tree, dict): #if it is leaf node
        return tree #return the value
    else:
        root_node = next(iter(tree)) #getting first key/feature name of the dictionary
        feature_value = instance[root_node] #value of the feature
        if feature_value in tree[root_node]: #checking the feature value in current tree node
            return predict(tree[root_node][feature_value], instance) #goto next feature
        else:
            return None

def evaluate(tree, test_data_m, label):
    correct_preditct = 0
    wrong_preditct = 0
    for index, row in test_data_m.iterrows(): #for each row in the dataset
        result = predict(tree, test_data_m.iloc[index]) #predict the row
        if result == test_data_m[label].iloc[index]: #predicted value and expected value is same or not
            correct_preditct += 1 #increase correct count
        else:
            wrong_preditct += 1 #increase incorrect count
    accuracy = correct_preditct / (correct_preditct + wrong_preditct) #calculating accuracy
    return accuracy
```
<br/>
```
#12
# Decision tree for feature importance on a classification problem
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot
# define dataset
X_train, y_train = make_classification(n_samples=255, n_features=22, n_informative=5, n_redundant=5, random_state=1)
# define the model
model = DecisionTreeClassifier()
# fit the model
model.fit(X_train, y_train)
# get importance
importance = model.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
pyplot.bar([x for x in range(len(importance))], importance)
pyplot.show()
```

<div dir="rtl">
در بخش 1 ، کتابخانه های لازم را فراخوانی کردیم .
<br/>
در بخش 2 ، پس از آپلود دیتاست خود ، ویژگی سن را بعناون ویژگی دارای مقادیر نامشخص (missing value) حذف کردیم .
سپس مقادیر ویژگی ها را به جای yes , no به مقادیر گسسته تبدیل کردیم .
<br/>
در بخش 3 ، ویژگی ها و concept را از هم جدا کردیم و مقادیر شان را نرمالایز کردیم (بین 0 و 1 آوردیم)
<br/>
در بخش 4 ، نمونه ها را به دو بخش Train , validation تقسیم کردیم .
<br/>
در بخش 5 ، نمونه ای مشابه و نویز را حذف کردیم.
<br/>
در بخش 6 تا آخر بررسی دیتاست براساس تمامی الگوریتم هایی که آموخته ایم اعم از KNN , Bayes , Candidate Elimination , Clustering , ID3 , Decission Tree انجام شده است .
<br/>
دقت درروش نایو بیز دقت بسیار بالایی است . 
<br/>
در مرحله آخر سعی کرده ایم ویژگی ها را براساس میزان اهمیت و تاثیز گذاری شان به تصویر بکشیم .
<br/>
در انتها تصویری از میزان دقت و سایر اطلاعات به دست آمده توسط Rapidminer آورده ایم .
</div>
![]()