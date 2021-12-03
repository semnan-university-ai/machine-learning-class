x <- 1:5
for (val in x) {
if (val == 3){
break
}
print(val)
}

x <- 1:5
for (val in x) {
if (val == 3){
next
}
print(val)
}