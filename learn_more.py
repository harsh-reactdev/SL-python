# Iterables

# different built-in functions that uses iterables as an argument
sortedNames = sorted(['harsh', 'keerthana', 'chaitanya', 'manohar'])
# print(sortedNames)

sumOfelems = sum([10, 12, 24, 54, 23, 11, 9, 22])
# print(sumOfelems)

checkAny = any([0, 0 , 0 , 0, 0, 0]) #all values are falsy. So returns False
checkAny = any([0, 0 , 0 , 0, 1, 0]) #only one value is truthy. So returns True
# print(checkAny)

checkAll = all([1, 1 , 1 , 1, 1, 1]) #all values are truthy. So returns True
# print(checkAll)
checkAll = all([1, 1 , 1 , 1, 0, 1]) #one of the values is falsy. So returns False
# print(checkAll)

#-------------------------------------------------------------------------
x = 10
xtype = isinstance(x, int) # returns True if x is of type int

#-------------------------------------------------------------------------
import math

mathTest1 = math.sqrt(4)
mathTest2 = math.log10(20)
mathTest3 = math.factorial(5)

#-------------------------------------------------------------------------

