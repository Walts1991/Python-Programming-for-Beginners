#Try a block of code
#Except if there is an exception, what do you want to do
#Logging if exception exists, what to do in the future

try:
    print("Running the try...")
    print("5"+5)
except Exception as e:
    print(str(e))
    print("Do more things...")

print("Code continues onward...")

#Without try / except above, the code fails on line 7 due to TypeError

#print("Running the try...")
#print("5"+5)
#print("Code does not continue onward...")

#When working with a lib, third party API or similar, may not be able to cover all errors in code

try:
    print("Running the try...")
    import mars #ImportError - General exception
    print("5"+5) #TypeError
    print("5"+x) #NameError
except TypeError as t:
    print("TypeError triggered")
    print(str(t))
except NameError as n:
    print("NameError triggered")
    print(str(n))
except Exception as e:
    print("General exception")
    print(str(e))

#To save specific errors, can use Python's logging function and log the error in a log file
#Save to a notepad.txt file with error details - save whole error
#Can also print error within the code by adding print(str([exception variable e.g. e as per above]))

try:
    name = input("What is your name? ") #Expect string - can add alert e.g. capitalize first letter
    age = input("What is your age? ") #Expect integer - can add alert e.g. whole number
    print(str(name))
    print(int(age))
except TypeError as t:
    print("TypeError triggered")
    print(str(t))
except NameError as n:
    print("NameError triggered")
    print(str(n))
except Exception as e:
    print("General exception")
    print(str(e))
