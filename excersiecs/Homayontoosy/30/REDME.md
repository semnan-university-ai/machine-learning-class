<div dir="rtl">
سوال : 
سعی کنید دسته بندی هر خبر را به صورت خودکار بدست آورید. 
<div/>

![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/30/1.jpg)
  

<div dir="rtl">
فایل خبر را فراخوانی میکنیم
<div/>  
  
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.cluster import KMeans

doc = news['news'].values.astype("UTF-8")

vector = TfidfVectorizer(stop_words='english')

features = vector.fit_transform(doc)

k = 10

model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)

model.fit(features)

news['type'] = model.labels_

news.head()

clusters = news.groupby('type')

for cluster in clusters.groups:

my = open('type'+ str(cluster) + '.txt', 'w')

data = clusters.get_group(cluster)[['news']]

my.write(data.to_csv(index_label='id'))

my.close()

<div dir="rtl">
به صورت زیر دسته بندی هر خبر را نمایش میدهیم:
<div/>

print("c:\n")

order_centeroids = model.cluster_centers_.argsort()[:,::-1]

terms = vector.get_feature_names()

for i in range(k):

print("c:" %i)

for j in order_centeroids[i, :10]:

print('%s' %terms[j])

  
![](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Homayontoosy/30/2.jpg) 
  
 
