#Input from user - built in function = input()

name = input("What is your name? ") #Good to add a space for readability post input
print("Hello",name)

#Statistics - Import Statistics module

import statistics

exList = [4,5,3,7,2,4,8,1,7,6,9,4]

x = statistics.mean(exList)
print(x)

x = statistics.median(exList)
print(x)

x = statistics.mode(exList)
print(x)

x = statistics.stdev(exList)
print(x)

x = statistics.variance(exList)
print(x)
