# f strings
def greet(name='Harsh'):
    print(f'Hey, {name}')

greet('krish')

def printCost(item, cost):
    print(f'Cost of {item} is {cost:.2f}')

printCost('Chicken', 54.09999)

# doc strings
def nullify():
    '''this is a doc string and can be accessed using functionName.__doc__'''
    pass

print(nullify.__doc__)
