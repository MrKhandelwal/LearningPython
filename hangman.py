# 
# Hangman game
#

import random
import string

WORDLIST_FILENAME = "wordsHangman.txt"

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
    if len(secretWord) == 1 and secretWord[0] in lettersGuessed:
        return True
    elif secretWord[0] in lettersGuessed:
        return isWordGuessed(secretWord[1:], lettersGuessed)
    return False    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    temp = ''
    for i in secretWord:
        if i not in lettersGuessed:
            temp += '_ '
        else:
            temp += i
    return temp    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    temp = ''
    s = string.ascii_lowercase
    for i in s:
        if i not in lettersGuessed:
            temp += i
    return temp    
    

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
    guessLeft = 8
    lettersGuessed = ''
    
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'    
    print '-------------'
    
    while guessLeft > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print 'Congratulations, you won!'
            break
        print 'You have ' + str(guessLeft) + ' guesses left.'
        print "Available letters: ", 
        print getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ')    
        if guess.lower() not in lettersGuessed:
            lettersGuessed += guess.lower()
            if guess.lower() in secretWord:
                print "Good guess: ", 
                print getGuessedWord(secretWord, lettersGuessed)
            else:
                print "Oops! That letter is not in my word: ", 
                print getGuessedWord(secretWord, lettersGuessed)
                guessLeft -= 1
        else:
            print "Oops! You've already guessed that letter: ", 
            print getGuessedWord(secretWord, lettersGuessed)
            
            
        print '-------------'
        
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print 'Sorry, you ran out of guesses. The word was ' + secretWord 
 

# you might want to pick your own secretWord

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
