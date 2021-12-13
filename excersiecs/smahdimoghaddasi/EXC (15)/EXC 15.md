
<div dir="rtl">
  
  #### 15) همانطور که در تعاریف درخت تصمیم گفته شده الگوریتم درخت تصمیم شامل IF THEN ELSE ها می باشد؛با یک زبان برنامه نویسی (ترجیحا پایتون، جاوا، سی پلاس پلاس) در قالب یک تابع هر درخت تصمیم مربوط به AND و OR و NOT و NAND و NOR و XOR را رسم کنید.     
  
 حل سوال با استفاده از زبان برنامه نویسی پایتون:
 </div>
 <br/>
 
## AND:

 |A  | B |AND|
 |---|---|---|
 | 0 | 0 | 0 | 
 | 0 | 1 | 0 | 
 | 1 | 0 | 0 | 
 | 1 | 1 | 1 |

```
#import libray  
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

#Read and print the data set
df = pandas.read_csv(r"C:\15\AND.csv")

print(df)

#X is the feature columns, y is the target column
features = ['A', 'B']

X = df[features]
y = df['AND']

print(X)
print(y)

#Create a Decision Tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)

graph.write_png('mydecisiontree.png')


img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
```
![Figure_1_AND.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(15)/Figure_1_AND.png)
 
 
 
 ## OR:
 
| A | B | OR |
|---|---|----|
| 0 | 0 | 0  |
| 0 | 1 | 1  |
| 1 | 0 | 1  |
| 1 | 1 | 1  |
 ```
#import libray 
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

#Read and print the data set
df = pandas.read_csv(r"C:\15\OR.csv")

print(df)

#X is the feature columns, y is the target column
features = ['A', 'B']

X = df[features]
y = df['OR']

print(X)
print(y)

#Create a Decision Tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)

graph.write_png('mydecisiontree.png')


img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show() 
```
 
 ![Figure_2_OR.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(15)/Figure_2_OR.png)
 
## NOT:


| A | ~A |
|---|----|
| 0 | 1  |
| 1 | 0  |

```
#import libray  
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

#Read and print the data set
df = pandas.read_csv(r"C:\15\NOT.csv")

print(df)

#X is the feature columns, y is the target column
feature = ['A']

X = df[feature]
y = df['NOT']

print(X)
print(y)

#Create a Decision Tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=feature)
graph = pydotplus.graph_from_dot_data(data)

graph.write_png('mydecisiontree.png')


img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show() 
```

 ![Figure_3_NOT.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(15)/Figure_3_NOT.png)
 
 ## NAND:
 
| A | B | NAND |
|---|---|------|
| 0 | 0 | 1    |
| 0 | 1 | 1    |
| 1 | 0 | 1    |
| 1 | 1 | 0    |
 
 ```
#import libray  
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

#Read and print the data set
df = pandas.read_csv(r"C:\15\NAND.csv")

print(df)

#X is the feature columns, y is the target column
features = ['A', 'B']

X = df[features]
y = df['NAND']

print(X)
print(y)

#Create a Decision Tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)

graph.write_png('mydecisiontree.png')


img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show() 
```
 
 ![Figure_4_NAND.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(15)/Figure_4_NAND.png)
 
 ## NOR:
| A | B | NOR |
|---|---|-----|
| 0 | 0 | 1   |
| 0 | 1 | 0   |
| 1 | 0 | 0   |
| 1 | 1 | 0   |
  
 
```
#import libray  
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

#Read and print the data set
df = pandas.read_csv(r"C:\15\NOR.csv")

print(df)

#X is the feature columns, y is the target column
features = ['A', 'B']

X = df[features]
y = df['NOR']

print(X)
print(y)

#Create a Decision Tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)

graph.write_png('mydecisiontree.png')


img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show() 
```
 ![Figure_5_NOR.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(15)/Figure_5_NOR.png)
 
## XOR:
| A | B | XOR |
|---|---|-----|
| 0 | 0 | 0   |
| 0 | 1 | 1   |
| 1 | 0 | 1   |
| 1 | 1 | 0   |

```
#import libray  
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

#Read and print the data set
df = pandas.read_csv(r"C:\15\XOR.csv")

print(df)

#X is the feature columns, y is the target column
features = ['A', 'B']

X = df[features]
y = df['XOR']

print(X)
print(y)

#Create a Decision Tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)

graph.write_png('mydecisiontree.png')


img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show() 
```
 
 ![Figure_6_XOR.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(15)/Figure_6_XOR.png)
 
 
