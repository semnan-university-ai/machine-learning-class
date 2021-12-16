Find-s algorithm step is:

1.Initilize h to the most specific hypothesis in H

2.For each positive training instance x For each attribute contraint ai in h If the contraint ai is satisfied by x then do nothing Else replace ai in h by the next more general constraint that is satisfied by x

3.Output the hypothesis h

first we imagine all of our value is 0

h0 = <0,0,0,0,0>

we see our first example is No we do not change our h

x1=<0,0,0>

then we see our first example is No we do not change our h

X2=X1

The next example class is Yes so we replace all the data

X3=<S,R,C>

Fourth example class is no so we ignor that and do not change our h

X4=x3

In Final data the class is Yes so we replace all of the data that is not set

X5=<S,?,C>

Our Final h is <S,?,C>

