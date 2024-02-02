#Tuples are immutable (cannot be changed once defined)
#Lists are mutable (can be changed once defined)

#Tuple - Sequence unpacking

def example():
    return 15,19

a,b = example() #unpack above return 15 to "a" and 19 to "b"

#Can define tuple by writing out a plain list e.g. 15,19 or use () e.g. (15,19)

print(a)
print(b)

#tuples used for items which we want to keep the same
#tuples take up less space for iteration

#List

x = [6,2,3,6,8,9,4,3]

print(x) #print entire list
print(x[5]) #print element which has ID = 5

#Can add/remove/combine/search/sort/count from lists
#Can append to a list

x.append(12)
print(x)

#Can insert elements into specific section of list

x.insert(5,7) #adds 7 to ID = 5 within list
print(x)

x.remove(7) #removes first 7 in the list
print(x)

print(x.index(12)) #Prints index ID where 12 is stored)

print(x.count(3)) #Counts how many 3's are in the list

x.sort() #Sorts list from smallest to largest
print(x)

#Lists do not have to be numbers

y=["Spot","Cam","Jan","Dave","Zack"]
print(y)
y.sort() #Sorts list in alphabetical order from a-z
print(y)

y.reverse() #Sorts list in alphabetical order from z-a
print(y)

#Sort changes the order of the list so the list ID also changes
