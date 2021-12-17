<div dir="rtl">

## part 1(EX1)

###
def ex1(a, b, c):
  if a == True:
    if b == True:
      if c == True:
          return True 
      elif c == False:
          return False 
    elif b == False: 
      return False
  elif a == False:
    if b == False:
      if c == True:
          return False
      elif c == False: 
          return True
    elif b == True:
      if c == True:
          return True 
      elif c == False:
          return False
print("A", "B", "C", "ex1")      
print("0", "0", "0", ex1(0,0,0))
print("0", "0", "1", ex1(0,0,1))
print("0", "1", "0", ex1(0,1,0))
print("0", "1", "1", ex1(0,1,1))
print("1", "0", "0", ex1(1,0,0))
print("1", "0", "1", ex1(1,0,1))
print("1", "1", "0", ex1(1,1,0))
print("1", "1", "1", ex1(1,1,1))
 ###
A B C ex1
0 0 0 True
0 0 1 False
0 1 0 False
0 1 1 True
1 0 0 False
1 0 1 False
1 1 0 False
1 1 1 True

import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
df = pandas.read_csv("/content/ex1")
print(df)
features = ['A', 'B','C']
X = df[features]
y = df['ex']
print(df)
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('ex1.png')

img=pltimg.imread('ex1.png')
imgplot = plt.imshow(img)
plt.show()

   A  B  C  ex
0  0  0  0   1
1  0  0  1   0
2  0  1  0   0
3  0  1  1   1
4  1  0  0   0
5  1  0  1   0
6  1  1  0   0
7  1  1  1   1 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
</div>
