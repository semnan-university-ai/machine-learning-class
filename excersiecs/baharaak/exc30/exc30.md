### سعی کنید دسته بندی هر خبر را به صورت خودکار بدست آورید

```
import numpy as np
import pandas as pd

news = pd.read_csv('news.txt', encoding='UTF-8')
news.head()

```
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

doc = news['news'].values.astype("UTF-8")
```

```

vector = TfidfVectorizer(stop_words='english')
features = vector.fit_transform(doc)

k = 10
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
model.fit(features)

news['type'] = model.labels_
news.head()
```

```
clusters = news.groupby('type')
for cluster in clusters.groups:
  my = open('type'+ str(cluster) + '.txt', 'w')
  data = clusters.get_group(cluster)[['news']]
  my.write(data.to_csv(index_label='id'))
  my.close()

```

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


