x <- factor(c("single", "married", "married", "single")); 
x 
x[3] 
x[c(2, 4)]
x[-1] 


x <- factor(c("single", "married", "married", "single"), levels = c("single", "married", "divorced"));
x
x[2] <- "divorced"
x


levels(x) <- c(levels(x), "unknown")
x[3] <- "unknown"
x
str(x)

x <- factor(c("single","married","married","single"))
str(x)

