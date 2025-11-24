# functions

# function to print the occurance of a character in a string

def checkOccurance(inpStr):
    strDict = {}

    for char in inpStr.lower():
        if char in strDict:
            strDict[char]+=1
        else:
            strDict[char] = 1
        
    print(strDict)

# checkOccurance('Hey, I am harsh.!')





