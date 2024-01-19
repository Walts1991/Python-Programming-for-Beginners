#While a condition is true, do something
condition = 1
while condition <= 10: #Condition is true while the value is less than or equal to 10
    print(condition)
    condition +=1 #adds 1 to the value each time
    #same as condition = condition + 1

#condition = '5' #String generates an error
#while condition < 15: #Infinite loop as 5 will always be less than 15
#    print('True')

while True:
    print('Infinite')