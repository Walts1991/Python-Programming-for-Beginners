#Adds another layer of logic to if/else statement

#all if statements are run
#elif statements are only run if previous if/elif statements are false

x = 3
y = 7
z = 10

#Example 1 - Second statement is true
if x > y:
    print(x,"is greater than",y)
elif x < z:
    print(x,"is less than",z)
else:
    print("nothing was the case")

#Example 2 - First statement is true
if x < y:
    print(x,"is less than",y)
elif x < z:
    print(x,"is less than",z)
else:
    print("nothing was the case")

#Example 3 - No statements are true
if x > y:
    print(x,"is greater than",y)
elif x > z:
    print(x,"is greater than",z)
else:
    print("Nothing was the case")

#Example 4 - No statements are true
if x > y:
    print(x,"is greater than",y)
elif x > z:
    print(x,"is greater than",z)
elif y > z:
    print(y,"is greater than",z)
else:
    print("Nothing was the case")

#Example 5 - Multiple elif statements are true - Second statement is true - Break
if x > y:
    print(x,"is greater than",y)
elif x < z:
    print(x,"is less than",z)
elif y < z:
    print(y,"is less than",z)
else:
    print("Nothing was the case")

#Use if statements to check if multiple statements are true

#Example 6 - First statement contains conditional operator (and / or) - Can use multiple conditional operators
if x > y or x < z: #same as z > x > y
    print(x,"is greater than",y,"or",x,"is less than",z)
elif x < z:
    print(x,"is less than",z)
elif y < z:
    print(y,"is less than",z)
else:
    print("Nothing was the case")
