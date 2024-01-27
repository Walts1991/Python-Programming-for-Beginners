#can add .read() below to line to save a line of code
readMe = open("m5u2_exampleFile.txt","r",encoding="utf-8").read() #encoding added
print(readMe)

#Above prints as a single string
#Can split the string using the below function and parameter e.g. at each new line

splitMe = readMe.split("\n")
print(splitMe)

#Adds the text to a python list
print(splitMe[2])

#Can use .readlines to automatically add data to a list
readMe2 = open("m5u2_exampleFile.txt","r",encoding="utf-8").readlines()
print(readMe2)

#note above includes new lines "\n" within list entries, can be split but not shown in course
