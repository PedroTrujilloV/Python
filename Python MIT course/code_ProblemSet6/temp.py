# -*- coding: utf-8 -*-
# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random
import re

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
        if char not in "0123456789 !@#$%^&*()-_+={}[]|\\:;'<>?,./\"":
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
    while k < 26:
        for string in strList:            
            if  isWord(wordList,applyShift(string, k)):#25-k)):
                return k
        k += 1
    return 0
    

builcoder3= {'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'B', 'X': 'A', 'Z': 'C', 'a': 'd', 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 'v': 'y', 'y': 'b', 'x': 'a', 'z': 'c'}


print findBestShift(loadWords(),"Znk zkgiNkX'y tgsk oy ZghOzng") 
# = 20 Znk zkgiNkX'y tgsk oy ZghOzng?
print findBestShift(loadWords(),"Jk, XQp pdanA eo W PW jWiaz WHrej!")
# = 4
print findBestShift(loadWords(),"bvpbw cyqRqv aNnspm")
#print findBestShift(loadWords(),"Pmttw, ewztl!")
# =  'HelLo, world!' ,  key = 18 
#print findBestShift(loadWords(),"KhoOr, zruog!")
# =  'HelLo, world!' ,  key = 3 

