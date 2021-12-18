کد زیر روی مثال 14 اعمال شده نتیجه هم زیر کد ها قرار دارد

![example 2](https://user-images.githubusercontent.com/94211519/146635150-567f3ef5-ae43-458e-b67c-f3e02bd40cfa.PNG)

```
import pandas as pd
from sklearn.preprocessing import LabelEncoder

col_names = ['Size', 'Color', 'Shape', 'Result']
data = pd.read_csv("/content/2.csv", header=None, names=col_names)

def log(x,base):
    result = ln(x)/ln(base)
    return result

def ln(x):
    val = x
    return 99999999*(x**(1/99999999)-1)

encoder = LabelEncoder()
data['Result']=encoder.fit_transform(pima['Result'])

total= len(list(data['Result']))

yes=data['Result'].sum()

no=total-yes

Entropy=-((yes/total *log(yes/total,2)) +(no/total *log(no/total,2)) )

Entropy
```

![data](https://user-images.githubusercontent.com/94211519/146340889-c610339f-c546-4a7f-bcdd-b3284ed41248.PNG)
