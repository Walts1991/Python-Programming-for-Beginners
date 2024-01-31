import statistics as s #Use "as [name]" to rename modules"

exList = [4,5,3,7,2,4,8,1,7,6,9,4]

print(s.mean(exList))

#Below code can also be used

from statistics import mean #Can import only specific functions from module
print(mean(exList))

#Below code adds shorthand naming to the above

from statistics import mean as m
print(m(exList))

#Below code adds standard deviation

from statistics import mean, stdev
print(mean(exList))
print(stdev(exList))

#Below code adds standard deviation with renaming

from statistics import mean as m, stdev as s
print(m(exList))
print(s(exList))

#Below code is alternative to first / second example - imports all functions of module

from statistics import * #asterisk is a wildcard and includes everything
print(mean(exList))
print(stdev(exList))
