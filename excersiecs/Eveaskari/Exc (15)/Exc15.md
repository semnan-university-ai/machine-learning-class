<div dir="rtl">
  
  ### همانطور که در تعاریف درخت تصمیم گفته شده الگوریتم درخت تصمیم شامل IF THEN ELSE ها می باشد؛با یک زبان برنامه نویسی (ترجیحا پایتون، جاوا، سی پلاس پلاس) در قالب یک تابع هر درخت تصمیم مربوط به AND و OR و NOT و NAND و NOR و XOR را رسم کنید.
      
  </div>
  AND:
 
```
#import library
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
#import dataset
df = pandas.read_csv("/content/gdrive/MyDrive/AndOrtree/data-and.csv")

print(df)

#print truthTable
features = ['A', 'B']

X = df[features]
y = df['And']

print(X)
print(y)

#show tree
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
```
![andtree](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(15)/and%20tree.JPG)

<div dir="rtl">
  
  برای باقی توابع هم به همین صورت انجام میدهیم.
  </div>
  
OR:<br/>
![ortree](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(15)/Or.JPG)

NOT:<br/>
![nottree](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(15)/not.JPG)

XOR:<br/>
![xortree](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(15)/xor.JPG)

NAND:<br/>
![nandtree](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(15)/nand.JPG)

NOR:<br/>
![nortree](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(15)/nor.JPG)
  
