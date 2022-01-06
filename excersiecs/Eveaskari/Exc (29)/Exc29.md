<div dir="">
  
  ###  ابرکلمات هر خبر را با کمک دیتاستی که جمع آوری کرده اید ایجاد کنید و یک ابرکلمات برای تمام خبرها نیز در نظر بگیرید.
  
  ```
  from wordcloud_fa import WordCloudFa
import numpy as np
import pandas as pd
from PIL import Image
from matplotlib.image import imread
import re
import matplotlib.pyplot as plt



with open('/content/gdrive/MyDrive/dataset/news.txt', 'r' , encoding='utf-8') as file:
    text = file.read()
mask_image = np.array(Image.open("/content/gdrive/MyDrive/dataset/cloudbrain.jpg"))
Word_cloud = WordCloudFa(mask=mask_image, 
                         background_color="#f2f2f2",
                          max_font_size=100,
                          min_font_size=15,  
                          scale=10,
                          collocations=False,
                          no_reshape=False, 
                          remove_unhandled_utf_characters=True,  
                          persian_normalize=False, 
                          include_numbers=False )
Word_cloud.add_stop_words_from_file("/content/gdrive/MyDrive/dataset/stop.txt"),
frequencies = Word_cloud.process_text(text)
cloud = Word_cloud.generate_from_frequencies(frequencies)
print(len(text))

plt.imshow(cloud)
plt.axis("off")
plt.show()
```
  <br/>
  
  ![wordcloud](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(29)/wordcloud.JPG)
  
  <br/>
  ابر کلمات خبر ورزشی
  
  ![sport](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(29)/sportwc.JPG)
  
  <br/>
  ابر کلمات خبر اقتصادی
  
  ![economic](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(29)/econ.JPG)
  
  <br/>
  ابر کلمات خبر سلامت
  
  ![helth](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(29)/helthcw.JPG)
  
  <br/>
  ابر کلمات خبر سیاسی
  
  ![politic](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(29)/politiccw.JPG)
  
  <br/>
  ابر کلمات خبر تکنولوژی
  
  ![hitech](https://github.com/semnan-university-ai/machine-learning-class/blob/main/excersiecs/Eveaskari/Exc%20(29)/hitech.JPG)
  
  <br/>
  
  
  
  <br/>
  
  </div>
