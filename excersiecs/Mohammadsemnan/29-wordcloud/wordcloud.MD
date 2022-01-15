```
import matplotlib.pyplot as plt
from wordcloud_fa import *
from google.colab import files

# Read text
text = open('/content/news.txt', mode='r', encoding='utf-8').read()
stop=open('/content/stop-words.txt', mode='r', encoding='utf-8').read()

wc = WordCloudFa(
        background_color='white',
        stopwords=stop,
        height = 600,
        width=400
)

wc.generate(text)

# store to file
wc.to_file('/content/aks/news.png')
```
بدون stop

![wordcloud_output](https://user-images.githubusercontent.com/94211519/148322838-e3c5e08c-93c2-420d-9c58-9c17efc9b20e.png)

با stop

![wordcloud_output (1)](https://user-images.githubusercontent.com/94211519/148322900-71b0be4f-0067-481f-88b7-eff986d36186.png)

اقتصادی:

![egh (1)](https://user-images.githubusercontent.com/94211519/148322926-21e71388-3d68-4d92-96a2-665b0a885236.png)

اجتماعی

![ej](https://user-images.githubusercontent.com/94211519/148322944-12464f3e-30e2-455c-b865-b1d77620f947.png)

سیاسی:

![siyasi](https://user-images.githubusercontent.com/94211519/148322973-ae704bf0-997b-46cd-be69-50b95ca0babf.png)

نظامی:

![nezami](https://user-images.githubusercontent.com/94211519/148322994-eabfb906-43a0-4ef1-b219-f9046309596c.png)

عمومی:

![omimi](https://user-images.githubusercontent.com/94211519/148323014-5a853238-51af-4b7d-8e28-72983bde9254.png)

پزشکی:

![pez](https://user-images.githubusercontent.com/94211519/148323037-ae6dee1d-bc10-47f0-9c15-823b5279c649.png)

ورزشی:

![varzeshi](https://user-images.githubusercontent.com/94211519/148323066-9dd05645-2567-4620-80e3-829fb3b2bb39.png)

