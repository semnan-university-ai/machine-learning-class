check <- function(x) {
if (x > 0) {
result <- "Positive"
}
else if (x < 0) {
result <- "Negative"
}
else {
result <- "Zero"
}
return(result)
}

check(1)


check <- function(x) {
if (x > 0) {
result <- "Positive"
}
else if (x < 0) {
result <- "Negative"
}
else {
result <- "Zero"
}
result
}



check <- function(x) {
if (x>0) {
return("Positive")
}
else if (x<0) {
return("Negative")
}
else {
return("Zero")
}
}




multi_return <- function() {
my_list <- list("color" = "red", "size" = 20, "shape" = "round")
return(my_list) 
}
a <- multi_return()