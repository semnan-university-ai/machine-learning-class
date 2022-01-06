
<div dir="rtl">
  
  #### 25)  با کمک توابع رندوم در یک زبان برنامه نویسی روی یک صفحه ی مختصات دوبعدی 100 نقطه با x و yهای رندوم در بازه ی 1 تا 50 بدست آورید و برنامه ای بنویسید که k=3 را نسبت به 43 یا چهل و سومین نقطه ی تولید شده ی شما دارد.
  
  </div>
  
```  
import matplotlib.pyplot as plt
import numpy as np

points = np.random.random_sample(size = (100,2))*50

n43th = points[43-1] 
dist = np.linalg.norm(points - n43th, axis=1)
neighbors = dist.argsort()[:4] 
plt.scatter(points[:,0],points[:,1],c="g")
plt.scatter(points[neighbors][:,0],points[neighbors][:,1],c="r")
plt.scatter(points[42,0],points[42,1],c="k")
plt.show()
print("index of neighbours of 43th are : {}".format(neighbors))

for i in range(3):
    print("point {} : x: {:.4f} y: {:.3f}".format(i+1,points[neighbors[i]][0],
                                          points[neighbors[i]][1]))
                                          
 ``` 
  
 ![25-knn.jpeg](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/smahdimoghaddasi/EXC%20(25)/25-knn.jpeg)
