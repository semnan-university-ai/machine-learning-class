pow <- function(x, y) {
# function to print x raised to the power y
result <- x^y
print(paste(x,"raised to the power", y, "is", result))
}

pow(8, 2)
pow(x = 8, y = 2)
pow(y = 2, x = 8)

pow <- function(x, y = 2) {
# function to print x raised to the power y
result <- x^y
print(paste(x,"raised to the power", y, "is", result))
}

pow(3)
pow(3,1)