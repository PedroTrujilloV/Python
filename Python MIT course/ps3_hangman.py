# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "F:/Python MIT course/PhytonMIT files/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if len(secretWord)<=0:
        return True
    else:
        return secretWord[0] in lettersGuessed and isWordGuessed(secretWord[1:], lettersGuessed)




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if len(secretWord)<=0:
        return secretWord
    elif secretWord[0] in lettersGuessed:
        return secretWord[0]+getGuessedWord(secretWord[1:], lettersGuessed)
    else:
        return '_ '+getGuessedWord(secretWord[1:], lettersGuessed)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    AvailableStr = string.ascii_lowercase
    AvailableStrC = ''
    
    for l in AvailableStr:
        if l not in lettersGuessed:
            AvailableStrC += l 
            
    return AvailableStrC
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = secretWord.lower()
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long.'
    lettersGuessed = []
    mistakesMade = 0
    MasxMistakesAlow = 8 
    backWord = ''
    inputLetter = ''
    
    while mistakesMade < MasxMistakesAlow:
        backWord = getGuessedWord(secretWord, lettersGuessed)
        print '-----------'
        print 'You have '+str(MasxMistakesAlow-mistakesMade)+' guesses left.'
        print 'Available Letters: '+getAvailableLetters(lettersGuessed)
        inputLetter = (raw_input("Please guess a letter: ")).lower()
        if inputLetter in lettersGuessed:
            print "Oops! You've already guessed that letter: "+backWord
        else:
            lettersGuessed.append(inputLetter)
            GuessedWord = getGuessedWord(secretWord, lettersGuessed)
            
            if isWordGuessed(secretWord, lettersGuessed):
                print 'Good guess: '+GuessedWord
                print '-----------'
                print 'Congratulations, you won!'
                break
            elif backWord == GuessedWord:                
                print 'Oops! That letter is not in my word: '+GuessedWord            
                mistakesMade+=1
            else:
                backWord = GuessedWord
                print 'Good guess: '+GuessedWord
            
    if mistakesMade>=MasxMistakesAlow:
        print '-----------'
        print 'Sorry, you ran out of guesses. The word was else.'






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
