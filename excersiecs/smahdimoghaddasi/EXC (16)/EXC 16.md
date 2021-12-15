 
 
 

<div dir="rtl">
  
  ### 16) برای سه عبارت زیر نیز مثل سوال یک کدهای مربوط به آنها را بنویسید.
 </div>
 
 ## (A AND B) OR (B OR C) XOR (A NAND B)
 
 
 ```
 def my_fun1(A, B, C):
    
 x = A and B
 y = B or C
 z = not x
 s = x or y
 if z!=s :
    return True
 else:
    return False
print(my_fun1(0, 0, 0))
print(my_fun1(0, 0, 1))
print(my_fun1(0, 1, 0))
print(my_fun1(0, 1, 1))
print(my_fun1(1, 0, 0))
print(my_fun1(1, 0, 1))
print(my_fun1(1, 1, 0))
print(my_fun1(1, 1, 1))
```
 
| A | B | C | CLASS |
|---|---|---|-----|
| 0 | 0 | 0 | 1   |
| 0 | 0 | 1 | 0   |
| 0 | 1 | 0 | 0   |
| 0 | 1 | 1 | 0   |
| 1 | 0 | 0 | 1   |
| 1 | 0 | 1 | 0   |
| 1 | 1 | 0 | 1   |
| 1 | 1 | 1 | 1   |


```
#  import libray  
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
# Read and print the data set
df = pandas.read_csv(r"C:\16\16-1.csv")

print(df)

# X is the feature columns, y is the target column
features = ['A', 'B' , 'C']

X = df[features]
y = df['CLASS']

print(X)
print(y)

# Create a Decision Tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)

graph.write_png('mydecisiontree.png')


img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show() 

```
![1.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(16)/1.png)

## (A AND B OR C) OR (C NAND B)
 
 ```
 def my_fun2(A, B, C):
    
 x = A and B
 y = x or C
 w = C and B
 m = not w
 w = y or m
 if w==1 :
    return True
 else:
    return False
 

print(my_fun2(0, 0, 0))
print(my_fun2(0, 0, 1))
print(my_fun2(0, 1, 0))
print(my_fun2(0, 1, 1))
print(my_fun2(1, 0, 0))
print(my_fun2(1, 0, 1))
print(my_fun2(1, 1, 0))
print(my_fun2(1, 1, 1))

```

 
 <br/>
 
| A | B | C | CLASS |
|---|---|---|-----|
| 0 | 0 | 0 | 1   |
| 0 | 0 | 1 | 1   |
| 0 | 1 | 0 | 1   |
| 0 | 1 | 1 | 1   |
| 1 | 0 | 0 | 1   |
| 1 | 0 | 1 | 1   |
| 1 | 1 | 0 | 1   |
| 1 | 1 | 1 | 1   |


```
#  import libray  
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
# Read and print the data set
df = pandas.read_csv(r"C:\16\16-2.csv")

print(df)

# X is the feature columns, y is the target column
features = ['A', 'B' , 'C']

X = df[features]
y = df['CLASS']

print(X)
print(y)

# Create a Decision Tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)

graph.write_png('mydecisiontree.png')
img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show() 
```


 ![2.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(16)/2.png)
 
 
 ## (A XOR B) AND (B OR C) AND (C AND D)
 
 
 ```
 def my_fun3(A, B, C, D):
    
 if A!=B:
   x = 1
 else:
   x = 0
   
 y = C and D
 w = C or B
 z = x and w
 m = z and y
 
 if m==1 :
    return True
 else:
    return False
 

print(my_fun3(0, 0, 0, 0))
print(my_fun3(0, 0, 0, 1))
print(my_fun3(0, 0, 1, 0))
print(my_fun3(0, 0, 1, 1))
print(my_fun3(0, 1, 0, 0))
print(my_fun3(0, 1, 0, 1))
print(my_fun3(0, 1, 1, 0))
print(my_fun3(0, 1, 1, 1))
print(my_fun3(1, 0, 0, 0))
print(my_fun3(1, 0, 0, 1))
print(my_fun3(1, 0, 1, 0))
print(my_fun3(1, 0, 1, 1))
print(my_fun3(1, 1, 0, 0))
print(my_fun3(1, 1, 0, 1))
print(my_fun3(1, 1, 1, 0))
print(my_fun3(1, 1, 1, 1))

```

 
 
| A | B | C | D |CLASS |
|---|---|---|---|-----|
| 0 | 0 | 0 | 0 | 0   |
| 0 | 0 | 0 | 1 | 0   |
| 0 | 0 | 1 | 0 | 0   |
| 0 | 0 | 1 | 1 | 0   |
| 0 | 1 | 0 | 0 | 0   |
| 0 | 1 | 0 | 1 | 0   |
| 0 | 1 | 1 | 0 | 0   |
| 0 | 1 | 1 | 1 | 1   |
| 1 | 0 | 0 | 0 | 0   |
| 1 | 0 | 0 | 1 | 0   |
| 1 | 0 | 1 | 0 | 0   |
| 1 | 0 | 1 | 1 | 1   |
| 1 | 1 | 0 | 0 | 0   |
| 1 | 1 | 0 | 1 | 0   |
| 1 | 1 | 1 | 0 | 0   |
| 1 | 1 | 1 | 1 | 0   |

 
 ```
 #  import libray  
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
# Read and print the data set
df = pandas.read_csv(r"C:\16\16-3.csv")

print(df)

# X is the feature columns, y is the target column
features = ['A', 'B' , 'C', 'D']

X = df[features]
y = df['CLASS']

print(X)
print(y)

# Create a Decision Tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)

graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show() 
```
 
 
 
 
 
 
 ![3.png](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(16)/3.png)
 

 
