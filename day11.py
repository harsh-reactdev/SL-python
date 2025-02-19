import random

fruitList = ['apple', 'mango', 'strawberry', 'watermelon', 'grapes', 'lychee']

rightWord = ''
blankStr = ''
guessedWord = ''
blanklist = []
guessCount = 0
remainingGuess = 5

# random word selection, the word to be guessed
def generateWord():
    global rightWord

    # wordPos = random.randint(0, 5)
    # rightWord = fruitList[wordPos]
    rightWord = random.choice(fruitList)

def generateBlanks(wordlen):
    global blankStr

    blankStr = '_' * wordlen
    print(blankStr)


def init():
    global guessCount, remainingGuess, rightWord

    rightWord = ''
    guessCount = 0
    remainingGuess = 5

    generateWord()
    generateBlanks(len(rightWord))

def updateGC():
    global guessCount

    guessCount = guessCount + 1

def updateRG():
    global remainingGuess

    remainingGuess = remainingGuess - 1

def replaceBlankWithLetter(letter):
    global blankStr, guessedWord, blanklist

    # blanklist[rightWord.index(letter)] = letter
    # guessedWord = ''.join(blanklist)
    # print(''.join(blanklist))
    # print(guessedWord)

    matchedIndices = [i for i, ltr in enumerate(rightWord) if ltr == letter]
    # print(matchedIndices)

    for ch in rightWord:
        if(ch == letter):
            for i in matchedIndices:
                blanklist[i] = letter
        else:
            continue
    
    guessedWord = ''.join(blanklist)
    
    print(guessedWord)


def guessWord():
    global guessCount, remainingGuess, blanklist

    init()
    blanklist = list(blankStr)

    if(not(remainingGuess)):
        print('Game over.!')

    while(remainingGuess):
        if(guessedWord == rightWord):
            print('Yay.! You guessed it.!')
            # init()
            return
        
        guessedLetter = (input('Guess a letter : ')).lower()
        
        if(guessedLetter in rightWord):
            replaceBlankWithLetter(guessedLetter)
        else:
            print('Wrong guess.!')
            updateRG()

guessWord()