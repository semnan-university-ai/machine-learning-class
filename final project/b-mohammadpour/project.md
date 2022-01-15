<div dir="rtl">
  
  با توجه به دیتاست covid که در پوشه ی data موجود است عملیات زیر را روی این دیتاست انجام دهید:
  - نرمالیزه کردن
  - مرتب سازی داده
  - حذف داده های یکسان و تکراری
  - بدست آوردن 5 ویژگی که کمترین اهمیت را دارند
  -  اجرای الگوریتم های find-s و ce و بیز و knn و کلاسترینگ و درخت تصمیم یکبار به صورت تصادفی و یک بار با الگوریتم id3
  - داده های زیر همگی به عنوان true برچسب گذاری خواهند شد و ترکیبات داده ای دیگر به عنوان false تمام ترکیبات داده ای که قابل کشف می باشد را بدست آورید.
  - الگوریتم های اجرا شده را با rappid minner نیست اجرا کنید و نتیجه ی خود را با آن مقایسه کنید
  - دیتاست در سایت kaggle ثبت شده است در صورتی که کد خود را در بخش notebook های kaggle ثبت کنید نمره ی اضافه دریافت خواهید کرد.
  
<br />

  </div>

  اتصال به google drive

  ```
from google.colab import drive
drive.mount('/content/drive')
  ```
 
بارگذاری دیتاست

  ```
  import pandas as pd
import numpy as np
from sklearn import preprocessing
covid = pd.read_csv('/content/drive/MyDrive/covid1.csv',header=0)#load data
#covid.shape 
covid
```

  تبدیل مقادیر خالی به NAN

```
covid.replace('-',np.nan,inplace=True)
covid.head(25)
```
```
covid.isnull().sum()
```
```
covid.replace('-',np.nan,inplace=True)
covid['Headache'].fillna('yes', inplace=True)
```
```
covid['age'] = covid['age'].astype('float64')
```
```
#Delete discarded data
max_age=covid['age'].max()
covid['age'][covid['age']==max_age]
covid.drop(103, axis=0, inplace=True)
```
```
#پرکردن مقادیر null
covid['age'].fillna(covid.groupby('Sleep_problems')['age'].transform("median"),inplace=True)
#ستون سن به دلیل مقادیر null زیاد  حذف خواهد شد
```
```
covid.drop_duplicates(inplace=True) #Remove duplicate row
covid.duplicated() 
  ```
  ```
#تبدیل yes no به 0 1
covid.Sleep_problems.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Headache.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Headache.replace(('Yes', 'No'), (1, 0), inplace=True)
covid.Diarrhea.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Diarrhea.replace(('Yes', 'No'), (1, 0), inplace=True)
covid.Abdominal_pain.replace(('yes', 'no'), (1, 0), inplace=True)
covid.body_pain.replace(('yes', 'no'), (1, 0), inplace=True)
covid.body_pain.replace(('Yes', 'No'), (1, 0), inplace=True)
covid.Body_discoloration.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Cough.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Cough.replace(('Yes', 'No'), (1, 0), inplace=True)
covid.Fever.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Fever.replace(('Yes', 'No'), (1, 0), inplace=True)
covid.Ague.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Sore_throat.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Sore_throat.replace(('Yes', 'No'), (1, 0), inplace=True)
covid.Fatigue.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Fatigue.replace(('Yes', 'No'), (1, 0), inplace=True)
covid.runny_nose.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Chest_pain.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Decreased_appetite.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Vomit.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Nausea.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Sneezing.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Shortness_of_breath.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Loss_of_smell.replace(('yes', 'no'), (1, 0), inplace=True)
covid.Loss_of_taste.replace(('yes', 'no'), (1, 0), inplace=True)
covid.urticaria.replace(('yes', 'no'), (1, 0), inplace=True)

covid
  ```
  ```

#مرتب سازی داده
covid.sort_values('age',inplace=True)
covid
  ```
  ```
#پیدا کردن 5 ویژگی که کم ترین اهمیت را دارند
covid = covid.drop(covid.index[covid['Abdominal_pain'] == 'es'])
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
covid['Loss_of_smell'].value_counts()
covid['Loss_of_smell'].value_counts()
covid['Loss_of_taste'].value_counts()
covid['urticaria'].value_counts()
  ```
  ```
covid.drop(['urticaria','Vomit','Body_discoloration','Abdominal_pain','age'], axis = 1,inplace=True)
covid
  ```
  ```
#normalize
from sklearn import preprocessing
scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
names = covid.columns
d = scaler.fit_transform(covid)
scaled_df = pd.DataFrame(d, columns=names)
scaled_df
  ```
  ```
scaled_df.sort_values('#',inplace=True)
scaled_df
  ```
  ```
# create label col
covid['concept']=0
covid
  ```
  ```
for i in range(len(covid)):
  if ( (covid.iloc[i,2] ==1) or (covid.iloc[i,3] ==1) or (covid.iloc[i,4] ==1)
    or (covid.iloc[i,5]==1) or (covid.iloc[i,6]==1) or (covid.iloc[i,7]==1) or (covid.iloc[i,8]==1)
    or (covid.iloc[i,9]==1) or (covid.iloc[i,10]==1) or (covid.iloc[i,11]==1) or (covid.iloc[i,12]==1)
    or (covid.iloc[i,13]==1) or (covid.iloc[i,14]==1) or (covid.iloc[i,15]==1) or (covid.iloc[i,16]==1) 
    or (covid.iloc[i,17]==1) or (covid.iloc[i,18]==1) ) :

    
    covid.iloc[i,18] = 1
  ```
  ```
covid.drop(['#'], axis = 1,inplace=True)
covid
  ```
  ```
covid.to_csv (r'covid.csv', index = False, header=True)
  ```
  ```
concepts=np.array(covid)[:,:-1]
concepts
covid.head(35)
  ```
  ```
target=np.array(covid)[:,-1]
target
  ```
  ```
#find-s algorithm
def train (con,tar):
    for i,val in enumerate(tar):
        if val== 1:
            specific_h=con[i].copy()
            break
    for i,val in enumerate(con):
        if tar[i]== 1:
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x]='0'#به جای  ؟ عدد 0 قرار داده شده است
                else:
                    pass
    return specific_h
    
print(train(concepts,target))
  ```
  ```
  #CE algorithm
def learn(c, t):

    specific_hy = c[0].copy()

    print("Initialization of specific_h and general_h")

    print("specific_h: ",specific_hy)

    general_h = [["?" for i in range(len(specific_hy))] for i in range(len(specific_hy))]

    print("general_h: ",general_h)

    print("concepts: ",c)

    for i, h in enumerate(c):

        if t[i] == 1:

            for x in range(len(specific_hy)):

                #print("h[x]",h[x])

                if h[x] != specific_hy[x]:

                    specific_hy[x] = '0'

                    general_h[x][x] = '0'

        if t[i] == 0:

            for x in range(len(specific_hy)):

                if h[x] != specific_hy[x]:

                    general_h[x][x] = specific_hy[x]

                else:

                    general_h[x][x] = '0'

    print("\nSteps of Candidate Elimination Algorithm: ",i+1)

    print("Specific_h: ",i+1)

    print(specific_hy,"\n")

    print("general_h :", i+1)

    print(general_h)

    indices = [i for i, val in enumerate(general_h) if val == ['0', '0', '0', '0', '0', '0','0','0','0','0','0','0','0','0','0','0','0']]

    print("\nIndices",indices)

    for i in indices:

        general_h.remove(['0', '0', '0', '0', '0', '0','0','0','0','0','0','0','0','0','0','0','0'])

    return specific_hy, general_h

s_final,g_final = learn(concepts, target)

print("\nFinal Specific_h:", s_final, sep="\n")

print("Final General_h:", g_final, sep="\n")
 ```
  ```
  #naive bayes
from sklearn.model_selection import train_test_split
 ```
  ```
X_train,X_test,y_train,y_test=train_test_split(concepts,target,test_size=0.3,random_state=100)
 ```
  ```
from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(X_train,y_train)
y_pred=gnb.predict(X_test)
print(y_pred)
 ```
  ```
from sklearn import metrics
print(metrics.accuracy_score(y_test,y_pred))
 ```
  ```
  from sklearn.metrics import confusion_matrix
cm=np.array(confusion_matrix(y_test,y_pred))
cm
  ```
  ```

#knn
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train,y_train)
  ```
  ```
knn.score(X_test,y_test)
  ```
  ```
error_rate = []
for i in range(1,20):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))
  ```
  ```
from sklearn.metrics import classification_report,confusion_matrix
pred = knn.predict(X_test)
print(classification_report(y_test,pred))
  ```
  ```
#clustering
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans
  ```
  ```
feature_columns = ['Sleep_problems', 'Headache', 'Diarrhea','body_pain','Cough','Fever','Ague',
                   'Sore_throat','Fatigue' ,'runny_nose','Chest_pain',
                   'Decreased_appetite','Nausea','Sneezing','Shortness_of_breath',
                   'Loss_of_smell','Loss_of_taste']
X = covid[feature_columns]
  ```
  ```
  kmeans = KMeans(n_clusters = 3, max_iter = 300, random_state = 0)
kmeans.fit(X)
 ```
  ```
centers = kmeans.cluster_centers_
print(centers)
 ```
  ```
#random forest
X_train,X_test,y_train,y_test=train_test_split(concepts,target,test_size=0.7,random_state=100)
X_train.shape, X_test.shape
 ```
  ```
from sklearn.ensemble import RandomForestClassifier
classifier_rf = RandomForestClassifier(random_state=100, n_jobs=-1, max_depth=5,
                                       n_estimators=100, oob_score=True)
  ```
  ```                                      
                                       
classifier_rf.fit(X_train, y_train)
classifier_rf.oob_score_
 ```
  ```
rf = RandomForestClassifier(random_state=42, n_jobs=-1)
 ```
  ```
params = {
    'max_depth': [2,3,5,10,20],
    'min_samples_leaf': [5,10,20,50,100,200],
    'n_estimators': [10,25,30,50,100,200]
}
 ```
  ```
from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(estimator=rf,
                           param_grid=params,
                           cv = 4,
                           n_jobs=-1, verbose=1, scoring="accuracy")
 ```
  ```                           
grid_search.fit(X_train, y_train)
 ```
  ```
grid_search.best_score_
 ```
  ```
rf_best = grid_search.best_estimator_
rf_best
 ```
  ```
from sklearn.tree import plot_tree
plt.figure(figsize=(80,40))
plot_tree(rf_best.estimators_[5], feature_names = X.columns,class_names=['Disease', "No Disease"],filled=True);
 ```
  ```
from sklearn.tree import plot_tree
plt.figure(figsize=(80,40))
plot_tree(rf_best.estimators_[7], feature_names = X.columns,class_names=['Disease', "No Disease"],filled=True);
 ```
  ```

rf_best.feature_importances_

 ```
  ```
X_train,X_test,y_train,y_test=train_test_split(concepts,target,test_size=0.3)
 ```
  ```
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
 ```
  ```
y_pred = classifier.predict(X_test)
 ```
  ```
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
 ```
  ```
  #id3
def calc_total_entropy(train_data, label, class_list):
    total_row = train_data.shape[0] #the total size of the dataset
    total_entr = 0
    
    for c in class_list: #for each class in the label
        total_class_count = train_data[train_data[label] == c].shape[0] #number of the class
        total_class_entr = - (total_class_count/total_row)*np.log2(total_class_count/total_row) #entropy of the class
        total_entr += total_class_entr #adding the class entropy to the total entropy of the dataset
    
    return total_entr
 ```
  ```    
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
 ```
```
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
```
```
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
```
```  
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
```
```
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
```
```
  def id3(train_data_m, label):
    train_data = train_data_m.copy() #getting a copy of the dataset
    tree = {} #tree which will be updated
    class_list = train_data[label].unique() #getting unqiue classes of the label
    make_tree(tree, None, train_data_m, label, class_list) #start calling recursion
    return tree
```
```
  tree = id3(covid, 'concept')
tree
```
 ```
  from sklearn.model_selection import cross_val_predict,KFold,cross_val_score, train_test_split, learning_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
```
```
X_train, X_test, y_train, y_test = train_test_split(concepts, target, test_size=0.2, random_state=1)
clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
clf.fit(X_train,y_train)
results = cross_val_score(estimator=clf, X=X_train, y=y_train, cv=4)
print("Accuracy: %0.2f (+/- %0.2f)" % (results.mean(), results.std()))
y_pred = cross_val_predict(estimator=clf, X=concepts, y=target, cv=4)
conf_mat = confusion_matrix(target,y_pred)
print(conf_mat)
```
