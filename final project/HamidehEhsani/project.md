# Covid dataset

حمیده احسانی

شماره دانشجویی: 9911624001

## بخش import کردن کتابخانه های مورد نیاز

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
```

## خواندن از فایل و نمایش اطلاعات 
```
#Let's Read csv file
df=pd.read_csv("covid.csv")
#Show records of dataframe
df
```
