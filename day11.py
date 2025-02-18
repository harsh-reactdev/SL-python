import random

# fruits = "Apple, Apricot, Avocado, Banana, Bilberry, Blackberry, Blackcurrant, Blueberry, Boysenberry, Currant, Cherry, Cherimoya, Chico fruit, Cloudberry, Coconut, Cranberry, Cucumber, Custard apple, Damson, Date, Dragonfruit, Durian, Elderberry, Feijoa, Fig, Goji berry, Gooseberry, Grape, Raisin, Grapefruit, Guava, Honeyberry, Huckleberry, Jabuticaba, Jackfruit, Jambul, Jujube, Juniper berry, Kiwano, Kiwifruit, Kumquat, Lemon, Lime, Loquat, Longan, Lychee, Mango, Mangosteen, Marionberry, Melon, Cantaloupe, Honeydew, Watermelon, Miracle fruit, Mulberry, Nectarine, Nance, Olive, Orange, Blood orange, Clementine, Mandarine, Tangerine, Papaya, Passionfruit, Peach, Pear, Persimmon, Physalis, Plantain, Plum, Prune, Pineapple, Plumcot, Pomegranate, Pomelo, Purple mangosteen, Quince, Raspberry, Salmonberry, Rambutan, Redcurrant, Salal berry, Salak, Satsuma, Soursop, Star fruit, Solanum quitoense, Strawberry, Tamarillo, Tamarind, Ugli fruit, Yuzu"

fruitList = ['apple', 'mango', 'strawberry', 'watermelon', 'grapes', 'lychee']
# fruitList = fruits.split(",")
# print(len(fruitList))

rightWord = ''
blankStr = ''
guessedWord = ''
blanklist = []
guessCount = 0
remainingGuess = 5

# random word selection, the word to be guessed
def generateWord():
    global rightWord

    wordPos = random.randint(0, 5)
    rightWord = fruitList[wordPos]

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

    blanklist[rightWord.index(letter)] = letter
    guessedWord = ''.join(blanklist)
    # print(''.join(blanklist))
    print(guessedWord)

def guessWord():
    global guessCount, remainingGuess, blanklist

    init()
    blanklist = list(blankStr)

    while(remainingGuess):
        guessedLetter = input('Guess a letter : ')

        if(guessedLetter in rightWord):
            replaceBlankWithLetter(guessedLetter)
        else:
            updateRG()

guessWord()