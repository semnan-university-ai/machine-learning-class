x <- list("a" = 2.5, "b" = TRUE, "c" = 1:3)
str(x)

x <- list(2.5,TRUE,1:3)
x

y<- list("En","Fr")

x <- list("name" = "John", "age" = 19, "language" =y)

x[c(1:2)]
x[c(T,F,T)]
x[c("age","language")]

x["age"]
typeof(x["age"]) 
x[["age"]]
typeof(x[["age"]])
x$name
x$a
x[["a"]]

x[["name"]] <- "Clair"
x

x[["married"]] <- FALSE
x

x[["age"]] <- NULL
str(x)

x$married <- NULL
str(x)