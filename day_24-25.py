tup = (1, 3, 6)
listA = ['a', 'b', 'c']

# methods
print(tup.count(1))
print(tup.index(6))
print(tup)

tup3 = listA, tup
print(tup3)

print(list(tup))
print(tuple(listA))

tup3 = tup + tuple(listA)
print(tup3)



