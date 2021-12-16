# task14
 
| Example |  Size | Color |   Shape  | Class/Lable |
|:-------:|:-----:|:-----:|:--------:|:-----------:|
|    1    |  big  |  red  |  circle  |      no     |
|    2    |  big  |  red  | triangle |     yes     |
|    3    | small |  red  |  circle  |      no     |
|    4    |  big  |  red  | triangle |      no     |    
|    5    | small |  blue |  circle  |      no     |



<div  dir="rtl">
 در این سه روش نمونه شماره 4 بایستی حدف شود و نباید در نظر گرفته شود. زیرا اگر توجه شود مقادیر ویژگی های نمونه دوم و چهارم یکسان هستند ولی نمونه 4 no شده و نمونه 4 yes شده. از طرف دیگر چون مثال دو تنها موردی است که yes شده است لذا به دلیل تناقض با نمونه 4، نمونه 4 در کل روش ها در نطر گرفته نمیشود و حذف می شود. 
 </div>

first step

S0 = <0,0,0>

G0 =< ?,?,?>

second step

x1= < big, red, circle> -

S1 =< 0,0,0>

G1=< small, ?, ?> < ?, blue, ?> < ?, ?, triangle>

third  step

x2= < big, red, triangle> +

S2 = < big, red, triangle>

G2= < ?, ?, triangle>

forth step

x3= < small, red, circle> -

S3 = < big, red, triangle>

G3= < ?, ?, triangle>

fifth step

x5= < small, blue, circle> -

S4 = < big, red, triangle>

G4= < ?, ?, triangle>

-------------------------

### ID3 ALGORITHM

Gain(S, A)= Entropy(S) - ∑((|Sᵥ|/ S|)* Entropy(Sᵥ))
Entropy(s): ∑-pi* log(pi)

<div  dir="rtl">
 با استفاده از رابطه بالا ابتدا بهره اطلاعاتی را برای انتخاب ریشه درخت حساب میکنیم
 </div>
 
 for (feature==size)
 
 entropy(small) => -2/4(0/4 log0/4 + 2/2 log2/2)= 0
 
entropy(big) => -2/4(1/2 log 1/2 + 1/2 log 1/2)= 0.5

gain(s, size)= Entropy(S) - ∑((|Sᵥ|/ S|)* Entropy(Sᵥ))= 0.87 - (0 + 0.5)= 0.37


for(feature==coller)

entropy(red) => -3/4(2/3 log2/3 + 1/3 log1/3)= 0.29

entropy(blue) => -1/4(1/1 log 1/1 + 0/1 log 0/1)= 0

gain(s, color)= Entropy(S) - ∑((|Sᵥ|/ S|)* Entropy(Sᵥ))= 0.87 - (0 + 0.29)= 0.58

for(feature==shape)

entropy(circle) => -3/4(0/3 log0/3 + 3/3 log3/3)= 0

entropy(triangle) => -1/4(1/1 log 1/1 + 0/1 log 0/1)= 0

gain(s, color)= Entropy(S) - ∑((|Sᵥ|/ S|)* Entropy(Sᵥ))= 0.87 - (0 + 0)= 0.87

----------------------------

so that we have:

![image](https://user-images.githubusercontent.com/95109502/146342899-d6dd9138-d009-49f4-a920-e030d4a96517.png)
