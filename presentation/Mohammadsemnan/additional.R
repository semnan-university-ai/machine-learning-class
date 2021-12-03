abs(-11)
log(9,3)
sqrt(16)

x=c(1,2)
y=c(4,6)

plot(x,y)
arrows(x[1],y[1],x[2],y[2])

#install.packages("ggplot2")
library(ggplot2)
qplot(wt, mpg, data = mtcars, colour = factor(cyl))

x<<- readline(prompt = "Enter your input      ")
x="123"
print(x)

x<-paste(1,'two',3,'four',5,'six')

paste(1,'two',3,'four',5,'six',sep =" & ")

paste(c(1,2,3,4,5,6,7,8),sep = "_")
paste(c(1,2,3,4,5,6,7,8),collapse = "_")
