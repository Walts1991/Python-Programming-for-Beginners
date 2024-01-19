#If Statement - if something is this then do that

x = 2
y = 7
z = 10

if x > y:
    print(x,"is greater than",y)

if x < y:
    print(x,"is less than",y)

if x == y: #Double == is used to compare if two values are equal
    print(x,"is the same as",y)

if x == '2': #No result as x does not equal string of 2
    print(x,"equals the string",2)

#if x < '2': #Error as different data types integer / string
    #print(x,"is less than 2")

if x <= y:
    print(x,"is less than or equal to",y)

if x >= y:
    print(x,"is greater than or equal to",y)

if z > y > x:
    print(z,"is greater than",y,"which is greater than",x)

if z > y > x < z > y: #Can continue to add logic as required
    print(z,"is greater than",y,"which is greater than",x)
