مثال ها به صورت زیر میباشد

1.(A AND B) OR (B OR C) XOR (A NAND B)

2.(A AND B OR C) OR (C NAND B)

3.(A XOR B) AND (B OR C) AND (C AND D)

جواب ها به ترتیب میباشد

1.

```
def Ex1(A, B, C):
 a1 = A and B
 a2 = B or C
 a3 = not (A and B)
 b1 = a1 or a2
 if a3==b1 :
    return False
 else:
    return True
print("A   B   C    Rusult")
print("0   0   0  ",Ex1(0, 0, 0))
print("0   0   1  ",Ex1(0, 0, 1))
print("0   1   0  ",Ex1(0, 1, 0))
print("0   1   1  ",Ex1(0, 1, 1))
print("1   0   0  ",Ex1(1, 0, 0))
print("1   0   1  ",Ex1(1, 0, 1))
print("1   1   0  ",Ex1(1, 1, 0))
print("1   1   1  ",Ex1(1, 1, 1))
```

![ex1](https://user-images.githubusercontent.com/94211519/146635384-0277b407-be9f-4b25-ae2e-4cf920845837.PNG)

![1](https://user-images.githubusercontent.com/94211519/146635386-ffc8aa9a-e198-4e95-816c-fc04a0e8c65f.PNG)


2.

```
def Ex2(A, B, C):
 a1 = A and B or C
 a2 = not(C and B)
 if a1==True or a2==True :
    return True
 else:
   return False
   
print("A   B   C    Rusult")
print("0   0   0  ",Ex2(0, 0, 0))
print("0   0   1  ",Ex2(0, 0, 1))
print("0   1   0  ",Ex2(0, 1, 0))
print("0   1   1  ",Ex2(0, 1, 1))
print("1   0   0  ",Ex2(1, 0, 0))
print("1   0   1  ",Ex2(1, 0, 1))
print("1   1   0  ",Ex2(1, 1, 0))
print("1   1   1  ",Ex2(1, 1, 1))
```
![ex2](https://user-images.githubusercontent.com/94211519/146635659-415252c6-32e3-4086-b04f-4890a2bbdd2e.PNG)

![2](https://user-images.githubusercontent.com/94211519/146635663-854b5cc7-fb90-47d1-843b-29df24e9bfb4.PNG)

3.

```
def Ex3(A, B, C, D):
 if A==B:
   a1 = False
 else:
   a1 = True
 a2 = B or C
 a3 = C and D
 b1 = a1 and a2
 if b1==True and a3==True  :
    return True
 else:
   return False
 
print("A   B   C   D   Rusult")
print("0   0   0   0   ",Ex3(0, 0, 0, 0))
print("0   0   0   1   ",Ex3(0, 0, 0, 1))
print("0   0   1   0   ",Ex3(0, 0, 1, 0))
print("0   0   1   1   ",Ex3(0, 0, 1, 1))
print("0   1   0   0   ",Ex3(0, 1, 0, 0))
print("0   1   0   1   ",Ex3(0, 1, 0, 1))
print("0   1   1   0   ",Ex3(0, 1, 1, 0))
print("0   1   1   1   ",Ex3(0, 1, 1, 1))
print("1   0   0   0   ",Ex3(1, 0, 0, 0))
print("1   0   0   1   ",Ex3(1, 0, 0, 1))
print("1   0   1   0   ",Ex3(1, 0, 1, 0))
print("1   0   1   1   ",Ex3(1, 0, 1, 1))
print("1   1   0   0   ",Ex3(1, 1, 0, 0))
print("1   1   0   1   ",Ex3(1, 1, 0, 1))
print("1   1   1   0   ",Ex3(1, 1, 1, 0))
print("1   1   1   1   ",Ex3(1, 1, 1, 1))
   
```

![ex3](https://user-images.githubusercontent.com/94211519/146635859-83c8fea9-e015-4df9-9613-f1de80c14616.PNG)

![3](https://user-images.githubusercontent.com/94211519/146635867-148fe666-6d66-4b13-a2a8-2e39db23257d.PNG)


کد ساخت درخت تنها نیاز به تغییر داده های آموزشی میباشد و در جوپبیتر اجرا شود

```
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn import tree
import graphviz

col_names = ['A', 'B', 'C', 'Result']
pima = pd.read_csv("/content/Third example.csv", header=None, names=col_names)

feature_cols = ['A', 'B', 'C','D']
x = pima[feature_cols] # Features
y = pima.Result # Target variable
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)


dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=['A', 'B', 'C'], 
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 
```
