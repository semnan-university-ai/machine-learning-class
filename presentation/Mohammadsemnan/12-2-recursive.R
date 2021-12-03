recursive.factorial <- function(x) {
if (x == 0)    return (1)
else           return (x * recursive.factorial(x-1))
}

recursive.factorial(0)

recursive.factorial(5)