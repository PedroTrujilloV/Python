# -*- coding: utf-8 -*-
from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0

    # Create a new variable to store the best word seen so far (initially None)  
    bWordSeen = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):

            # Find out how much making that word is worth
            bestScore = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if maxScore < bestScore:
                

                # Update your best score, and best word accordingly
                maxScore = bestScore
                bWordSeen = word


    # return the best word you found.
    #print bWordSeen
    return bWordSeen


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    word = ''
    totalScore = 0
    #hand2 = hand.copy()
    #hand = hand.copy()
        
    # Keep track of the total score
    totalScore = getWordScore(word, n)
        
    # As long as there are still letters left in the hand:
    while  calculateHandlen(hand) > 0:
    
        # Display the hand
        print 'Current Hand:  ',
        displayHand(hand)
        
        # Ask user for input (default)
        #word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        
        #changes for machine (Skynet):
        #option = raw_input('Ask Skynet´s word (any key), or a "." to indicate that you are finished: ')
        option = 'm'
        # If the input is a single period:(default)
        #if word == '.':
        #changes for machine (Skynet):
        if option == '.':
            
            # End the game (break out of the loop)
            print 'Goodbye!',
            break

        # Otherwise (the input is not a single period):
        else:
            
            #changes for machine (Skynet):
            word = compChooseWord(hand, wordList, n)
        
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                            
                # Reject invalid word (print a message followed by a blank line)
                #changes for machine (Skynet):
                #print 'Invalid word, please try again.'
                #changes for machine (Skynet):
                break
                print 

            # Otherwise (the word is valid):
            else:

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                earned = getWordScore(word, n)
                totalScore += earned
                print '"'+word+'" earned '+str(earned)+' points. Total: '+str(totalScore)+' points'
                print
                # Update the hand 
                hand = updateHand(hand, word)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    '''
    if calculateHandlen(hand) == 0 and totalScore >0:
        print 'Run out of letters.',
    '''
    print 'Total score: '+str(totalScore)+' points.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    lastHand ={}
    while True:
        inPut = raw_input( 'Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if inPut == 'e':
            break
        elif inPut != 'r' and inPut != 'n':
            print 'Invalid command.'
        else:
            if inPut == 'n':
                lastHand = dealHand(HAND_SIZE).copy()
            if lastHand == {}:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                while True:
                    inPut2 = raw_input( 'Enter u to have yourself play, c to have the computer play: ')
                    if inPut2 != 'u' and inPut2 != 'c':
                        print 'Invalid command.'
                    else:               
                        if inPut2 == 'u':  
                            playHand(lastHand, wordList, HAND_SIZE)
                        else:
                            compPlayHand(lastHand, wordList, HAND_SIZE)
                        break
                    
                
                    
                    
    '''
    lastHand ={}
    n = HAND_SIZE
    def inputSelection(lastHand,wordList,n):
        if lastHand == {}:
            print 'You have not played a hand yet. Please play a new hand first!'
        else:
            inPut2 = raw_input( 'Enter u to have yourself play, c to have the computer play: ')
            while True:
                    if inPut2 != 'u' and inPut2 != 'c':
                        print 'Invalid command.'
                    else:
                        if inPut2 == 'u':              
                            playHand(lastHand, wordList, n)
                        else:
                            compPlayHand(lastHand, wordList, n)
                        break
    while True:
        inPut = raw_input( 'Enter n to deal a new hand, r to replay the last hand, or e to end game: ') 
        if inPut == 'e':
            break
        elif inPut != 'r' and inPut != 'n':
            print 'Invalid command.'
        else:
            if inPut == 'n':
                lastHand = dealHand(n).copy()
            inputSelection(lastHand,wordList,n)

    '''
#
# Build data structures used for entire session and play game
#



if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    
#compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)



