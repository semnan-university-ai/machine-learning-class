# sixith-task
 sixith-task
## تمرین ششم
### یک مثال با الگوریتم Find-s

ابتدا به مثال های آموزشی می‌کنیم:

| example | citation | size  | inlibrary |    price    | editions |  buy  |
|---------|----------|-------|-----------|-------------|----------|-------|
|    1    |   some   | small |    no     | affordeable |   many   |  no   |
|    2    |   many   |  big  |    no     |  expensive  |   one    |  yes  | 
|    3    |   some   |  big  |  always   |  expensive  |   few    |  no   |
|    4    |   many   |medioum|    no     |  expensive  |   many   |  yes  |
|    5    |   many   | small |    no     | affordeable |   many   |  yes  |


#### step1
h0 = (ø, ø, ø, ø, ø)

#### step2
 X1 = (some, small, no, expensive, many) – No
 
 h1 = (ø, ø, ø, ø, ø)
 
#### step3
X2 = (many, big, no, expensive, one) – Yes

h2 = (many, big, no, expensive, one)

#### step4
X3 = (some, big, always, expensive, few) – No

h3 = (many, big, no, expensive, one)

#### step5
X4 = (many, medium, no, expensive, many) – Yes

h4 = (many, ?, no, expensive, ?)

#### step6
X5 = (many, small, no, affordable, many) – Yes

h5 = (many, ?, no, ?, ?)

لذا اخرین فرضیه به دست آمده به عنوان فرضیه بهینه در نظر گرفته می‌شود. یکی از معایب این روش این است که هیچ معیار توقف وجود ندارد و هرگاه یک نمونه آموزشی به آن اضافه شود یک فرضیه جدید تر ارائه می‌دهد.
 
