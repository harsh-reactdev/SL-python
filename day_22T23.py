listA = [1, 2, 3, 'harsh', True, [4, 5, 6]]

# len() gives us the length of the list
print(len(listA))

# to check if an element is present in the list:
if 'harsh' in listA: #this works on strings too
    print('Yes')
else:
    print('No')


# ------------------------------------------------
# list comprehensions
listB = [i*i for i in range(1, 20) if i%2==0]
print(listB)

# methods
listC = listA + listB
print(listC)

print(listA)