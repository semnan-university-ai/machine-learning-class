import os
"""
path="../data/sms/"
path="../data/news/"
"""
list = []
outputcontent = ""

for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.txt' in f:
        	filecontent = open(path + f, mode="r")
        	filecontent = filecontent.read()
        	# print(filecontent)

        	outputcontent += filecontent.replace("\n", "") + "\n"

"""
with open('smsout.txt', mode="a") as f:
	f.write(outputcontent)
with open('newsout.txt', mode="a") as f:
	f.write(outputcontent)
"""