## فرمول انتروپی روش id3 در پایتون

یک درخت تصمیم توسط گره ها تشکیل می شود: گره ریشه، گره های داخلی و گره های برگ. ما می توانیم یک کلاس پایتون ایجاد کنیم که حاوی تمام اطلاعات تمام گره های درخت تصمیم باشد.

class Node:
  
    def __init__(self):
        self.value = None
        self.next = None
        self.childs = None

اکنون کلاس اصلی خود را به نام DecisionTreeClassifier ایجاد می کنیم و از سازنده __init__ برای مقداردهی اولیه ویژگی های کلاس و برخی از متغیرهای مهمی که قرار است مورد نیاز هستند استفاده کنیم.


class DecisionTreeClassifier:
    """Decision Tree Classifier using ID3 algorithm."""

    def __init__(self, X, feature_names, labels):
        self.X = X  # features or predictors
        self.feature_names = feature_names  # name of the features
        self.labels = labels  # categories
        self.labelCategories = list(set(labels))  # unique categories
        # number of instances of each category
        self.labelCategoriesCount = [list(labels).count(x) for x in self.labelCategories]
        self.node = None  # nodes
        # calculate the initial entropy of the system
        self.entropy = self._get_entropy([x for x in range(len(self.labels))])

برای محاسبه نت آنتروپی از تابع خصوصی _get_entropy( ) استفاده می کنیم. کد این تابع در زیر ارائه شده است:

Entropy(S)= -((p+ logp+) + (p-logp-))


def _get_entropy(self, x_ids):
    
  
    labels = [self.labels[i] for i in x_ids]
    # count number of instances of each category
    label_count = [labels.count(x) for x in self.labelCategories]
    # calculate the entropy for each category and sum them
    entropy = sum([-count / len(x_ids) * math.log(count / len(x_ids), 2)
                   if count else 0
                   for count in label_count
                  ])
        
    return entropy
