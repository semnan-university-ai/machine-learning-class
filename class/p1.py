
"""
print("hello world.")
num1 = 10
print(num1)
num1 = "semnan"
num2 = 19.5
num3 = 87.7e100

"""
"""
# + / - *
print(2 * 3)
print(2 + 3)

number1 = 10
number2 = 20
#print(number1 - number2)
number3 = number1 / number2
print(number3)



x, y, z = 2, 10, 5
print(x)
print(y)
print(z)


variable1 = "semnan"
variable2 = 10
variable3 = 2.5
variable4 = False
variable5 = "25"""
"""print(type(variable1))
print(type(variable2))
print(type(variable3))
print(type(variable4))

print(variable2 * 5)
variable2 = str(variable2)
#print(type(variable2))
print(variable2 * 5)

print(variable2)
variable2 = float(variable2)
print(variable2)
number5 = -567
"""
"""
str1 = "i am happy"

#print(type(str1))
#print(str1)

print(str1[2:4])
print(len(str1))
print(len(str1[2:4]))\

"""
"""
students = "tosi, yazdi, hashemi, shokri, torabzade"
#print(students)
#print(len(students))
#print(type(students))

student1 = students[0:4]
student2 = students[7:11]
student3 = students[14:21]
print(student1)
print(student2)
print(student3)


print(students)
print(type(students))
print(len(students))
studentlist = students.split(", ")
print(studentlist)
print(type(studentlist))
print(len(studentlist))
print(studentlist[3])
"""
"""
mydate = "1380/10/03"
datesplitted = mydate.split("/")
#print("ali birthday is ", datesplitted[0])

firstname = "ali"
lastname = "ahmadi"
fullname = firstname + " " + lastname

#print(fullname)
number1 = 4

names = [ "amir", "ali", "fatemeh", "zahra" ]
str2 = "i am happy"
print("apz" in str2)

"""

"""

# List

names = [ "amir", "ali", "fatemeh", "zahra", "ali" ]
names[0] = "saeed"
#print(names[1:3])

for nm in names:
	print("my name is " + nm)


mylen = 0
for nm in names:
	mylen += len(nm)

#print(mylen)

names.append("alireza")
names.remove("ali")
names.remove("ali")

del names[2]
print(names)

"""

"""
# Tuple
names = ("ali", "amir", "hanie")
print(names)
print(type(names))
print(len(names))

names = list(names)
names[2] = "reza"
names = tuple(names)




# Set
names = { "amir", "ali", "zahra", "hanie" }
#print(names)
#print(type(names))
#print(len(names))

for nm in names:
	print("my name is " + nm)



#names.add("reza")
names.update(["amir", "ali", "sepehr", "zahra", "hanie"])

names.remove("ali")

names = tuple(names)
#print(names[2])"""

"""

# Dictionary
persons = {
	"person1":{
		"name":"ali",
		"lastname":"ahmadi",
		"birthday":"1383/02/11",
		"age":17,
		"weight":83.2
	},
	"person2":{
		"name":"sara",
		"lastname":"abasi",
		"birthday":"1383/02/11",
		"age":17,
		"weight":83.2
	},
}

#print(persons["lastname"])
#print(persons.get("lastname"))
print(persons["person2"]["name"])

"""

a = 21
b = 2
"""
if a > b:
	if b < a:
		c = a + 2
	else:
		c = a + 3

	c = a * b
	print("salam")
	print(c * 2)
elif a == b:
	print("22")
else:
	print("bye")
"""

# if a > b print(1) else print(2)