در ابتدا کد های اجرایی و بعد درخت هر کدام از آن ها

```
#And Function

def And(A, B):
  if A == False or B==False:
    return False 
  else:
    return True
print("A", "B", "AND")      
print("0", "0",And(0,0))
print("0", "1",And(0,1))
print("1", "0",And(1,0))
print("1", "1",And(1,1))

#Or Function
def Or(A, B):
  if A == True or B==True:
    return True 
  else:
    return False
print("A", "B", "Or")      
print("0", "0",Or(0,0))
print("0", "1",Or(0,1))
print("1", "0",Or(1,0))
print("1", "1",Or(1,1))

#Not Function
def Not(A):
  if A == True:
    return False 
  else:
    return True
print("A", "AND")      
print("0",Not(0))
print("1",Not(1))

#Nand Function
def Nand(A, B):
  if A == True and B==True:
    return False 
  else:
    return True
print("A", "B", "AND")      
print("0", "0",Nand(0,0))
print("0", "1",Nand(0,1))
print("1", "0",Nand(1,0))
print("1", "1",Nand(1,1))

#Nor Function
def NOr(A, B):
  if A == False and B==False:
    return True 
  else:
    return False
print("A", "B", "Or")      
print("0", "0",NOr(0,0))
print("0", "1",NOr(0,1))
print("1", "0",NOr(1,0))
print("1", "1",NOr(1,1))


#Xor function
def Xor(A, B):
  if A == B :
    return False 
  else:
    return True
print("A", "B", "Or")      
print("0", "0",Xor(0,0))
print("0", "1",Xor(0,1))
print("1", "0",Xor(1,0))
print("1", "1",Xor(1,1))

```

حالا کد های درخت و نتایج به دست آمده
```
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn import tree
import graphviz

col_names = ['A','B','Result']

And = pd.read_csv("/content/Data/And.csv", header=None, names=col_names)



x = And[['A']] # Featuresr
y = And.Result # Target variable
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)


dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=['A'], 
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 

```

![And](https://user-images.githubusercontent.com/94211519/146339084-ebba591d-b3b0-4231-9a0a-8f6f5456c5fc.PNG)

Nand

![Nand](https://user-images.githubusercontent.com/94211519/146339192-b48cab4b-833a-4bbc-ac77-48b42e7483b0.PNG)

OR

![Or](https://user-images.githubusercontent.com/94211519/146339216-92be4e6b-03de-43c5-8767-03f412b0f0ef.PNG)

Xor

![Xor](https://user-images.githubusercontent.com/94211519/146339270-21a0243b-7266-455b-8ebc-bb9f8f4f58b6.PNG)

nor

![Nor](https://user-images.githubusercontent.com/94211519/146339298-49022b72-3c48-4c29-af9c-ae1bf28a8f7e.PNG)


Not

![Not](https://user-images.githubusercontent.com/94211519/146339454-3ed955cf-1196-4a81-ae23-c6d591296438.PNG)
