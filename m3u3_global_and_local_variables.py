#global variables is one that can be accessed anywhere globally
#can be accessed locally but cannot be modified locally inherently

#local variables are is one that can only be accessed in its locale
#cannot be accessed globally inherently but can be modified locally

x = 6 #global variable - local to everything under it

def example3(): #see note below re example3 - not considered best practice
    global x
    x += 1
    print(x)

example3()
print(x)

def example():
    z = 5 #local variable
    print(z)

#print(z) #z is not defined, as local to example function

example()

def example2():
    z = 7
    print(z)
    print(x)
    #x += 1 #same as x = x + 1 #unable to modify x within local function
    #print(x)
    y = x + 1 #use another variable name instead as can call x but not modify
    print(y)
    return y

example2()

x = example2()
print(x)

#local variables often seen as best practice

#if still want to use global variables as intended originally - see example3 above
