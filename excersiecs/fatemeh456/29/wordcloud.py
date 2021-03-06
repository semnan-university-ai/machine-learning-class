!pip install wordcloud-fa

import wordcloud
import matplotlib.pyplot as plt
from wordcloud_fa import WordCloudFa
from IPython.core.display import Image
from PIL import Image
Word_c = WordCloudFa(height= 800 , width=1000 , background_color='white')
with open('news_data.txt' , 'r') as file:
  text = file.read()

cloud = Word_c.generate(text)
plt.imshow(Word_c , interpolation="bilinear")
plt.axis("off")
plt.show()
