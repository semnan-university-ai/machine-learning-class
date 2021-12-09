Find-s algorithm step is:


1.Initilize h to the most specific hypothesis in H

2.For each positive training instance x For each attribute contraint ai in h If the contraint ai is satisfied by x then do nothing Else replace ai in h by the next more general constraint that is satisfied by x

3.Output the hypothesis h

![Table](https://user-images.githubusercontent.com/94211519/145341319-8adbf10a-b4dc-49c1-8a73-3b0f24bdc99a.PNG)



first we imagine all of our value is 0

h1=<0,0,0,0>

then we see our first example is true so we replace the 0 with the values that we have

x1=<Green,Soft,No,Wrinkled>

now check the next example but since the final result is no we do not change our h

x2=x1

third example is yes so we compare every eleming in x2 with third element and for every diffrence we replace element with ?

x3=<?,?,No,?>

next example final result is no so we ignore that one 

x4=x3

and in the last example we compare element again 

x5=<?,?,?,?>

so as final result we have our hypothesis which is  h=<?,?,?,?>
