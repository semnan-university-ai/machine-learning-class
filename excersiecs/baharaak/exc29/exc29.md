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


### ابر کلمات برای هر خبر جدا



![news-hashemi(1)](news-hashemi(1).jpg)

![news-hashemi(2)](news-hashemi(2).jpg)

![news-hashemi(3)](news-hashemi(3).jpg)

![news-hashemi(4)](news-hashemi(4).jpg)

![news-hashemi(5)](news-hashemi(5).jpg)

![news-hashemi(6)](news-hashemi(6).jpg)

![news-hashemi(7)](news-hashemi(7).jpg)

![news-hashemi(8)](news-hashemi(8).jpg)

![news-hashemi(9)](news-hashemi(9).jpg)

![news-hashemi(10)](news-hashemi(10).jpg)

![news-hashemi(11)](news-hashemi(11).jpg)

![news-hashemi(12)](news-hashemi(12).jpg)

![news-hashemi(13)](news-hashemi(13).jpg)

![news-hashemi(14)](news-hashemi(14).jpg)

![news-hashemi(15)](news-hashemi(15).jpg)

![news-hashemi(16)](news-hashemi(16).jpg)

![news-hashemi(17)](news-hashemi(17).jpg)

![news-hashemi(18)](news-hashemi(18).jpg)

![news-hashemi(19)](news-hashemi(19).jpg)

![news-hashemi(20)](news-hashemi(20).jpg)

#### ابر کلمات برای دیتاست کلی 

![news](news.jpg)

![newss](newss.jpg)

