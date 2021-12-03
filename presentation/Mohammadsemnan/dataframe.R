x <- data.frame("SN" = 1:2, "Age" = c(21,15), "Name" = c("John","Dora"))
str(x) 

names(x)
ncol(x)
nrow(x)
length(x)

x <- data.frame("SN" = 1:2, "Age" = c(21,15), "Name" = c("John", "Dora"), stringsAsFactors = FALSE)
str(x) 

x["Name"]
x$Name
x[["Name"]]
x[[3]]

x[1,"Age"] <- 20
rbind(x,list(1,16,"Paul"))
cbind(x,State=c("NY","FL"))
x$State <- c("NY","FL")

x$State <- NULL
x <- x[-1,]

library(help = "datasets")

str(trees)
head(trees,n=3)
trees[2:3,] 
trees[trees$Height > 82,] 

trees[10:12,2]
trees[10:12,2, drop = FALSE]
