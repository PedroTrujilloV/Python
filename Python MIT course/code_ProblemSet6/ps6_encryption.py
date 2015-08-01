# -*- coding: utf-8 -*-
# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "F:/Python MIT course/PhytonMIT files/code_ProblemSet6/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("F:/Python MIT course/PhytonMIT files/code_ProblemSet6/story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    assert 0 <= shift < 26, 'Index not 0 <= int < 26'
    try:
        upperStr = string.ascii_uppercase
        lowerStr = string.ascii_lowercase
        asciiList = list(upperStr)[:] + list(lowerStr)[:]#[::-1].split()
        shiftList = list(upperStr)[shift:]+list(upperStr)[:shift]+list(lowerStr)[shift:]+list(lowerStr)[:shift]
        shiftDic =  {}
        
        for index in range(len(asciiList)):
            shiftDic[asciiList[index]] = shiftList[index]
        '''
        let = 0
        for key in asciiList:
            
            shiftDic[key] = shiftList[let]
            let+=1
            
        print asciiList
        print shiftList
        print  shiftDic
        '''
        return shiftDic # Remove this comment when you code the function
        
    except KeyError:        
        raise ValueError('Letter not in shiftDic')
    except IndexError:        
        raise ValueError('Index not 0 <= int < 26')
    except TypeError:        
        raise ValueError('Index must int number')

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
       
    textC = ''
    
    for index in range(len(text)):
        char = text[index]
        if char not in "0123456789 !@#$%^&*()-_+={}[]|\\:;'<>?,./\n\"":
            textC += coder[char]
        else:
            textC += char
        
    return textC

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    assert 0 <= shift < 26, 'Index not 0 <= int < 26'
    return applyCoder(text, buildCoder(shift)) 

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    
    pseudo: 
        0:
            creo y asigno valor de 0 a "K" (shift)
        1:
            importo libreria re
            
        2:
            Aplico funcion split(expresion regular) a text y guardo resultado en strList
        3:
            Ordeno (sort) strList por tamaño de cadena de  mayor a menor 
            
        4:
            mientras K sea menor a 26 hacer:
                
            5:
                Loop, recorro strList n:
            6:
                    si applyShift(string[n], K) convertido a lowercase está en isWord():
            7:
                        returnar K
            9:  
                incremento 1 a K 
            10:
                retorno 0 si no existe llave
    """
    ### TODO
    
    k = 0
    import re
    strList = re.split(" |'|0-9|!|@|\.|#|$|\"|%|&|/|·|^",text)
    strList.sort(lambda y,x: cmp(len(x), len(y))) 
    #print strList
    while k < 26:
        succes = 0
        for string in strList:     
            if  isWord(wordList,applyShift(string, k)):#25-k)):
                succes += 1
                if succes == len(strList)/2:
                    return k
        k += 1
    return 0

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    stringH = getStoryString()
    key = findBestShift(loadWords(), stringH)    
    return applyShift(stringH, key) 

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    '''
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    '''
    # To test decryptStory, comment the above four lines and uncomment this line:
    print decryptStory()
