#Most errors are typos,
    #misunderstanding of standards / syntax,
    #missing module,
    #wrong python version etc

#Python IDE's automatically indent - check indentation
#Check typos for function / variable names

#name error - typo - exception - will continue to run program if exception error
"""variable = 55
print(varaible)

varaible = 55
print(variable)"""

#Read errors for details on the error including line number

#indentation error - syntax error - will stop program from running entirely
#expected an indent (can have parent / child functions which are nested)
"""def func1():

def func2():
    print(2)"""

#unexpected indent
"""Python is a scripted language that runs line by line
def task():
    print("1")

print("2")

    print("3")"""

#unterminated string literal / "(" not closed
"""
print("Hey there how are you today?
print("Hey there how are you today?"""
      #automatic indent should be a flag that something may be wrong

#x = [1,6,23,3,23 - similar error to above

#Modules must be same version as Python e.g. 64 bit
