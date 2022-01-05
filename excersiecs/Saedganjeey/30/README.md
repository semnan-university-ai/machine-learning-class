<div dir="rtl">
  
  ###  سعی کنید دسته بندی هر خبر را به صورت خودکار بدست آورید.
  
  ابتدا به گوگل درایو یا محل قرار گیری مجموعه داده مان متصل می شویم، سپس کتابخانه های لازم را می خوانیم
  
</div>

```
from google.colab import drive
drive.mount('/content/gdrive')
```

```
import numpy as np
import pandas as pd

news = pd.read_csv('/content/gdrive/MyDrive/dataset/news_data.txt', encoding='utf-8')
news.head()
```
<div dir="rtl">
  
بعد از خواندن فایل مورد نظرمان خروجی به صورت زیر می باشد:
  
  ![pic1](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Saedganjeey/30/1.jpg)


  سپس از کتابخانه sklearn بردار را برای ساخت کلمات فراخوانی می کنیم:
  
  </div>
  
  ```
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

doc = news['news'].values.astype("U")
```
<div dir="rtl">
  
  سپس بعد از ساخت بردار الگوریتم خوشه بندی KMeans را اجرا میکنیم. ما در اینجا مقدار k را 8 گرفته ایم که می تواند بیشتر یا کمتر باشد:
  
  </div>

```
vector = TfidfVectorizer(stop_words='english')
features = vector.fit_transform(doc)

k = 8 #number of our clusters
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
model.fit(features)

news['type'] = model.labels_
news.head()
```

<div dir="rtl">
  
خروجی این مرحله به صورت زیر می باشد:
  

  ![pic2](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Saedganjeey/30/2.jpg)
  در مرحله بعد برای هر دسته یک فایل متنی ساخته و در فایل های خود ذخیره می کنیم:
  <br/>
  اگر در سمت چپ در قسمت فایل ها چک کنیم ،  میبینیم که فایل های دسته بندی ما ساخته شده اند.
  <br/>
  در این فایل میتوانید دسته بندی متون را در فایل های متنی که در مخزن گذاشته شده را چک کنید.
  
 
  ![pic4(https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Saedganjeey/30/4.jpg)
</div>
  
```
clusters = news.groupby('type')
for cluster in clusters.groups:
  my = open('type'+ str(cluster) + '.txt', 'w')
  data = clusters.get_group(cluster)[['news']]
  my.write(data.to_csv(index_label='id'))
  my.close()
  ```
  
  <div dir="rtl">
  
  در این قسمت هم مبنای کار خوشه بندی یا همان مرکز ثقل مان را برای هر دسته چاپ می کنیم:
  
  </div>
  
```
print("cluster centroids:\n")

order_centeroids = model.cluster_centers_.argsort()[:,::-1]
terms = vector.get_feature_names()
for i in range(k):
  print("cluster %d:" %i)
  for j in order_centeroids[i, :10]:
    print('%s' %terms[j])
  print('-----------------')
  ```
  
  <div dir="rtl">
  
  خروجی این قسمت به این صورت می باشد:
  
 
  ![pic3](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Saedganjeey/30/3.jpg)
  </div>
