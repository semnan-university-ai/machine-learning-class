### ابرکلمات هر خبر را با کمک دیتاستی که جمع آوری کرده اید ایجاد کنید و یک ابرکلمات برای تمام خبرها نیزدر نظر بگیرید

</div>

```  
!pip3 install wordcloud-fa

from wordcloud_fa import WordCloudFa
wc = WordCloudFa()

with open('news.txt', 'r') as file:
    text = file.read()

    wc = WordCloudFa(width=1000, height=600)
    wc = WordCloudFa(background_color="blue")

word_cloud = wc.generate(text)

image = word_cloud.to_image()
image.show()

image.save('news.png')

``` 

![news-hashemi(1).png](https://github.com/semnan-university-ai/machine-learning-class/tree/main/excersiecs/baharaak/exc29/news-hashemi(1).png)

![news-hashemi(2).png](https://github.com/semnan-university-ai/machine-learning-class/edit/main/excersiecs/baharaak/exc29/news-hashemi(2).png)

![news-hashemi(3).png](https://github.com/semnan-university-ai/machine-learning-class/edit/main/excersiecs/baharaak/exc29/news-hashemi(3).png)

![news-hashemi(4).png](https://github.com/semnan-university-ai/machine-learning-class/edit/main/excersiecs/baharaak/exc29/news-hashemi(4).png)

![news-hashemi(5).png](https://github.com/semnan-university-ai/machine-learning-class/edit/main/excersiecs/baharaak/exc29/news-hashemi(5).png)

![news-hashemi(6).png](https://github.com/semnan-university-ai/machine-learning-class/edit/main/excersiecs/baharaak/exc29/news-hashemi(6).png)
