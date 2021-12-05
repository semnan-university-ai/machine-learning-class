این الگوریتم به دنبال یک فرضیه خاص در بین تمام داده های آموزشی میباشد و آن را نمایش میدهد.

مثال:

1. Initilize h to the most specific hypothesis in H
2. For each positive training instance x
For each attribute contraint ai in h
If the contraint ai is satisfied by x
then do nothing
Else
replace ai in h by the next more general constraint that is satisfied by x
3. Output the hypothesis h

![Capture](https://user-images.githubusercontent.com/94211519/144725826-f75c3750-e7ea-464f-8a8e-9bcecd5c5724.PNG)


first we imagine all of our value is 0

h0 = <0,0,0,0,0>

then we see our first example is true so we replace the 0 with the values that we have
x1=<green,big,yes,yes>
h1=<green,big,yes,yes>

now we check the next colum and we check every element we have with the new values and if their diffrent we replace it with "?"
x2=<green,small,yes,no>
h2=<green,?,yes,?>

now we check next one
x3=<red,big,yes,yes>

since the final result is no we do not change h and we go for next one
h3=<green,?,yes,no>

x4=<green,small,yes,yes>
h4=<green,?,yes,?>

so as final result we can our hypothesis  is <green,?,yes,?>
