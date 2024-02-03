#One of the most useful data types - a lot like a database / associated arrays in other languages
#Uses unique keys with values
#Lists/Tuple are ordered - Dictionaries are unordered
#Dictionaries are mutable - Can be changed
#Would not use insert/sort/reverse as dictionaries are not ordered

gradeDict = {"Kelly":89,"David":65,"Jack":95,"Samantha":78} #Dictionaries use {key:value} syntax
#Typically keys are integers or strings

print(gradeDict) #Print dictionary
print(gradeDict["David"]) #Print value for specific key - Syntax = print(dictionary["key"])

gradeDict["David"] = 56 #To amend David's grade to 56 - Syntax = dictionary["key"]
print(gradeDict)

gradeDict["Jesse"] = 92 #Adds Jesse to dictionary - Same syntax as amendments in line 13
print(gradeDict)

del gradeDict["David"] #Delete "David" from dictionary - Syntax = del dictionary["key"]
print(gradeDict)

#Can uses lists to add scores from additional tests
gradeDict = {"Kelly":[89,88],
             "Jack":[95,87],
             "Samantha":[78,89],
             "Jesse":[92,99]}
print(gradeDict)

print(gradeDict["Jesse"])
print(gradeDict["Jesse"][0]) #Can use syntax - dictionary["key"][index] - to find specific values
