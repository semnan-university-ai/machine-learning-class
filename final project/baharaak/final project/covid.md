
```
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from itertools import product
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import math
from collections import deque

```

```
covid= pd.read_csv('covid.csv')

covid.head()
```

```
covid= covid.drop(['#'], axis=1)
covid= covid.drop(['age'], axis=1)
covid.head()
```
```
covid.describe()
```
```
covid=covid.replace({'es':'Yes'});
covid=covid.replace({'Yes':'yes'});
covid=covid.replace({'No':'no'});
covid.describe()

```
```
from sklearn import preprocessing
covid=covid.drop_duplicates()
covid.replace(('yes', 'no'), (1 , 0), inplace=True)
covid.head()

```
```
covid['Sleep_problems'].value_counts()
covid['Headache'].value_counts()
covid['Diarrhea'].value_counts()
covid['Abdominal_pain'].value_counts()
covid['body_pain'].value_counts()
covid['Body_discoloration'].value_counts()
covid['Cough'].value_counts()
covid['Fever'].value_counts()
covid['Ague'].value_counts()
covid['Sore_throat'].value_counts()
covid['Fatigue'].value_counts()
covid['runny_nose'].value_counts()
covid['Chest_pain'].value_counts()
covid['Decreased_appetite'].value_counts()
covid['Vomit'].value_counts()
covid['Nausea'].value_counts()
covid['Sneezing'].value_counts()
covid['Shortness_of_breath'].value_counts()

```
```
covid.drop(['urticaria','Vomit','Body_discoloration','Abdominal_pain'], axis = 1,inplace=True)
covid
```
```
np.where(pd.isnull(covid))
covid=covid.drop(covid.index[194])
np.where(pd.isnull(covid))
```
```
from sklearn import preprocessing
covid_data = covid.copy()

```
```
data = covid.append(covid_data, ignore_index=True)

data

```
```
scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
names = data.columns
d = scaler.fit_transform(data)
DATA = pd.DataFrame(d, columns=names)
DATA
```

```
COVID = np.array(DATA)[:,:-1]
CLASS = np.array(DATA)[:,-1]
```
```
def train(con, tar):
    for i, val in enumerate(tar):
        if val == 'yes' or "Yes":
            specific_h = con[i].copy()
            break
            
    for i, val in enumerate(con):
        if tar[i] == 'yes' or "Yes":
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
                else:
                    pass
    return specific_h


print(find_s(COVID,CLASS))
```
```
def learn(con, tar):

    specific_h = con[0].copy()
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]

    print("specific_h: ",specific_h)
    print("general_h: ",general_h)
    #print("concepts: ",con)

    for i, h in enumerate(con):
        if tar[i] == "yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'

        if tar[i] == "no":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'


    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]

    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    return specific_h, general_h

s_final,g_final = learn(COVID,CLASS)

print("\nFinal Specific_h:", s_final, sep="\n")

print("Final General_h:", g_final, sep="\n")
```

```
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(COVID,CLASS, test_size = 0.30, random_state = 0)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
```

```
classifier = GaussianNB()
classifier.fit(x_train, y_train)
yprob  =  classifier.predict(x_test)
confusion = confusion_matrix(y_test, yprob)
print(classification_report(y_test, yprob))
accuracy = accuracy_score(y_test,yprob)

print(accuracy)
```
```
classifier = KNeighborsClassifier(n_neighbors=15)
classifier.fit(x_train, y_train)
yprob_1 = classifier.predict(x_test)
print(confusion_matrix(y_test, yprob_1))
print(classification_report(y_test, yprob_1))
accuracy = accuracy_score(y_test,yprob_1)

print(accuracy)
```

```
clf = DecisionTreeClassifier(max_depth=8, criterion='entropy', random_state=1)
clf = clf.fit(x_train,y_train)
yprob_2 = clf.predict(x_test)
print(confusion_matrix(y_test, yprob_2))
print(classification_report(y_test, yprob_2))
accuracy = accuracy_score(y_test,yprob_2)

print(accuracy)
```

```
kmeans = KMeans(n_clusters = 3, max_iter = 300, random_state = 0)
kmeans.fit(x_train)
centers = kmeans.cluster_centers_
print(centers)
```

```
class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.childs = None


class DecisionTreeClassifier:
    def __init__(self, X, feature_names, labels):
        self.X = X
        self.feature_names = feature_names
        self.labels = labels
        self.labelCategories = list(set(labels))
        self.labelCategoriesCount = [list(labels).count(x) for x in self.labelCategories]
        self.node = None
        self.entropy = self._get_entropy([x for x in range(len(self.labels))])  # calculates the initial entropy

    def _get_entropy(self, x_ids):
        labels = [self.labels[i] for i in x_ids]
      
        label_count = [labels.count(x) for x in self.labelCategories]
    
        entropy = sum([-count / len(x_ids) * math.log(count / len(x_ids), 2) if count else 0 for count in label_count])
        return entropy

    def _get_information_gain(self, x_ids, feature_id):
      
        info_gain = self._get_entropy(x_ids)
        
        x_features = [self.X[x][feature_id] for x in x_ids]
        
        feature_vals = list(set(x_features))
        
        feature_vals_count = [x_features.count(x) for x in feature_vals]
        
        feature_vals_id = [
            [x_ids[i]
            for i, x in enumerate(x_features)
            if x == y]
            for y in feature_vals
        ]

        
        info_gain = info_gain - sum([val_counts / len(x_ids) * self._get_entropy(val_ids)
                                     for val_counts, val_ids in zip(feature_vals_count, feature_vals_id)])

        return info_gain

    def _get_feature_max_information_gain(self, x_ids, feature_ids):

        
        features_entropy = [self._get_information_gain(x_ids, feature_id) for feature_id in feature_ids]
        
        max_id = feature_ids[features_entropy.index(max(features_entropy))]

        return self.feature_names[max_id], max_id

    def id3(self):

        x_ids = [x for x in range(len(self.X))]
        feature_ids = [x for x in range(len(self.feature_names))]
        self.node = self._id3_recv(x_ids, feature_ids, self.node)
        print('')

    def _id3_recv(self, x_ids, feature_ids, node):

        if not node:
            node = Node()  

        # sorted labels by instance id
        labels_in_features = [self.labels[x] for x in x_ids]

        # if all the example have the same class (pure node), return node
        if len(set(labels_in_features)) == 1:
            node.value = self.labels[x_ids[0]]
            return node

        
        if len(feature_ids) == 0:
            node.value = max(set(labels_in_features), key=labels_in_features.count)  # compute mode
            return node
        
        best_feature_name, best_feature_id = self._get_feature_max_information_gain(x_ids, feature_ids)
        node.value = best_feature_name
        node.childs = []
        # value of the chosen feature for each instance
        feature_values = list(set([self.X[x][best_feature_id] for x in x_ids]))
        # loop through all the values
        for value in feature_values:
            child = Node()
            child.value = value  
            node.childs.append(child)  
            child_x_ids = [x for x in x_ids if self.X[x][best_feature_id] == value]
            if not child_x_ids:
                child.next = max(set(labels_in_features), key=labels_in_features.count)
                print('')
            else:
                if feature_ids and best_feature_id in feature_ids:
                    to_remove = feature_ids.index(best_feature_id)
                    feature_ids.pop(to_remove)
                # recursively call the algorithm
                child.next = self._id3_recv(child_x_ids, feature_ids, child.next)
        return node

    def printTree(self):
        if not self.node:
            return
        nodes = deque()
        nodes.append(self.node)
        while len(nodes) > 0:
            node = nodes.popleft()
            print(node.value)
            if node.childs:
                for child in node.childs:
                    print('({})'.format(child.value))
                    nodes.append(child.next)
            elif node.next:
                print(node.next)

tree_clf = DecisionTreeClassifier(X=X_train, feature_names=feature_vector[:-1], labels=Y_train)
print("System entropy {:.4f}".format(tree_clf.entropy))
```










