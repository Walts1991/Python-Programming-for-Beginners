#If/Else statement adds another layer of logic to statement

#If something is the case do something, if not do something else

x = 13
y = 6

#Example 1
if x < y:
    print(x,"is less than",y)
else:
    print(x,"is not less than",y)

#Example 2
if x < y:
    print(x,"is less than",y)
if x > y:
    print(x,"is greater than",y)
else:
    print(x,"is not less than",y)

#else statement will only run if immediately preceding if statement is false
#elif statement is used if multiple if statements are needed to be to trigger else statement
