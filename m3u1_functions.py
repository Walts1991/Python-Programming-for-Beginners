#functions used to save code to a single word

#Typically functions are defined in global variables at the top of the script

#Code not including a function
#x = 1
#y = 3
#print(x + y)

#Function syntax = def [name]():

def example(): #example is the name of the function
    x = 1
    y = 3
    print(x + y)
    if x < y:
        print(x,"is less than",y)

example()

#def main(): #Main loop to run all functions at the bottom of the script
#    example():
